from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["webshop"]

# Design: a library app shows a book page with the book's title, author and all
# its reviews. Many members borrow the same book. Would you embed or reference
# the reviews? The members? Explain in two sentences.

# Reviews should be embeded in the book: they belong to the book, have no life
# of their own, and the book page needs to show them together.
# Members, reference, don’t embed: a member is independent and shared across
# many books, so embedding would duplicate the same person everywhere.
# Loans, give them an collection of their own. A many-to-many. You can query
#  from both the book and the member side and no array grows for ever.


# Our orders copy the product name into each item. Give one advantage and one
# disadvantage of that copy.

# Advantage: the order will refere to the product you odered even if it changes
# name later.
# Disadvantage: If you have to change the name fore some reason you will have
# to change it in many places.

# Create a collection newsletter_signups with validation: email is required and must be a string, and
# source can only be "web" or "store" (look up enum). Insert one valid and one invalid document.

# pipeline = [
#     {"$group": {"_id": "$city", "count": {"$sum": 1}}},
#     {"$sort": {"count": -1}},
# ]

# for rad in db.customers.aggregate(pipeline):
#     print(f"{rad['_id']}: {rad['count']}")


# pipeline = [
#     {
#         "$group": {
#             "_id": "$category",
#             "cheapest": {"$min": "$price"},
#             "most_expensive": {"$max": "$price"},
#         }
#     },
#     {"$sort": {"_id": 1}},
# ]

# for rad in db.products.aggregate(pipeline):
#     print(f"{rad['_id']}: {rad['cheapest']} – {rad['most_expensive']}")


# pipeline = [
#     {
#         "$group": {
#             "_id": "$category",
#             "cheapest": {"$min": "$price"},
#             "most_expensive": {"$max": "$price"},
#         }
#     },
#     {"$sort": {"_id": 1}},
# ]

# for rad in db.products.aggregate(pipeline):
#     print(f"{rad['_id']}: {rad['cheapest']} – {rad['most_expensive']}")

# pipeline = [
#     {"$group": {"_id": "$customer_id", "order_count": {"$sum": 1}}},
#     {"$match": {"order_count": {"$gte": 2}}},
#     {"$sort": {"order_count": -1}},
# ]

# for rad in db.orders.aggregate(pipeline):
#     print(f"Kund {rad['_id']}: {rad['order_count']} ordrar")

# pipeline = [
#     {"$match": {"status": {"$ne": "cancelled"}}},
#     {"$unwind": "$items"},
#     {
#         "$lookup": {
#             "from": "products",
#             "localField": "items.product_id",
#             "foreignField": "_id",
#             "as": "product",
#         }
#     },
#     {"$unwind": "$product"},
#     {"$group": {"_id": "$product.category", "units_sold": {"$sum": "$items.quantity"}}},
#     {"$sort": {"units_sold": -1}},
# ]

# for rad in db.orders.aggregate(pipeline):
#     print(f"{rad['_id']}: {rad['units_sold']} sålda")

# pipeline = [
#     {"$unwind": "$items"},
#     {
#         "$group": {
#             "_id": "$status",
#             "revenue": {
#                 "$sum": {"$multiply": ["$items.quantity", "$items.unit_price"]}
#             },
#         }
#     },
#     {"$sort": {"revenue": -1}},
# ]

# for rad in db.orders.aggregate(pipeline):
#     print(f"{rad['_id']}: {rad['revenue']} kr")

pipeline = [
    {"$unwind": "$tags"},
    {"$group": {"_id": "$tags", "antal": {"$sum": 1}}},
    {"$sort": {"antal": -1}},
]

for rad in db.products.aggregate(pipeline):
    print(f"{rad['_id']}: {rad['antal']}")
