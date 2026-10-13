from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

for product in db.products.find({"category": "Accessories"}, {"name": 1, "_id": 0}):
    print(product["name"])
