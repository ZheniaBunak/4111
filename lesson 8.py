import random
from cgitb import reset
from idlelib.debugger_r import restart_subprocess_debugger


def powers(number, end_pow):
    for p in range(1, end_pow + 1):
        yield number ** p


def get_random_numbers(count: int):
    for _ in range(count):
        yield random.randint(-100, 100)

result = list(get_random_numbers(1000))

print(result)