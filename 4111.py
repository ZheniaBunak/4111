

class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def __str__ (self):
        return f"Об'єкст класу людина з ім'ям {self.name}"

    def __int__(self):
        return self.age




    def say_hi(self):
        print(f'Привіт! Мене звуть {self.name}! Мені {self.age} років. Мій зріст становить {self.height} см.')

    def birthday(self, years):
        self.age += years



class Auto:
    def __init__(self,brand, max_passengers=5):
        self.brand = brand
        self.max = max_passengers

        self.passengers = []

    def add_passengers(self, *new_passengers):
        for passenger in new_passengers:
            if len(self.passengers) >= self.max:
                print('Авто вже зайнято, іди на вулицю!')
            else:
                self.passengers.append(passenger)
    def print_all_passengers(self):
        if len(self.passengers) == 0:
            print(f'Авто {self.brand} порожнє!')
        else:
            print(f'Список пасажирів {self.brand}: ')
            for passenger in self.passengers:
                passenger.say_hi()




bob = Human("Боб",17,180)
bob.say_hi()

alice = Human("Аліса",28,150)
alice.say_hi()
alice.birthday(5)
alice.say_hi()

bmw = Auto('BMW')
tesla = Auto('Tesla')

tesla.add_passengers(bob,alice)

bmw.print_all_passengers()
tesla.print_all_passengers()
