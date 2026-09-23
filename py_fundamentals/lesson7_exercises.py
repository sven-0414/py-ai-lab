# # Sven Eriksson
# # Python och AI

# # Lab 7
# # Part A - Classes and objects
# # 1. Create a Book class with title, author and pages. Create at least four Book objects and print their
# # attributes.

# books = []


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages


# books.append(Book("Röde Orm", "Frans G. Bengtsson", 604))
# books.append(Book("Doktor Glas", "Hjalmar Söderberg", 168))
# books.append(Book("Kallocain", "Karin Boye", 240))
# books.append(Book("Låt den rätte komma in", "John Ajvide Lindqvist", 512))

# for book in books:
#     print(f"{book.title} av {book.author}, {book.pages} sidor")

# # 2. Create a Laptop class with brand, model, ram_gb and price. Create three separate objects and
# # change the price of one object.

# laptops = []


# class Laptop:
#     def __init__(self, brand, model, ram_gb, price):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# laptops.append(Laptop("Apple", "MacBook Air M3", 16, 15990))
# laptops.append(Laptop("Lenovo", "ThinkPad X1 Carbon", 32, 24500))
# laptops.append(Laptop("Dell", "XPS 13", 16, 18990))

# laptops[0].price += 1000

# for laptop in laptops:
#     print(f"{laptop.brand} av {laptop.model}, {laptop.ram_gb}, {laptop.price} kr.")


# # 3. Create two objects with the same attribute values. Use is to check whether they are the same object.
# laptop1 = Laptop("Apple", "MacBook Air M3", 16, 15990)
# laptop2 = Laptop("Apple", "MacBook Air M3", 16, 15990)

# print(laptop1 is laptop2)

# # 4. Add a default value to at least one __init__ parameter.
# class Laptop:
#     def __init__(self, brand: str, model: str, price: int, ram_gb: int = 16): # default RAM and type hints
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# # 5. Create one object using keyword arguments.
# class Laptop:
#     def __init__(self, brand: str, model: str, price: int, ram_gb: int = 16):
#         self.brand = brand
#         self.model = model
#         self.ram_gb = ram_gb
#         self.price = price


# leno_data = {"brand": "Lenovo", "model": "ThinkPad X1 Carbon Gen 12", "price": 24990}

# lenovo = Laptop(**leno_data)

# # Part B - Methods and state
# # 1. Extend your Book class with an is_long() method that returns True if the
# # book has more than 300 pages.
# books = []


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def is_long(self):
#         if self.pages > 300:
#             return True
#         else:
#             return False


# # 2. Create a BankAccount class with owner and balance. Add a deposit() method that changes the
# # balance.

# # 3. Add a withdraw() method. Prevent withdrawals that would make the balance negative by raising a
# # ValueError.


# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance += amount

#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         else:
#             self.balance -= amount


# # 4. Create a Task class with title and completed=False. Add complete() and reopen() methods.
# class Task:
#     def __init__(self, title: str, completed: bool = False):
#         self.title = title
#         self.completed = completed

#     def complete(self):
#         self.completed = True

#     def reopen(self):
#         self.completed = False


# # 5. Create at least two objects from one of your classes and show that changing the state of one object
# # does not change the other.
# task1 = Task("Write CV")
# task2 = Task("Apply for jobs")

# print(
#     f"Before: task1.completed = {task1.completed}, task2.completed = {task2.completed}"
# )

# task1.complete()

# print(
#     f"After: task1.completed = {task1.completed}, task2.completed = {task2.completed}"
# )

# # Part C - Instance and class attributes
# # 1. Create a Product class with name and price as instance attributes.
# # 2. Add a class attribute called tax_rate that is shared by all Product objects.
# # 3. Add a price_with_tax() method that returns the price including tax.
# # 4. Create at least three Product objects and print their prices with tax.
# # 5. Change Product.tax_rate and show how it affects the Product objects.
# # 6. Give one Product object its own tax_rate. Print the tax rate from that
# # object, another Product object and the Product class.


