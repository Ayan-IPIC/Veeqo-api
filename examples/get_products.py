from veeqo import VeeqoClient
import os

API_KEY = os.getenv("VEEQO_API_KEY", "****")

client = VeeqoClient(api_key=API_KEY)
products = client.list_products(page=1)
print(products)
