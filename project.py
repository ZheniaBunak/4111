import random


class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def __str__(self):
        return f'{self.model} за {self.price} грн.'


class Person:
    def __init__(self, name, profession, dream_car):
        self.name = name
        self.money = random.randint(100000, 1000000)
        self.months = 0
        self.happiness = random.randint(30, 70)
        self.profession = profession
        self.dream_car = dream_car

    def show_info(self):
        print(f'Меня зовут {self.name}, моя профессия {self.profession}, я имею {self.money} грн., '
              f'мой уровень счастья: {self.happiness}/100, Машина мечты: {self.dream_car}')

    def buy_car(self, dealership):
        car = self.dream_car
        initial_gap = car.price - self.money
        while self.money < car.price:
            remaining_gap = car.price - self.money
            self.update_happiness(initial_gap, remaining_gap)
            print(f'{self.name} не хватает денег на {car}. У него {self.money} грн. Он идет работать как {self.profession}.')
            self.work()
            print(f'--==Уровень радости {self.name} теперь {self.happiness}/100.==--')
        self.money -= car.price
        dealership.sell_car(car)
        self.happiness = 100
        print(f'-------{self.name} купил {car}. Уровень радости увеличился до 100/100.-------')

    def update_happiness(self, initial_gap, remaining_gap):
        progress = (initial_gap - remaining_gap) / initial_gap
        if progress < 0.5:
            happiness_change = -random.randint(5, 15)
        else:
            happiness_change = random.randint(5, 25)
        self.happiness = round(max(0, min(100, self.happiness + happiness_change)))

    def work(self):
        if self.profession == 'Программист':
            earned_money = random.randint(30000, 50000)
        elif self.profession == 'Учитель':
            earned_money = random.randint(15000, 25000)
        elif self.profession == 'Инженер':
            earned_money = random.randint(20000, 35000)
        elif self.profession == 'Врач':
            earned_money = random.randint(25000, 40000)

        self.money += earned_money
        self.months += 1
        print(f'----------{self.name} проработал {self.months} месяц(а) как {self.profession} и заработал {earned_money} грн. Теперь у него {self.money} грн.----------')


class CarDealership:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        if self.cars:
            print('-------В автосалоне есть следующие машины:-------')
            for i, car in enumerate(self.cars, 1):
                print(f'--------{i}. {car}--------')
        else:
            print('Автосалон пуст, машин нет.')

    def sell_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
            print(f'Машина {car.model} продана.')
        else:
            print(f'Ошибка: {car.model} не найдена в автосалоне.')


professions = ['Программист', 'Учитель', 'Инженер', 'Врач']
cars = [
    Car('BMW X5', 1500000),
    Car('Audi A4', 1000000),
    Car('Tesla Model S', 2000000),
    Car('Lada Vesta', 500000)
]


dealership = CarDealership()
for car in cars:
    dealership.add_car(car)


person1 = Person('Иван', random.choice(professions), random.choice(dealership.cars))
person2 = Person('Сергей', random.choice(professions), random.choice(dealership.cars))


print("Информация о людях:")
person1.show_info()
person2.show_info()


dealership.show_cars()


person1.buy_car(dealership)
person2.buy_car(dealership)
