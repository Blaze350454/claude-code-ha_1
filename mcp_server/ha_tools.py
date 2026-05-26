"""Home Assistant MCP tools for controlling and querying HA instance."""

import sys
from typing import Any, Dict, List, Optional

from mcp_server.app import mcp_server
from mcp_server.config import HA_ENABLED
from mcp_server.ha_client import HomeAssistantClient

# Initialize HA client if credentials are available
ha_client: Optional[HomeAssistantClient] = None

if HA_ENABLED:
    try:
        ha_client = HomeAssistantClient()
        print("Home Assistant integration enabled", file=sys.stderr)
    except Exception as e:
        print(f"Warning: Failed to initialize HA client: {e}", file=sys.stderr)
        ha_client = None
else:
    print(
        "Home Assistant integration disabled (missing HA_URL or HA_TOKEN)",
        file=sys.stderr,
    )


def _check_ha_available():
    """Check if HA client is available, raise error if not."""
    if ha_client is None:
        raise RuntimeError(
            "Home Assistant integration not configured. "
            "Please set HA_URL and HA_TOKEN environment variables."
        )


# --- Home Assistant Tools ---


@mcp_server.tool()
async def ha_get_states(entity_id: str = "") -> List[Dict[str, Any]]:
    """
    Get entity states from Home Assistant.

    Args:
        entity_id: Optional specific entity ID (e.g., 'light.bedroom').
                   If empty, returns all entities.

    Returns:
        List of entity state dictionaries containing:
        - entity_id: The entity identifier
        - state: Current state value
        - attributes: Dictionary of entity attributes
        - last_changed: ISO timestamp of last state change
        - last_updated: ISO timestamp of last update
    """
    _check_ha_available()
    return await ha_client.get_states(entity_id if entity_id else None)


@mcp_server.tool()
async def ha_call_service(
    domain: str, service: str, entity_id: str = "", service_data: str = "{}"
) -> List[Dict[str, Any]]:
    """
    Call a Home Assistant service.

    Args:
        domain: Service domain (e.g., 'light', 'switch', 'automation', 'script')
        service: Service name (e.g., 'turn_on', 'turn_off', 'toggle', 'trigger')
        entity_id: Optional entity ID to target (e.g., 'light.bedroom')
        service_data: Optional JSON string with additional service data
                      (e.g., '{"brightness": 255, "color_name": "red"}')

    Returns:
        List of affected entity states after service call

    Examples:
        - Turn on a light: domain='light', service='turn_on', entity_id='light.bedroom'
        - Set brightness: domain='light', service='turn_on', entity_id='light.bedroom',
                         service_data='{"brightness": 128}'
        - Trigger automation: domain='automation', service='trigger',
                             entity_id='automation.motion_light'
    """
    _check_ha_available()

    import json

    # Parse service_data JSON string
    try:
        data = json.loads(service_data) if service_data else {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid service_data JSON: {e}")

    # Add entity_id to service data if provided
    if entity_id:
        data["entity_id"] = entity_id

    return await ha_client.call_service(domain, service, data)


@mcp_server.tool()
async def ha_get_config() -> Dict[str, Any]:
    """
    Get Home Assistant configuration information.

    Returns:
        Configuration dictionary containing:
        - version: Home Assistant version
        - location_name: Configured location name
        - latitude/longitude: Geographic coordinates
        - time_zone: Time zone setting
        - unit_system: Unit system (metric/imperial)
        - components: List of loaded components/integrations
    """
    _check_ha_available()
    return await ha_client.get_config()


@mcp_server.tool()
async def ha_get_services() -> List[Dict[str, Any]]:
    """
    Get all available services in Home Assistant.

    Returns:
        List of service definitions grouped by domain, each containing:
        - domain: Service domain name
        - services: Dictionary of available services in that domain
    """
    _check_ha_available()
    return await ha_client.get_services()


@mcp_server.tool()
async def ha_list_entities(domain: str = "") -> List[str]:
    """
    List all entity IDs, optionally filtered by domain.

    Args:
        domain: Optional domain filter (e.g., 'light', 'switch', 'sensor', 'binary_sensor')
                If empty, returns all entity IDs.

    Returns:
        List of entity IDs

    Examples:
        - List all lights: domain='light'
        - List all switches: domain='switch'
        - List everything: domain='' (empty)
    """
    _check_ha_available()
    states = await ha_client.get_states()

    if domain:
        # Filter by domain prefix
        entity_ids = [
            state["entity_id"]
            for state in states
            if state["entity_id"].startswith(f"{domain}.")
        ]
    else:
        entity_ids = [state["entity_id"] for state in states]

    return sorted(entity_ids)


@mcp_server.tool()
async def ha_get_entity_state(entity_id: str) -> Dict[str, Any]:
    """
    Get detailed state and attributes for a specific entity.

    Args:
        entity_id: The entity ID (e.g., 'light.bedroom', 'sensor.temperature')

    Returns:
        Entity state dictionary containing:
        - entity_id: The entity identifier
        - state: Current state value
        - attributes: Full dictionary of entity attributes
        - last_changed: When the state last changed
        - last_updated: When the entity was last updated
        - context: Context information about the last state change
    """
    _check_ha_available()
    states = await ha_client.get_states(entity_id)
    if not states:
        raise ValueError(f"Entity not found: {entity_id}")
    return states[0]


@mcp_server.tool()
async def ha_fire_event(event_type: str, event_data: str = "{}") -> Dict[str, Any]:
    """
    Fire an event on the Home Assistant event bus.

    Args:
        event_type: Type of event to fire (e.g., 'custom_event')
        event_data: Optional JSON string with event data

    Returns:
        Success message

    Note: This is an advanced feature. Most users should use ha_call_service instead.
    """
    _check_ha_available()

    import json

    try:
        data = json.loads(event_data) if event_data else {}
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid event_data JSON: {e}")

    return await ha_client.fire_event(event_type, data)


@mcp_server.tool()
async def ha_check_connection() -> Dict[str, Any]:
    """
    Check if the Home Assistant API is accessible.

    Returns:
        Dictionary with connection status and basic API info
    """
    _check_ha_available()
    try:
        api_status = await ha_client.check_api()
        config = await ha_client.get_config()
        return {
            "status": "connected",
            "api_message": api_status.get("message", ""),
            "version": config.get("version", "unknown"),
            "location": config.get("location_name", "unknown"),
            "url": ha_client.url,
        }
    except Exception as e:
        return {
            "status": "error",
            "error": str(e),
            "url": ha_client.url,
        }


# Tools are automatically registered via @mcp_server.tool() decorator
# No manual registration needed
