class Human:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        return f'Привіт, я людина {self.name}'

class Student(Human):
    def __init__(self, name, grades):
        super().__init__(name)
        self.__grades = grades

    def say_hi(self):
      return f'Привіт, я студент з оцінками {self.__grades}'

    def average_grade(self):
        return sum(self.__grades) / len(self.__grades)

    def get_grades(self):
        return self.__grades


class Worker(Human):
    def __init__(self, name, salary):
        super().__init__(name)
        self.__salary = salary

        self.__start_job()



    def __start_job(self):
        print(f'робітник {self.name} почав роботу!')


    def say_hi(self):
        return super().say_hi() + f' з зарплатою {self.__salary} $'


bob = Student('Bob', [10, 8, 10, 7, 8, 9])
john = Worker('John', 10_000)


print(bob.say_hi())
print(john.say_hi())

print(bob.get_grades())



#dz

