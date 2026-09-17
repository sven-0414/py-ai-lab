# ==================================================
# TASK 1
# ==================================================

products = [
    {"name": "Laptop", "price": 12000, "stock": 4},
    {"name": "Mouse", "price": 350, "stock": 0},
    {"name": "Keyboard", "price": 800, "stock": 6},
    {"name": "Monitor", "price": 3200, "stock": 3},
    {"name": "Headset", "price": 950, "stock": 0},
    {"name": "Webcam", "price": 1100, "stock": 5},
]

# 1. Loop through the products.
# 2. Print the name of every product that is in stock.
# 3. Calculate the total value of all products in stock.
#    The value of a product is price * stock.
# 4. Print the total value.
# 5. Keep track of which in-stock product has the highest price
#    without using max(), and print its name.


# Write your solution below:
total_value = 0
max_value = 0
max_name = ""

for product in products:
    if product["price"] > max_value:
        max_value = product["price"]
        max_name = product["name"]
    if product["stock"] > 0:
        print(product["name"])
        total_value += product["price"] * product["stock"]


print(
    f"Total value of products: {total_value}\nProduct with highest price: {max_name}.\n\n"
)


# ==================================================
# TASK 2
# ==================================================

scores = [78, 92, 55, 81, 67, 95, 73]

# Create a function called calculate_average that:
# - receives a list of scores
# - calculates and returns the average score
#
# Create another function called create_result that:
# - receives a list of scores
# - uses calculate_average()
# - returns "PASS" if the average is 70 or higher
# - otherwise returns "FAIL"
#
# Call create_result() using the scores above.
# Print both the average score and the final result.


# Write your solution below:
def calculate_average(numbers: list):
    return sum(numbers) / len(numbers)


def create_result(numbers: list):
    average = calculate_average(numbers)
    if average >= 70:
        return "PASS"
    else:
        return "FAIL"


print(
    f"Average score: {calculate_average(scores)}\nResult: {create_result(scores)}\n\n"
)


# ==================================================
# TASK 3
# ==================================================

product_prices = [250, 400, 150, 700]

order_settings = {"discount": 10, "shipping": 49, "priority": True}

# Create a function called calculate_order that:
# - receives a customer name as a normal parameter
# - receives any number of product prices using *args
# - receives optional settings using **kwargs
# - calculates the subtotal of all product prices
# - applies the discount percentage if "discount" exists
# - adds shipping if "shipping" exists
# - returns a dictionary containing:
#       customer
#       subtotal
#       final_total
#       settings
#
# Call the function using:
# - customer name "Anna"
# - the values from product_prices using unpacking
# - the values from order_settings using dictionary unpacking
#
# Print the returned dictionary.


# Write your solution below:
def calculate_order(name, *args, **kwargs):
    sub_total = sum(args)
    if kwargs["discount"] > 0:
        discount = sub_total * kwargs["discount"] / 100
    else:
        discount = 0
    if kwargs["shipping"] > 0:
        shipping = kwargs["shipping"]
    else:
        shipping = 0

    return {
        "customer": name,
        "subtotal": sub_total,
        "final_total": sub_total + shipping - discount,
        "settings": kwargs,
    }


print(calculate_order("Anna", *product_prices, **order_settings))

# ==================================================
# TASK 4
# ==================================================

players = [
    {"name": "  anna", "score": 85, "active": True},
    {"name": "DAVID ", "score": 72, "active": False},
    {"name": " sara ", "score": 94, "active": True},
    {"name": "LEO", "score": 67, "active": True},
    {"name": " emma", "score": 88, "active": True},
    {"name": "OSCAR ", "score": 76, "active": False},
]

# 1. Create a new list containing normalized player names.
#    Remove unnecessary whitespace and use consistent capitalization.
#    Use a list comprehension.
#
# 2. Create a new list containing only the active players
#    with a score of 80 or higher.
#    Use a list comprehension.
#
# 3. Sort the original players by score from highest to lowest.
#    Use sorted() with a lambda.
#
# 4. Print the ranking in the following format:
#
#    1. Sara - 94
#    2. Emma - 88
#    ...
#
#    Generate the ranking numbers using enumerate().
#
# 5. Create a separate list containing the player names and
#    another list containing their scores.
#    Combine them using zip() and print each name together
#    with its score.


# Write your solution below:
new_list = [player["name"].strip().capitalize() for player in players]

active_players = [
    player["name"] for player in players if player["active"] and player["score"] > 80
]

# # I have not done the last lab yet and therefor can not to the lamba and zip tasks.
