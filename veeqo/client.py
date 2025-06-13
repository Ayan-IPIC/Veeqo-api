"""Minimal HTTP client for Veeqo API without external dependencies."""

import json
import urllib.error
import urllib.parse
import urllib.request
from typing import Any, Dict, Optional


class VeeqoClient:
    """Minimal Veeqo API client.

    This implementation avoids third party dependencies so it can run in
    restricted environments. Unsupported endpoints can be accessed using
    the generic :py:meth:`request` method.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.veeqo.com") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        }

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json_data: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """Make a request to the Veeqo API and return the parsed JSON response.

        Parameters
        ----------
        method:
            HTTP method (``'GET'``, ``'POST'``, etc).
        path:
            API path starting with ``/``.
        params:
            Query parameters for the request.
        json:
            JSON body to send with the request (for ``POST``/``PUT``/``PATCH``).
        """
        url = f"{self.base_url}{path}"
        if params:
            url = f"{url}?{urllib.parse.urlencode(params)}"

        data = None
        if json_data is not None:
            data = json.dumps(json_data).encode()

        req = urllib.request.Request(url, data=data, headers=self.headers, method=method)
        try:
            with urllib.request.urlopen(req) as resp:
                body = resp.read()
        except urllib.error.HTTPError as exc:
            error_content = exc.read().decode()
            raise RuntimeError(f"{exc.code} {exc.reason}: {error_content}") from exc

        return json.loads(body)

    # Example convenience wrappers -----------------------------------------
    def list_products(self, **params: Any) -> Dict[str, Any]:
        """Return a list of products."""
        return self.request("GET", "/products", params=params)

    def get_order(self, order_id: int) -> Dict[str, Any]:
        """Retrieve a single order by ID."""
        return self.request("GET", f"/orders/{order_id}")

    def create_order(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new order with the provided data."""
        return self.request("POST", "/orders", json_data=data)

    def update_order(self, order_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing order."""
        return self.request("PUT", f"/orders/{order_id}", json_data=data)

    def delete_order(self, order_id: int) -> None:
        """Delete an order."""
        self.request("DELETE", f"/orders/{order_id}")