# class Product:
#     tax_rate: float = 0.25

#     def __init__(self, name: str, price: float):
#         self.name = name
#         self.price = price

#     def price_with_tax(self) -> float:
#         return self.price * (1 + self.tax_rate)


# coffee_maker = Product("Coffee maker", 799.00)
# toaster = Product("Toaster", 449.00)
# kettle = Product("Kettle", 349.00)

# for product in [coffee_maker, toaster, kettle]:
#     print(f"{product.name}: {product.price_with_tax():.2f} kr")

# Product.tax_rate = 0.12

# for product in [coffee_maker, toaster, kettle]:
#     print(f"{product.name}: {product.price_with_tax():.2f} kr")


# # Part D - Collections of objects
# # 1. Create at least six Student objects with name and score.
# # 2. Store all Student objects in a list.
# # 3. Loop through the list and print each student's name and score.
# # 4. Add a get_status() method that returns "PASS" or "FAIL" based on the score.
# # 5. Loop through the students again and print each student's name and status.
# # 6. Use a list comprehension to create a new list containing only students with a score of 70 or higher.
# class Student:
#     PASS_THRESHOLD = 50

#     def __init__(self, name: str, score: int):
#         self.name = name
#         self.score = score

#     def get_status(self) -> str:
#         return "PASS" if self.score >= self.PASS_THRESHOLD else "FAIL"


# students = [
#     Student("Alice", 85),
#     Student("Bob", 42),
#     Student("Charlie", 70),
#     Student("Diana", 91),
#     Student("Erik", 38),
#     Student("Fatima", 67),
# ]

# for student in students:
#     print(f"{student.name}: {student.score}")

# Part E - Objects inside objects
# 1. Create a Teacher class with a name.
# 2. Create a Course class with a course name and a teacher. The teacher should be a Teacher object.
# 3. Create a Teacher object and use it when creating a Course object.
# 4. Print the course name and the teacher's name through the Course object.
# 5. Extend Course so that it also contains an initially empty list of Student objects.
# 6. Add an add_student() method and use it to add at least three Student objects to the course.
# 7. Loop through course.students and print the name of every student.


class Teacher:
    def __init__(self, name: str):
        self.name = name


class Course:
    def __init__(self, course_name, teacher):
        self.course_name = course_name
        self.teacher = teacher
        self.students: list[Student] = []

    def add_student(self, student: "Student") -> None:
        self.students.append(student)


teacher = Teacher("Alladin")
course = Course("Introduction to Python", teacher)

print(f"Course: {course.course_name}")
print(f"Teacher: {course.teacher.name}")


class Student:
    PASS_THRESHOLD = 50

    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def get_status(self) -> str:
        return "PASS" if self.score >= self.PASS_THRESHOLD else "FAIL"


course.add_student(Student("Alice", 25))
course.add_student(Student("Bob", 42))
course.add_student(Student("Charlie", 70))

for student in course.students:
    print(student.name)

# Part F - Applied challenge: Course manager
# 1. Build a small course management program using Student, Teacher and Course classes.
# 2. Student should contain at least name and score.
# 3. Student should have a method that returns "PASS" or "FAIL".
# 4. Teacher should contain at least a name.
# 5. Course should contain a name, a Teacher object and a list of Student objects.
# 6. Add methods for adding a student and showing how many students are currently
#  in the course.
# 7. Add a method that returns a list containing only the students who passed.
# 8. Add validation somewhere in your program using ValueError. Choose a
# validation that makes sense.
# 9. Create at least five Student objects, one Teacher object and one Course
# object. Demonstrate that your methods work.
# 10. Print a simple course summary containing the course name, teacher name,
# number of students and the names of the students who passed.

# Part G - Stretch challenges
# 1. Add a method that updates a student's score with validation.
# 2. Add a method to Course that finds students above a score threshold.
# 3. Create another Course object and show that its student list is separate from the first course.
# 4. Add one useful class attribute to Student, Teacher or Course and explain in a comment why it belongs
# to the class rather than an individual object.
