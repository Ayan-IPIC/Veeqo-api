from veeqo import VeeqoClient
import os

# Comma-separated list of API keys. Only structure is demonstrated here.
API_KEYS = os.getenv(
    "VEEQO_API_KEYS",
    "Vqt/800967642dae577f3ed97a48ca8f9ff0",
).split(",")

client = VeeqoClient(api_keys=API_KEYS)
products = client.list_products(page=1)
print(products)
