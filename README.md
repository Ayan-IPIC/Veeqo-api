# Veeqo API Client

This repository provides a minimal Python client for the [Veeqo API](https://developers.veeqo.com/api).
It exposes a `VeeqoClient` class that wraps HTTP requests and offers a few
convenience methods for common endpoints. Unsupported endpoints can be
accessed using the generic `request` method.

**Note:** The development environment used for this repository does not have
internet access. The client and example code can be executed, but real API
requests will fail. Use this project for offline development or adapt it for
your own environment.

## Example

```python
from veeqo import VeeqoClient

# Provide one or more API keys. Multiple keys will be cycled between
# successive requests.
client = VeeqoClient(api_keys=["YOUR_API_KEY"])
products = client.list_products(page=1)
print(products)
```

You can also run the example script in ``examples/get_products.py``. Set the
``VEEQO_API_KEYS`` environment variable if you don't want to edit the file:

```bash
export VEEQO_API_KEYS=YOUR_API_KEY
python examples/get_products.py
```
