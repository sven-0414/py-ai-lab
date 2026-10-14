from pymongo import MongoClient

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

products = db.products.find({"tags": "sport"}, {"name": 1, "tags": 1, "_id": 0})


for p in products:
    print(f"{p['name']}")
