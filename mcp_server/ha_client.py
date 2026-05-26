"""Home Assistant API client for MCP server integration."""

import os
import sys
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import aiohttp


class HomeAssistantClient:
    """Async client for Home Assistant REST API."""

    def __init__(self, url: Optional[str] = None, token: Optional[str] = None):
        """
        Initialize the Home Assistant client.

        Args:
            url: Home Assistant URL (e.g., http://192.168.1.100:8123).
                 If not provided, reads from HA_URL environment variable.
            token: Long-lived access token for authentication.
                   If not provided, reads from HA_TOKEN environment variable.
        """
        self.url = url or os.getenv("HA_URL")
        self.token = token or os.getenv("HA_TOKEN")

        if not self.url:
            raise ValueError(
                "Home Assistant URL not provided. Set HA_URL environment variable "
                "or pass url parameter."
            )
        if not self.token:
            raise ValueError(
                "Home Assistant token not provided. Set HA_TOKEN environment variable "
                "or pass token parameter."
            )

        # Ensure URL doesn't have trailing slash
        self.url = self.url.rstrip("/")

        # Headers for API requests
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json",
        }

        print(f"HomeAssistantClient initialized for {self.url}", file=sys.stderr)

    async def _request(
        self,
        method: str,
        endpoint: str,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Any:
        """
        Make an async HTTP request to Home Assistant API.

        Args:
            method: HTTP method (GET, POST, etc.)
            endpoint: API endpoint path (e.g., /api/states)
            json_data: Optional JSON payload for POST requests

        Returns:
            Parsed JSON response

        Raises:
            aiohttp.ClientError: On HTTP errors
        """
        url = urljoin(self.url, endpoint)

        async with aiohttp.ClientSession() as session:
            async with session.request(
                method, url, headers=self.headers, json=json_data
            ) as response:
                response.raise_for_status()
                return await response.json()

    async def get_states(self, entity_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """
        Get entity states from Home Assistant.

        Args:
            entity_id: Optional specific entity ID. If None, returns all entities.

        Returns:
            List of entity state dictionaries or single entity dict if entity_id provided.
        """
        if entity_id:
            endpoint = f"/api/states/{entity_id}"
            result = await self._request("GET", endpoint)
            return [result]  # Wrap single entity in list for consistency
        else:
            endpoint = "/api/states"
            return await self._request("GET", endpoint)

    async def call_service(
        self, domain: str, service: str, service_data: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Call a Home Assistant service.

        Args:
            domain: Service domain (e.g., 'light', 'switch', 'automation')
            service: Service name (e.g., 'turn_on', 'turn_off', 'trigger')
            service_data: Optional service data (e.g., {'entity_id': 'light.bedroom'})

        Returns:
            List of affected entity states
        """
        endpoint = f"/api/services/{domain}/{service}"
        return await self._request("POST", endpoint, json_data=service_data or {})

    async def get_config(self) -> Dict[str, Any]:
        """
        Get Home Assistant configuration.

        Returns:
            Configuration dictionary with version, location, etc.
        """
        endpoint = "/api/config"
        return await self._request("GET", endpoint)

    async def get_services(self) -> List[Dict[str, Any]]:
        """
        Get all available services in Home Assistant.

        Returns:
            List of service definitions grouped by domain
        """
        endpoint = "/api/services"
        return await self._request("GET", endpoint)

    async def get_error_log(self) -> str:
        """
        Get Home Assistant error log.

        Returns:
            Error log as string
        """
        endpoint = "/api/error_log"
        async with aiohttp.ClientSession() as session:
            async with session.get(
                urljoin(self.url, endpoint), headers=self.headers
            ) as response:
                response.raise_for_status()
                return await response.text()

    async def fire_event(
        self, event_type: str, event_data: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Fire an event on the Home Assistant event bus.

        Args:
            event_type: Type of event to fire
            event_data: Optional event data

        Returns:
            Success message
        """
        endpoint = f"/api/events/{event_type}"
        return await self._request("POST", endpoint, json_data=event_data or {})

    async def check_api(self) -> Dict[str, str]:
        """
        Check API availability and return basic info.

        Returns:
            Dict with 'message' key indicating API status
        """
        endpoint = "/api/"
        return await self._request("GET", endpoint)
