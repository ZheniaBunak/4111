from multiprocessing.sharedctypes import Value

list_iter = iter([1,2,3,4,5])
str_iter = iter('Hello World!')

print(f'{list_iter}, {str_iter}')

# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))
# print(next(list_iter))


#for el in list_iter:
 #   print(el)
#print('-----------------')
#for char in str_iter:
#    print(char)

class Counter:
    def __init__(self, max_value: int):
        self.max_value = max_value
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index <= self.max_value:
            return_value = self.index
            self.index += 1

            return return_value

        raise StopIteration

class StudentIterator:
    def __init__(self, grades):
        self.grades = grades
        self.index = 0

    def __next__(self):
        if self.index < len(self.grades):
            value = self.grades[self.index]
            self.index += 1
            return value

        raise StopIteration



class Student:
    def __init__(self,name, grades: list):
        self.name = name
        self.grades = grades

    def __iter__(self):
        return StudentIterator(self.grades)


    def add_grades(self, new_grades: list):
        self.grades.extend(new_grades)

    def average_grade(self):
        return sum(self.grades) / len(self.grades)



counter = Counter(100)

print(*counter, sep = '  | |  ' )

anton = Student('Антон', [8, 10, 8, 8])
anton.add_grades([10, 10, 11])

for gr in anton:
    print(gr)