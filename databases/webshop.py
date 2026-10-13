from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# for product in db.products.find({"category": "Accessories"}, {"name": 1, "_id": 0}):
#     print(product["name"])


# for c in db.customers.find({"city": "Göteborg"}, {"first_name": 1, "last_name": 1}):
#    print(c["first_name"], c["last_name"])

# for p in db.products.find():
#     print(p["name"], p["price"])


count = db.customers.count_documents({"city": "Uppsala"})
print(count)
