class MyException(Exception):
    def __str__(self):
        return 'Це мій власний виняток! 😊'

def convert_to_int(value: str):
    try:
        number = int(value)
        return number
    except ValueError:
        raise MyException

try:
    user_input = input("Введіть число: ")

    result = convert_to_int(user_input)

except MyException as exc:
    print(f'Помилка! {exc}')
except Exception as exc:
    print(f'Сталася помилка: {exc}')
else:
    print(f'Ви ввели число: {result}')
finally:
    print('Програма завершила роботу.')
