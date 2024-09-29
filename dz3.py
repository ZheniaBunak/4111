
class Person:
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def get_age(self):
        return self._age

    def say_hello(self):
        print(f"Привіт! Мене звати {self.name}, і мені {self._age} років.")

class Driver(Person):
    def __init__(self, name, age, driver_license_number):
        super().__init__(name, age)
        self.driver_license_number = driver_license_number

    def show_license(self):
        print(f"Мій номер водійського посвідчення: {self.driver_license_number}")




person = Person("Олена", 30)
person.say_hello()
print(f"Вік: {person.get_age()}")

driver = Driver("Іван", 45, "AB123456")
driver.say_hello()
driver.show_license()
print(f"Вік: {driver.get_age()}")
