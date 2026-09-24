# # Part A - Mutable default arguments
# # 1. Create a BadTeam class with name and a default parameter members=[]. Add an add_member()
# # method.
# # 2. Create two BadTeam objects without providing a members list. Add a member to only one team and
# # print both lists. Explain in a comment what happened.
# # 3. Create a corrected Team class using None as the default value and create a new list inside __init__.
# # 4. Repeat the test with two Team objects and show that each object now has its own list.


# class BadTeam:
#     def __init__(self, name, members=[]):
#         self.name = name
#         self.members = members

#     def add_member(self, name):
#         self.members.append(name)


# team_bad = BadTeam("Bad Developing")
# team_evil = BadTeam("Evil Developing")

# team_bad.add_member("Ada Lovelace")

# print(team_bad.members)
# print(team_evil.members)  # Both instances refer to the same list object

# # Correct version
# class Team:
#     def __init__(self, name, members=None):
#         self.name = name
#         self.members = members if members is not None else []

#     def add_member(self, member):
#         self.members.append(member)


# # Part B - Dictionary or class?
# # 1. Represent a movie using a dictionary with title, director and rating.
# # 2. Represent the same information using a Movie class.
# # 3. Add a method to Movie that returns whether the movie is highly rated. Choose a sensible rating
# # threshold.
# # 4. In comments, briefly explain one situation where you would choose a dictionary and one where you
# # would choose a class.

# movie_dict = {
#     "title": "Inception",
#     "director": "Christopher Nolan",
#     "rating": 8.8,
# }


# class Movie:
#     def __init__(self, title, director, rating):
#         self.title = title
#         self.director = director
#         self.rating = rating

#     def is_highly_rated(self):
#         return self.rating >= 8.0


# movie_obj = Movie("Inception", "Christopher Nolan", 8.8)

# print(movie_dict["title"], movie_dict["rating"])
# print(movie_obj.title, movie_obj.rating)
# print(movie_obj.is_highly_rated())  # True

# # Choose class: when the data has behavior or many objects of the same kind
# # are needed, e.g. a movie catalog where every movie has the same fields and methods.

# # Part C - Inheritance fundamentals
# # 1. Create a base class Account with owner and balance.
# # 2. Create SavingsAccount(Account) with an additional interest_rate attribute.
# # 3. Use super() so SavingsAccount reuses the initialization from Account.
# # 4. Create at least two objects and print their attributes.
# # 5. Write the "is-a" statement that explains why this inheritance relationship makes sense.


# class Account:
#     def __init__(self, owner, balance=0.0):
#         self.owner = owner
#         self.balance = balance


# class SavingsAccount(Account):
#     def __init__(self, owner, balance=0.0, interest_rate=0.02):
#         super().__init__(owner, balance)
#         self.interest_rate = interest_rate


# acc = Account("Anna", 1500)
# sav = SavingsAccount("Sven", 20000, 0.035)

# print(f"Account: {acc.owner}, balance {acc.balance}")
# print(
#     f"SavingsAccount: {sav.owner}, balance {sav.balance}, rate {sav.interest_rate:.1%}"
# )


# # Part D - Inherited and subclass-specific behaviour
# # 1. Create a base class Employee with name and a method get_information().
# # 2. Create Developer(Employee) and add a method that only Developer has.
# # 3. Create another Employee subclass of your choice and give it its own subclass-specific method.
# # 4. Demonstrate that both subclasses can use inherited behaviour from Employee.
# # 5. Demonstrate that an Employee object cannot automatically use a method that only exists in one of its
# # subclasses.


# class Employee:
#     def __init__(self, name):
#         self.name = name

#     def get_information(self):
#         return f"Employee: {self.name}"


# class Developer(Employee):
#     def __init__(self, name, language):
#         super().__init__(name)
#         self.language = language

#     def write_code(self):
#         return f"{self.name} is writing {self.language} code."


# class Manager(Employee):
#     def __init__(self, name):
#         super().__init__(name)
#         self.team = []

#     def add_team_member(self, employee):
#         self.team.append(employee)
#         return f"{employee.name} added to {self.name}'s team."


# mgr = Manager("Göran")
# emp = Employee("Anna")
# dev = Developer("Sven", "Python")

# print(mgr.get_information())
# print(mgr.add_team_member(dev))
# print(mgr.add_team_member(emp))
# print([member.name for member in mgr.team])
# print(dev.get_information())
# try:
#     print(emp.write_code)
# except AttributeError as error:
#     print(f"Error: {error}")

# Part E - super() and shared initialization
# 1. Create a base class Device with brand and year.
# 2. Add useful shared initialization logic inside Device, for example validation that year cannot be negative
# and an attribute such as is_active=True.
# 3. Create Laptop(Device) with one additional attribute such as ram_gb. Use super().
# 4. Create another Device subclass with its own additional attribute and use super() again.
# 5. Demonstrate that both subclasses receive the shared initialization logic from Device without duplicating
# it.


class Device:
    def __init__(self, brand, year, is_active=True):
        self.brand = brand
        if year < 1950:
            raise ValueError("Årtal måste vara större än 1950")
        self.year = year
        self.is_active = is_active


class Laptop(Device):
    def __init__(self, brand, year, ram_gb, is_active=True):
        super().__init__(brand, year, is_active)
        self.ram_gb = ram_gb


class Tablet(Device):
    def __init__(self, brand, year, screen_size, is_active=True):
        super().__init__(brand, year, is_active)
        self.screen_size = screen_size


laptop = Laptop("Lenovo", 2023, 16)
tablet = Tablet("Apple", 2022, 11)

print(laptop.brand, laptop.year, laptop.ram_gb, laptop.is_active)
print(tablet.brand, tablet.year, tablet.screen_size, tablet.is_active)

# Both trowing errors from baseclass
try:
    Laptop("Dell", 1800, 8)
except ValueError as e:
    print("Laptop:", e)

try:
    Tablet("Samsung", 1800, 10)
except ValueError as e:
    print("Tablet:", e)

# Part F - Method overriding
# 1. Create a base class Notification with a method send() that returns a general message.
# 2. Create EmailNotification(Notification) and SMSNotification(Notification).
# 3. Override send() in both subclasses so each returns a different message.
# 4. Create one object from each class and call send() on all of them.
# 5. Explain in a comment which method is used when send() is called on each object.


class Notification:
    def send(self):
        return "Sending a general notification."


# Part G - Override and still use the base method
# 1. Create a base class Report with a method get_summary() that returns a general report summary.
# 2. Create SalesReport(Report) and override get_summary().
# 3. Inside the overridden method, call the base implementation using super() and add SalesReport-specific
# information.
# 4. Create a SalesReport object and print the final result.

# Part H - Applied challenge: User accounts
# 1. Build a small user account system using inheritance.
# 2. Create a base class User with at least username and email.
# 3. Add a useful method to User that all user types should inherit.
# 4. Create AdminUser(User) and PremiumUser(User). Give each subclass at least one additional
# attribute and one subclass-specific method.
# 5. Use super() in both subclasses instead of duplicating User's initialization.
# 6. Add one method to User and override it differently in AdminUser and PremiumUser.
# 7. In one overridden method, use super() to reuse the base implementation and then extend it.
# 8. Create several objects and demonstrate inherited methods, subclass-specific methods and overridden
# methods.
# 9. Add at least one sensible validation using ValueError.
# 10. In comments, explain why AdminUser and PremiumUser have an "is-a" relationship with User.
