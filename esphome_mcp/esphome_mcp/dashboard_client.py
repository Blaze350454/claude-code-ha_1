import httpx
from esphome_mcp.config import ESPHOME_DASHBOARD_URL


def _client(**kwargs) -> httpx.Client:
    return httpx.Client(base_url=ESPHOME_DASHBOARD_URL, **kwargs)


def list_configs() -> list[str]:
    with _client(timeout=10) as c:
        r = c.get("/ping")
        r.raise_for_status()
        data = r.json()
        if isinstance(data, dict):
            return list(data.keys())
        return [item["name"] if isinstance(item, dict) else item for item in data]


def read_config(configuration: str) -> str:
    with _client(timeout=10) as c:
        r = c.get("/edit", params={"configuration": configuration})
        r.raise_for_status()
        return r.text


def write_config(configuration: str, content: str) -> dict:
    with _client(timeout=10) as c:
        r = c.post(
            "/edit",
            content=content.encode(),
            params={"configuration": configuration},
            headers={"Content-Type": "text/plain"},
        )
        r.raise_for_status()
        return {"status": "ok"}


def run_dashboard_operation(operation: str, configuration: str, timeout: int = 300) -> str:
    """POST to /compile, /validate, or /upload and collect streamed output."""
    lines = []
    with _client(timeout=timeout) as c:
        with c.stream("POST", f"/{operation}", json={"configuration": configuration}) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if line.strip():
                    lines.append(line)
    return "\n".join(lines)
