from pymongo import MongoClient
from pprint import pprint

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


# count = db.customers.count_documents({"city": "Uppsala"})
# print(count)


# product = db.products.find_one({"name": "Sandals"})
# print(product["stock"])


# for c in db.customers.find({"newsletter": True}, {"first_name": 1}):
#     print(c["first_name"])


# result = db.customers.insert_one(
#     {
#         "first_name": "Sven",
#         "last_name": "Eriksson",
#         "email": "svenpleriksson@example.com",
#         "city": "Göteborg",
#     }
# )
# print(result.inserted_id)


# result = db.products.insert_many(
#     [
#         {
#             "_id": "13",
#             "name": "Long Johns",
#             "category": "Underwear",
#             "stock": 125,
#             "price": 199,
#             "tags": ["winter"],
#             "details": {"material": "wool"},
#         },
#         {
#             "_id": "14",
#             "name": "Fleece Jacket",
#             "category": "Clothing",
#             "stock": 40,
#             "price": 699,
#             "tags": ["winter", "fleece"],
#             "details": {"color": "navy", "material": "polyester"},
#         },
#     ]
# )

# print(db.products.count_documents({}))
