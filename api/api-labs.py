from api_utils import get_json

# products = get_json(
#     "https://fakestoreapi.com/products", params=None, headers=None, timeout=5
# )

# # print(products[0])

# products = sorted(products, key=lambda p: p["price"])

# for p in products:
#     print(f"{p['title']}: {p['price']}")

# categories = get_json("https://fakestoreapi.com/products/categories")
# print(f"Categories: {categories}")
# choice = input("Choose a category: ").strip().lower()
# products = get_json(f"https://fakestoreapi.com/products/category/{choice}")

# lowest_price = products[0]["price"]
# lowest_product = products[0]["title"]
# counter = 0

# for p in products:
#     counter += 1
#     if lowest_price > p["price"]:
#         lowest_price = p["price"]
#         lowest_product = p["title"]

# print(f"{counter} products. {lowest_product} has the lowest price: {lowest_price} $.")
