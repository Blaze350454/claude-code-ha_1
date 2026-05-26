"""Proxmox VE MCP tools for managing VMs and containers."""

import sys
from typing import Any, Dict, List, Optional

from mcp_server.app import mcp_server
from mcp_server.config import PROXMOX_ENABLED
from mcp_server.proxmox_client import ProxmoxClient

proxmox_client: Optional[ProxmoxClient] = None

if PROXMOX_ENABLED:
    try:
        proxmox_client = ProxmoxClient()
        print("Proxmox integration enabled", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Failed to initialize Proxmox client: {e}", file=sys.stderr)
else:
    print("Proxmox integration disabled (missing PROXMOX_URL or PROXMOX_PASSWORD)", file=sys.stderr)


def _check_proxmox():
    if proxmox_client is None:
        raise RuntimeError(
            "Proxmox not configured. Set PROXMOX_URL, PROXMOX_USER, and PROXMOX_PASSWORD."
        )


@mcp_server.tool()
async def proxmox_list_containers() -> List[Dict[str, Any]]:
    """
    List all LXC containers on the Proxmox node with their status.

    Returns:
        List of containers with vmid, name, status, memory, cpu info.
    """
    _check_proxmox()
    containers = await proxmox_client.list_lxc()
    return sorted(containers or [], key=lambda x: x.get("vmid", 0))


@mcp_server.tool()
async def proxmox_list_vms() -> List[Dict[str, Any]]:
    """
    List all QEMU virtual machines on the Proxmox node with their status.

    Returns:
        List of VMs with vmid, name, status, memory, cpu info.
    """
    _check_proxmox()
    vms = await proxmox_client.list_vms()
    return sorted(vms or [], key=lambda x: x.get("vmid", 0))


@mcp_server.tool()
async def proxmox_node_status() -> Dict[str, Any]:
    """
    Get Proxmox node hardware and resource usage status.

    Returns:
        Node status including CPU usage, memory, uptime, kernel version.
    """
    _check_proxmox()
    return await proxmox_client.get_node_status()


@mcp_server.tool()
async def proxmox_container_status(vmid: int) -> Dict[str, Any]:
    """
    Get detailed status of a specific LXC container.

    Args:
        vmid: Container ID (e.g., 100 for esphome, 102 for mosquitto, 104 for vscode-server)

    Returns:
        Container status including state, cpu, memory, uptime.
    """
    _check_proxmox()
    return await proxmox_client.get_lxc_status(vmid)


@mcp_server.tool()
async def proxmox_vm_status(vmid: int) -> Dict[str, Any]:
    """
    Get detailed status of a specific QEMU VM.

    Args:
        vmid: VM ID (e.g., 101 for home-assistant)

    Returns:
        VM status including state, cpu, memory, uptime.
    """
    _check_proxmox()
    return await proxmox_client.get_vm_status(vmid)


@mcp_server.tool()
async def proxmox_container_action(vmid: int, action: str) -> Any:
    """
    Start, stop, reboot, or shutdown an LXC container.

    Args:
        vmid: Container ID
        action: One of 'start', 'stop', 'reboot', 'shutdown'

    Returns:
        Task ID for the action.
    """
    _check_proxmox()
    allowed = {"start", "stop", "reboot", "shutdown"}
    if action not in allowed:
        raise ValueError(f"action must be one of: {', '.join(sorted(allowed))}")
    return await proxmox_client.lxc_action(vmid, action)


@mcp_server.tool()
async def proxmox_vm_action(vmid: int, action: str) -> Any:
    """
    Start, stop, reboot, or shutdown a QEMU VM.

    Args:
        vmid: VM ID
        action: One of 'start', 'stop', 'reboot', 'shutdown', 'reset'

    Returns:
        Task ID for the action.
    """
    _check_proxmox()
    allowed = {"start", "stop", "reboot", "shutdown", "reset"}
    if action not in allowed:
        raise ValueError(f"action must be one of: {', '.join(sorted(allowed))}")
    return await proxmox_client.vm_action(vmid, action)


@mcp_server.tool()
async def proxmox_storage_status() -> List[Dict[str, Any]]:
    """
    Get storage pool usage on the Proxmox node.

    Returns:
        List of storage pools with type, total, used, available space.
    """
    _check_proxmox()
    return await proxmox_client.get_storage()


@mcp_server.tool()
async def proxmox_recent_tasks(limit: int = 20) -> List[Dict[str, Any]]:
    """
    Get recent tasks/jobs from the Proxmox task log.

    Args:
        limit: Number of recent tasks to return (default 20)

    Returns:
        List of recent tasks with type, status, start time, node.
    """
    _check_proxmox()
    return await proxmox_client.get_tasks(limit=limit)
