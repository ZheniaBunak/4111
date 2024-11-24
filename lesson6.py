
class MyException(Exception):
    def __str__(self):
        return 'Це мій вийняток!)😊'


def raiser(n: int):
    match n:
        case 1:
            raise ValueError
        case 2:
            raise ZeroDivisionError
        case 3:
            raise IndexError('Це мій власний IndexError')
        case 4:
            raise KeyError
        case 5:
            raise KeyboardInterrupt
        case 6:
            raise MyException


try:


    n1 = int(input('Введіть число 1:'))
    n2 = int(input('Введіть число 2:'))

    result = n1 / n2

except ZeroDivisionError:
    print('Ти не можшь ділити на  0')
except ValueError:
    print('Ти вписав не число')
except Exception as exc:
  print(f'Сталася помилка: {exc}')
else:
    print(result)
finally:
    print('finally')