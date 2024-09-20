class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0

class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def best_student(self):
        if not self.students:
            return None
        best = max(self.students, key=lambda student: student.average_grade())
        return best.name, best.average_grade()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Привіт, мене звати {self.name}!")

    def __len__(self):
        return self.age

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} грн було додано на рахунок. Поточний баланс: {self.balance} грн.")
        else:
            print("Сума повинна бути більшою за 0.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} грн було знято з рахунку. Поточний баланс: {self.balance} грн.")
        else:
            print("Недостатньо коштів або некоректна сума.")

    def get_balance(self):
        return self.balance

student1 = Student("Олег", [90, 85, 78])
student2 = Student("Іван", [88, 92, 80])
student3 = Student("Анна", [95, 93, 90])

group = StudentGroup()
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)

best_name, best_avg = group.best_student()
print(f"Найкращий студент: {best_name} із середнім балом {best_avg}")

person = Person("Катерина", 25)
person.say_hello()
print(f"Вік людини: {len(person)} років")

account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Поточний баланс: {account.get_balance()} грн")