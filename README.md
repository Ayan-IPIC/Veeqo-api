# Veeqo API Client

This repository provides a minimal Python client for the [Veeqo API](https://developers.veeqo.com/api).
It exposes a `VeeqoClient` class that wraps HTTP requests and offers a few
convenience methods for common endpoints. Unsupported endpoints can be
accessed using the generic `request` method.

## Example

```python
from veeqo import VeeqoClient

client = VeeqoClient(api_key="YOUR_API_KEY")
products = client.list_products(limit=10)
print(products)
```
