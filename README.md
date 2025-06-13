# Veeqo API Client

This repository provides a minimal Python client for the [Veeqo API](https://developers.veeqo.com/api).
It exposes a `VeeqoClient` class that wraps HTTP requests and offers a few
convenience methods for common endpoints. Unsupported endpoints can be
accessed using the generic `request` method.

## Example

```python
from veeqo import VeeqoClient

client = VeeqoClient(api_key="YOUR_API_KEY")
products = client.list_products(page=1)
print(products)
```

You can also run the example script in ``examples/get_products.py``. Set the
``VEEQO_API_KEY`` environment variable if you don't want to edit the file:

```bash
export VEEQO_API_KEY=YOUR_API_KEY
python examples/get_products.py
```
