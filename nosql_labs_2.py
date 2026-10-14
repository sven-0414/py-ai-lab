from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


# products = db.products.find({"price": {"$gt": 1000}}, {"name": 1, "price": 1, "_id": 0})

# for p in products:
#     print(f"{p['name']}")

# not_delivered = db.orders.find({"status": {"$ne": "delivered"}}, {"status": 1})

# for o in not_delivered:
#     print(f"{o['_id']} {o['status']}")
