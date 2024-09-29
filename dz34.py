
class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def average_grade(self):
        if len(self.grades) > 0:
            return sum(self.grades) / len(self.grades)
        else:
            return 0

    def __str__(self):
        return f"Студент {self.name} із середнім балом {self.average_grade():.2f}"

class StudentGroup:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def best_student(self):
        if not self.students:
            print("Група порожня!")
            return None
        best = max(self.students, key=lambda s: s.average_grade())
        print(f'Найкращий студент: {best.name} із середнім балом {best.average_grade():.2f}')


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Привіт! Мене звати {self.name} і мені {self.age} років.')

    def __len__(self):
        return self.age


class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Внесено {amount}. Баланс: {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостатньо коштів!')
        else:
            self.balance -= amount
            print(f'Знято {amount}. Баланс: {self.balance}')

    def get_balance(self):
        return self.balance



student1 = Student("Іван", [90, 85, 88])
student2 = Student("Марія", [78, 80, 95])
student3 = Student("Олексій", [92, 90, 85])


group = StudentGroup()
group.add_student(student1)
group.add_student(student2)
group.add_student(student3)


group.best_student()


person = Person("Олена", 25)
person.say_hello()
print(f"Вік людини: {len(person)}")

account = BankAccount("12345678", 1000)
account.deposit(500)
account.withdraw(300)
print(f"Поточний баланс: {account.get_balance()}")
