from api_utils import get_json

products = get_json(
    "https://fakestoreapi.com/products", params=None, headers=None, timeout=5
)

# print(products[0])

products = sorted(products, key=lambda p: p["price"])

for p in products:
    print(f"{p['title']}: {p['price']}")
