from pymongo import MongoClient
from datetime import datetime

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# products = db.products.find({"price": {"$gt": 1000}}, {"name": 1, "price": 1, "_id": 0})

# for p in products:
#     print(f"{p['name']}")

# not_delivered = db.orders.find({"status": {"$ne": "delivered"}}, {"status": 1})

# for o in not_delivered:
#     print(f"{o['_id']} {o['status']}")

# customers_in_wrong_city = db.customers.find({"city": {"$in": ["Stockholm", "Malmö"]}})

# for c in customers_in_wrong_city:
#     print(f"{c['first_name']} {c['city']}")

# white_products = db.products.find({"details.color": "white"})

# for w in white_products:
#     print(f"{w['name']} {w['details']['color']}")

# products = db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0})


# for p in products:
#     print(f"{p['name']}")


# cheapest = (
#     db.products.find({}, {"name": 1, "price": 1, "_id": 0}).sort("price", 1).limit(5)
# )

# for p in cheapest:
#     print(f"{p['name']} {p['price']}")


# for o in db.orders.find({"items.product_id": 2}):
#     print(o)


# db.products.update_many({"category": "Accessories"}, {"$inc": {"price": 20}})

# for p in db.products.find(
#     {"category": "Accessories"}, {"name": 1, "price": 1, "_id": 0}
# ):
#     print(f"{p['name']} {p['price']}")


# filter = {"category": "Accessories"}

# print("Innan:")
# for p in db.products.find(filter, {"name": 1, "price": 1, "_id": 0}):
#     print(f"  {p['name']} {p['price']}")

# if input("Höj dessa med 20 kr? (j/n): ") == "j":
#     result = db.products.update_many(filter, {"$inc": {"price": 20}})
#     print(f"{result.modified_count} produkter uppdaterade.")

#     print("Efter:")
#     for p in db.products.find(filter, {"name": 1, "price": 1, "_id": 0}):
#         print(f"  {p['name']} {p['price']}")
# else:
#     print("Avbröt, inget ändrat.")


# db.products.update_one(
#     {"name": "Rain Jacket"},
#     {"$addToSet": {"tags": "new"}, "$set": {"restock_date": datetime.now()}},
# )

# for p in db.products.find(
#     {"name": "Rain Jacket"}, {"name": 1, "tags": 1, "restock_date": 1, "_id": 0}
# ):
#     print(p)


query = {"status": "new", "order_date": {"$lt": datetime(2026, 3, 20)}}

# 1. Räkna först
antal = db.orders.count_documents(query)
print(f"Matchar: {antal} ordrar")

# 2. Fråga innan radering
if input(f"Radera dessa {antal} ordrar? (j/n): ") == "j":
    result = db.orders.delete_many(query)
    print(f"{result.deleted_count} ordrar raderade.")
else:
    print("Avbröt, inget raderat.")
