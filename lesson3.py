import random


class Human:

    def __init__(self,name='Human', job=None, house=None, car=None):
        self.name = name
        self.job = job
        self.house = house
        self.car = car

        self.money = 100
        self.gladness = 50 #щастя
        self.satiety = 50 #ситість

    def get_job(self):
        self.job = Job(jobs)
        print(f'{self.name} отримав роботу {self.job.job_name} за зарплатою {self.job.salary}$')

    def get_house(self):
        self.house = House()
        print(f'{self.name} отримав будинок!')


    def get_car(self):
        self.car = Auto(cars)
        print(f'{self.name} отримав машину {self.car.brand}!')


    def work(self):
        if not self.car.drive():
            if self.car.fuel < 20:
                self.shopping('fuel')
            else:
                self.to_repair()
            return

        self.money += self.job.salary
        self.gladness -= self.job.gladness_less
        self.satiety -= 4




    def eat(self):
        if self.house.food <= 0:
            self.shopping('food')
        else:
            self.satiety += 5
            self.house.food -= 5

            if self.satiety > 100:
                self.satiety = 100

    def shopping(self, manage):
        if manage == 'fuel':
            print(f'{self.name} купляє паливо!')
            self.money -= 100
            self.car.fuel += 100
        elif manage == 'foof':
            print(f'{self.name} купляє їжу')
            self.money -= 50
            self.house.food += 50
        elif manage == 'delicious':
            print(f'{self.name} сходив у ресторан!')
            self.money -= 100
            self.gladness += 10
            self.satiety += 10


    def chill(self):
        self.gladness += 10
        self.house.mess += 5

    def clean_house(self):
        self.gladness -= 5
        self.house.mess = 0

    def to_repair(self):
        self.money -= 500
        self.car.strength +=50

    def day_indexes(self,day):
        print(f'----====Сьогодні {day} життя {self.name}====----')
        print(f'----====Робота: {self.job.job_name}. Зарплата: {self.job.salary} $====----')
        print(f'--==Рівень щастя: {self.gladness}. Гроші: {self.money}  $. Ситість: {self.satiety}==--')
        print(f'--==Стан автомобіля: пальне: {self.car.fuel} , міцність: {self.car.strength}==--')




    def is_alive(self):
        if self.gladness < 0:
            print(f'{self.name} впав у депресію')
            return False
        if self.money <= -500:
            print(f'{self.name} вліз у борги')
            return False
        if self.satiety < 0:
            print(f'{self.name} помер з голоду')
            return False

        return True



    def live(self,day):
        if not self.is_alive():
            return  False

        if self.house is None:
            self.get_house()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()

        self.day_indexes(day)

        if self.satiety < 20:
            self.eat()
        if self.house.mess > 20:
            self.clean_house()



        dice = random.randint(1, 4)

        if dice == 1:
            print(f'{self.name} пішов на роботу!')
            self.work()
        elif dice == 2:
            print(f'{self.name} вирішив відпочивати!')
            self.chill()
        elif dice == 3:
            print(f'{self.name} прибирає будинок')
            self.clean_house()
        elif dice == 4:
            self.shopping('delicious')



class House:
    def __init__(self):
        self.food = 0
        self.mess = 0

class Job:
    def __init__(self, job_dict):
        self.job_name = random.choice(list(job_dict))

        self.salary =  job_dict[self.job_name]['salary']
        self.gladness_less = job_dict[self.job_name]['gladness_less']






class Auto:
    def __init__(self, cars_dict):
        self.brand = random.choice(list(cars_dict))

        self.fuel = cars_dict[self.brand]['fuel']
        self.strength = cars_dict[self.brand]['strength'] #отличаются ключем и названием
        self.consumption = cars_dict[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('Авто не поїхало((((')
            return False





cars = {
    'BMW': {
        'fuel': 100,
        'strength': 25,
        'consumption': 15
    },
    'Honda': {
        'fuel': 80,
        'strength': 40,
        'consumption': 25
    },
    'Жигуль': {
        'fuel': 40,
        'strength': 10,
        'consumption': 15
    },
    'Toyota': {
        'fuel': 70,
        'strength': 35,
        'consumption': 12
    },
    'Audi': {
        'fuel': 60,
        'strength': 55,
        'consumption': 15
    }
}
jobs = {
    'Прибиральник': {
        'salary': 150,
        'gladness_less': 14
    },
    'Касир': {
        'salary': 200,
        'gladness_less': 20
    },
    'Лікар': {
        'salary': 250,
        'gladness_less': 15
    },
    'Junior Python Розробник': {
        'salary': 900,
        'gladness_less': 8
    },
    'Senior Python Розробник': {
        'salary': 3500,
        'gladness_less': 3
    }

}


bob = Human('Боб')

for day in range(1, 10001):
    if not bob.is_alive():
        break

    bob.live(day)




















