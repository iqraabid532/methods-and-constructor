class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print(f'Name: {self.name}, Salary: {self.salary}')

    @classmethod
    def total_employees(cls):
        print(f'Total Employees: {cls.count}')

# Test Example
emp1 = Employee("aisha", 50000)
emp2 = Employee("abrish fatima", 60000)
emp1.display()
emp2.display()
Employee.total_employees()


class Math:
    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

# Test Example
print(Math.is_prime(7))   # True
print(Math.is_prime(10))  # False


class Account:
    def __init__(self, balance):
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if value >= 0:
            self._balance = value
        else:
            print("Invalid balance!")

# Test Example
acc = Account(1000)
print(acc.balance)
acc.balance = 2000
print(acc.balance)
acc.balance = -500 


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Python Basics", "aisha")
book2 = Book("Flask Guide", "abrish fatima")

print(book1.title, book1.author)
print(book2.title, book2.author)

