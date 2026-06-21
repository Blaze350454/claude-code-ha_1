from typing import Dict, List

from esphome_mcp.app import mcp_server
from esphome_mcp import dashboard_client


@mcp_server.tool()
def esphome_list_configs() -> List[str]:
    """List all ESPHome device configuration files on the dashboard."""
    return dashboard_client.list_configs()


@mcp_server.tool()
def esphome_read_config(configuration: str) -> str:
    """Read the YAML content of an ESPHome configuration file.

    Args:
        configuration: Filename, e.g. 'tent-irrigation-controller.yaml'
    """
    return dashboard_client.read_config(configuration)


@mcp_server.tool()
def esphome_write_config(configuration: str, content: str) -> Dict[str, str]:
    """Write/update an ESPHome YAML config. Creates the file if it doesn't exist.

    Args:
        configuration: Filename, e.g. 'tent-irrigation-controller.yaml'
        content: Full YAML content to write
    """
    return dashboard_client.write_config(configuration, content)


@mcp_server.tool()
def esphome_validate(configuration: str) -> str:
    """Validate an ESPHome configuration and return the output.

    Args:
        configuration: Filename, e.g. 'tent-irrigation-controller.yaml'
    """
    return dashboard_client.run_dashboard_operation("validate", configuration, timeout=60)


@mcp_server.tool()
def esphome_compile(configuration: str) -> str:
    """Compile ESPHome firmware and return the build output. May take several minutes.

    Args:
        configuration: Filename, e.g. 'tent-irrigation-controller.yaml'
    """
    return dashboard_client.run_dashboard_operation("compile", configuration, timeout=600)
