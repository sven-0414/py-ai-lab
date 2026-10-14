from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]


db.products.find({ price: { $gt: 1000 } }, { name: 1, price: 1, _id: 0 })