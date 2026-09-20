"""Client for the ESPHome Device Builder API.

ESPHome 2026.7 replaced the dashboard with Device Builder and dropped the old
REST API. `/edit` and `/validate` are gone; `/compile` and `/upload` became
websocket upgrades. Worse, Device Builder registers `add_get("/{tail:.*}")` as
a catch-all, so every dead route answers `200 text/html` with the SPA index —
a dead endpoint looks like a success and returns a web page. `_reject_spa`
exists so that can never reach a caller as content again.

Everything except the config listing now goes over the websocket API at `/ws`.
"""

import asyncio
import json
import re
import threading
import uuid
from typing import Any

import httpx
import websockets

from esphome_mcp.config import ESPHOME_DASHBOARD_URL

# Device Builder emits colour codes as the literal six characters `\033[` as
# often as it emits a real ESC byte, so both forms have to go.
_ANSI = re.compile(r"(?:\x1b|\\033|\\x1b|\\u001b)\[[0-9;]*[A-Za-z]")


def _client(**kwargs) -> httpx.Client:
    return httpx.Client(base_url=ESPHOME_DASHBOARD_URL, **kwargs)


def _reject_spa(r: httpx.Response, endpoint: str) -> None:
    if "html" in r.headers.get("content-type", ""):
        raise RuntimeError(
            f"{endpoint} no longer exists on the ESPHome Device Builder "
            f"({ESPHOME_DASHBOARD_URL}); its SPA catch-all returned the index page."
        )


def _ws_url() -> str:
    base = ESPHOME_DASHBOARD_URL.rstrip("/")
    if base.startswith("https://"):
        return "wss://" + base[len("https://"):] + "/ws"
    return "ws://" + base[len("http://"):] + "/ws"


def _run(coro):
    """Run *coro* to completion from sync code, event loop running or not."""
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return asyncio.run(coro)

    box: dict[str, Any] = {}

    def target():
        try:
            box["value"] = asyncio.run(coro)
        except BaseException as err:  # re-raised on the calling thread
            box["error"] = err

    t = threading.Thread(target=target)
    t.start()
    t.join()
    if "error" in box:
        raise box["error"]
    return box["value"]


async def _command(command: str, args: dict, timeout: float, stream: bool) -> Any:
    """Issue one websocket command.

    Device Builder greets every connection with an unsolicited server-info
    frame and multiplexes by `message_id`, so anything not carrying ours is
    dropped. A streaming command emits `event: output` per line and terminates
    on `event: result`; a plain command answers with a single `result` key.
    """
    message_id = uuid.uuid4().hex
    lines: list[str] = []

    async with websockets.connect(_ws_url(), max_size=None, open_timeout=15) as ws:
        await ws.send(json.dumps({"command": command, "message_id": message_id, "args": args}))
        while True:
            frame = json.loads(await asyncio.wait_for(ws.recv(), timeout=timeout))
            if frame.get("message_id") != message_id:
                continue

            if "error_code" in frame:
                raise RuntimeError(
                    f"{command} failed: {frame['error_code']} — "
                    f"{frame.get('details', 'no detail given')}"
                )

            if not stream:
                return frame.get("result")

            event = frame.get("event")
            if event == "output":
                lines.append(_ANSI.sub("", str(frame.get("data", ""))))
            elif event == "result":
                return "\n".join(lines)


def list_configs() -> list[str]:
    """Device filenames, from the legacy `{config.yaml: online?}` map."""
    with _client(timeout=10) as c:
        r = c.get("/ping")
        r.raise_for_status()
        _reject_spa(r, "GET /ping")
        data = r.json()
        if isinstance(data, dict):
            return list(data.keys())
        return [item["name"] if isinstance(item, dict) else item for item in data]


def read_config(configuration: str) -> str:
    return _run(_command("devices/get_config", {"configuration": configuration}, 30, False))


def write_config(configuration: str, content: str) -> dict:
    _run(
        _command(
            "devices/update_config",
            {"configuration": configuration, "content": content},
            60,
            False,
        )
    )
    return {"status": "ok"}


def validate_config(configuration: str, timeout: float = 120) -> str:
    """`show_secrets` is left at its default False so Device Builder strips the
    ANSI-concealed secret runs server-side; never turn it on from here."""
    return _run(_command("devices/validate", {"configuration": configuration}, timeout, True))


def compile_config(configuration: str, timeout: float = 900) -> str:
    """Queue a build, then follow its job stream to completion."""
    job = _run(_command("firmware/compile", {"configuration": configuration}, 60, False))
    job_id = job.get("job_id") if isinstance(job, dict) else job
    if not job_id:
        raise RuntimeError(f"firmware/compile returned no job id: {job!r}")
    return _run(_command("firmware/follow_job", {"job_id": job_id}, timeout, True))


def run_dashboard_operation(operation: str, configuration: str, timeout: int = 300) -> str:
    if operation == "validate":
        return validate_config(configuration, timeout=timeout)
    if operation == "compile":
        return compile_config(configuration, timeout=timeout)
    raise ValueError(f"unsupported operation: {operation}")
