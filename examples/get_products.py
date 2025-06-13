from veeqo import VeeqoClient
import os

API_KEY = os.getenv("VEEQO_API_KEY", "Vqt/800967642dae577f3ed97a48ca8f9ff0")

client = VeeqoClient(api_key=API_KEY)
products = client.list_products(page=1)
print(products)
