"""Proxmox VE API client for MCP server integration."""

import os
import ssl
import sys
from typing import Any, Dict, List, Optional

import aiohttp


class ProxmoxClient:
    """Async client for Proxmox VE REST API."""

    def __init__(
        self,
        url: Optional[str] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        node: Optional[str] = None,
    ):
        self.url = (url or os.getenv("PROXMOX_URL", "")).rstrip("/")
        self.username = username or os.getenv("PROXMOX_USER", "root@pam")
        self.password = password or os.getenv("PROXMOX_PASSWORD", "")
        self.node = node or os.getenv("PROXMOX_NODE", "proxmox")

        if not self.url:
            raise ValueError("Proxmox URL not provided. Set PROXMOX_URL env var.")
        if not self.password:
            raise ValueError("Proxmox password not provided. Set PROXMOX_PASSWORD env var.")

        self._ticket: Optional[str] = None
        self._csrf_token: Optional[str] = None
        # Skip SSL verification for self-signed Proxmox certs
        self._ssl = ssl.create_default_context()
        self._ssl.check_hostname = False
        self._ssl.verify_mode = ssl.CERT_NONE

        print(f"ProxmoxClient initialized for {self.url}", file=sys.stderr)

    async def _authenticate(self) -> None:
        """Obtain a Proxmox auth ticket."""
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.url}/api2/json/access/ticket",
                data={"username": self.username, "password": self.password},
                ssl=self._ssl,
            ) as resp:
                resp.raise_for_status()
                data = await resp.json()
                self._ticket = data["data"]["ticket"]
                self._csrf_token = data["data"]["CSRFPreventionToken"]

    async def _request(
        self,
        method: str,
        path: str,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        if not self._ticket:
            await self._authenticate()

        def _headers():
            return {
                "CSRFPreventionToken": self._csrf_token,
                "Cookie": f"PVEAuthCookie={self._ticket}",
            }

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method,
                f"{self.url}/api2/json{path}",
                headers=_headers(),
                json=json_data,
                ssl=self._ssl,
            ) as resp:
                if resp.status == 401:
                    self._ticket = None
                    await self._authenticate()
                    async with session.request(
                        method,
                        f"{self.url}/api2/json{path}",
                        headers=_headers(),
                        json=json_data,
                        ssl=self._ssl,
                    ) as resp2:
                        resp2.raise_for_status()
                        result = await resp2.json()
                        return result.get("data")
                resp.raise_for_status()
                result = await resp.json()
                return result.get("data")

    async def get_nodes(self) -> List[Dict[str, Any]]:
        return await self._request("GET", "/nodes")

    async def get_node_status(self, node: Optional[str] = None) -> Dict[str, Any]:
        return await self._request("GET", f"/nodes/{node or self.node}/status")

    async def list_lxc(self, node: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self._request("GET", f"/nodes/{node or self.node}/lxc")

    async def list_vms(self, node: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self._request("GET", f"/nodes/{node or self.node}/qemu")

    async def get_lxc_status(self, vmid: int, node: Optional[str] = None) -> Dict[str, Any]:
        return await self._request("GET", f"/nodes/{node or self.node}/lxc/{vmid}/status/current")

    async def get_vm_status(self, vmid: int, node: Optional[str] = None) -> Dict[str, Any]:
        return await self._request("GET", f"/nodes/{node or self.node}/qemu/{vmid}/status/current")

    async def lxc_action(self, vmid: int, action: str, node: Optional[str] = None) -> Any:
        return await self._request("POST", f"/nodes/{node or self.node}/lxc/{vmid}/status/{action}")

    async def vm_action(self, vmid: int, action: str, node: Optional[str] = None) -> Any:
        return await self._request("POST", f"/nodes/{node or self.node}/qemu/{vmid}/status/{action}")

    async def get_storage(self, node: Optional[str] = None) -> List[Dict[str, Any]]:
        return await self._request("GET", f"/nodes/{node or self.node}/storage")

    async def get_tasks(self, node: Optional[str] = None, limit: int = 20) -> List[Dict[str, Any]]:
        return await self._request("GET", f"/nodes/{node or self.node}/tasks?limit={limit}")
