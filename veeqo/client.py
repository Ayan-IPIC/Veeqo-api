import requests
from typing import Any, Dict, Optional


class VeeqoClient:
    """Minimal Veeqo API client.

    This client provides generic request helpers and a few example
    endpoint wrappers. The full Veeqo API includes many resources which
    are not implemented here. For unsupported endpoints use the generic
    ``request`` method.
    """

    def __init__(self, api_key: str, base_url: str = "https://api.veeqo.com") -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"})

    def request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> requests.Response:
        """Make a request to the Veeqo API.

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
        response = self.session.request(method, url, params=params, json=json)
        response.raise_for_status()
        return response

    # Example convenience wrappers -----------------------------------------
    def list_products(self, **params: Any) -> Dict[str, Any]:
        """Return a list of products."""
        resp = self.request("GET", "/products", params=params)
        return resp.json()

    def get_order(self, order_id: int) -> Dict[str, Any]:
        """Retrieve a single order by ID."""
        resp = self.request("GET", f"/orders/{order_id}")
        return resp.json()

    def create_order(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new order with the provided data."""
        resp = self.request("POST", "/orders", json=data)
        return resp.json()

    def update_order(self, order_id: int, data: Dict[str, Any]) -> Dict[str, Any]:
        """Update an existing order."""
        resp = self.request("PUT", f"/orders/{order_id}", json=data)
        return resp.json()

    def delete_order(self, order_id: int) -> None:
        """Delete an order."""
        self.request("DELETE", f"/orders/{order_id}")
