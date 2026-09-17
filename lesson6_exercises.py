# Sven Eriksson
# Kurs: Python & ai
# Lab 6

# Part A – List comprehensions
# Create squares for numbers 1–20 using a normal loop, then a list comprehension.
numbers = [n for n in range(1, 21)]
print(numbers)

# Create a list containing only even numbers from 1–100.
numbers = [n for n in range(2, 101, 2)]
print(numbers)

# Convert a list of names to stripped, title-cased names.
players = [
    "  daniel MUZITO-bagenda  ",
    "MELKER ljunggren   ",
    "   anton bengtsson",
    "  LUDVIG nilsson  ",
    "oskar LINDGREN   ",
]

players = [player.strip().title() for player in players]
print(players)

# Given scores, create a list containing only passing scores.
scores = [17, 25, 62, 55, 47]
passing = []

for score in scores:
    if score > 45:
        passing.append(score)

print(passing)

# Create labels such as 'PASS'/'FAIL' for every score using a conditional expression in a comprehension.
# Rewrite three earlier loop-based transformations from Lessons 2–4 as comprehensions.

# Part B – Dictionary and set comprehensions
# Create a dictionary mapping numbers 1–10 to their squares.
numbers = [n for n in range(1, 11)]
squares = {number: number**2 for number in numbers}


# Given a list of words, create a dictionary mapping each word to its length.
words = ["cat", "piano", "elephant", "hi", "refrigerator"]

mapped_words = {len(word): word for word in words}

# Given a list with duplicates, create a set comprehension containing lowercase normalized values.
words = [
    "  Apple",
    "banana  ",
    "  cherry  ",
    "apple",
    "date",
    "  banaNa",
    "elderberry  ",
    "Cherry",
]

unique_words = {word.strip().lower() for word in words}
print(unique_words)

# Create a dictionary of only products whose price is below a chosen threshold.
# Create a dictionary mapping student names to PASS/FAIL from a list of student dictionaries.
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 72},
    {"name": "Charlie", "age": 19, "grade": 91},
    {"name": "Diana", "age": 21, "grade": 68},
    {"name": "Ethan", "age": 23, "grade": 77},
]

passed = {
    student["name"]: "PASS" if student["grade"] >= 70 else "FAIL"
    for student in students
}
print(passed)

# Part C – enumerate
# Print a playlist with numbering starting at 1 using enumerate.
songs = [
    "Bohemian Rhapsody",
    "Imagine",
    "Hotel California",
    "Smells Like Teen Spirit",
    "Billie Jean",
    "Hey Jude",
    "Stairway to Heaven",
    "Wonderwall",
    "Losing My Religion",
    "Sweet Child O' Mine",
]

for index, song in enumerate(songs, start=1):
    print(f"{index}. {song}")

# Given a list of tasks, print 'Task 1:', 'Task 2:' etc.
tasks = [
    "Write project report",
    "Reply to client emails",
    "Fix login bug",
    "Prepare presentation slides",
    "Review pull requests",
]

for index, task in enumerate(tasks, start=1):
    print(f"Task {index}: {task}")


# Find and print indexes of all values above a threshold.
# Rewrite a range(len(…)) loop using enumerate and explain why the new version is clearer.

# Part D – zip and unpacking
# Combine separate name and score lists using zip and print each pair.
names = ["Alice", "Bob", "Charlie", "Diana", "Ethan"]
scores = [85, 72, 91, 68, 77]

for name, score in zip(names, scores):
    print(name, score)

# Create a dictionary using dict(zip(keys, values)).
keys = ["name", "age", "city", "job", "email"]
values = ["Alice", 30, "Göteborg", "developer", "alice@example.com"]

dict = {key: value for key, value in zip(keys, values)}
print(dict)

# Combine three lists: product name, price and stock.
# Investigate what happens when zipped lists have different lengths.
# Use tuple unpacking directly in a for loop over zipped data.
products = ["bread", "milk", "coffee", "cheese", "apple"]
prices = [32, 18, 89, 75, 12]
stocks = [15, 40, 8, 12, 60, 20]

for product, price, stock in zip(products, prices, stocks):
    print(product, price, stock)
# Swap two variables without a temporary variable.

a = 1
b = 2
a, b = b, a
print(a, b)

# Part E – sorted and lambda
# Sort a list of words by length using sorted(…, key=…).
words = ["cat", "piano", "elephant", "hi", "refrigerator"]

print(sorted(words, key=lambda w: len(w)))

# Sort a list of student dictionaries by score ascending and descending.
students = [
    {"name": "Alice", "age": 20, "grade": 85},
    {"name": "Bob", "age": 22, "grade": 72},
    {"name": "Charlie", "age": 19, "grade": 91},
    {"name": "Diana", "age": 21, "grade": 68},
    {"name": "Ethan", "age": 23, "grade": 77},
]

print(sorted(students, key=lambda s: s["grade"]))
print(sorted(students, key=lambda s: s["grade"], reverse=True))

# Sort products by price using a lambda.
products = ["bread", "milk", "coffee", "cheese", "apple"]
prices = [32, 18, 89, 75, 12]

print(sorted(zip(products, prices), key=lambda p: p[1]))

# Sort people by last name when each item is a dictionary containing first_name and last_name.
people = [
    {"first_name": "Alice", "last_name": "Johnson"},
    {"first_name": "Bob", "last_name": "Andersson"},
    {"first_name": "Charlie", "last_name": "Nguyen"},
    {"first_name": "Diana", "last_name": "Bergström"},
    {"first_name": "Ethan", "last_name": "Okafor"},
]

print(sorted(people, key=lambda p: p["last_name"]))

# Write a normal named function for a sort key, then replace it with lambda. Compare when each is clearer.


def get_lastname(people):
    return people["last_name"]


print(sorted(people, key=get_lastname))


# Part F – Applied challenge: Data cleanup
# Start with a list of at least twelve messy dictionaries representing products: inconsistent name casing/spacing, category, price and stock.
# Create a cleaned list where names/categories are normalized. Use comprehensions where readable.
# Create a list of in-stock products.
# Create a set of unique normalized categories.
# Create a dictionary mapping product name to inventory value (price * stock).
# Sort products by inventory value from highest to lowest.
# Use enumerate to print a ranked report.
# Use zip to combine at least one pair of separate derived lists in a meaningful way.
# Write both a deliberately över-complicated comprehension and a clearer alternative. Explain why the clearer version wins.

# Part G – Stretch challenges
# Flatten a simple list of lists using a comprehension.
# Create a multiplication table structure using a nested comprehension, then decide whether the result is readable enough.
# Given names and scores, create only passing student dictionaries in one readable comprehension.
# Use any() and all() to answer useful questions about a score list, after first solving them with loops.
# Create five examples where Pythonic syntax reduces boilerplate without reducing clarity.
