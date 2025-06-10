class NegativeValueError(Exception):
    def __init__(self, number):
        super().__init__(f'Введено отрицательное число: {number}')

def check_number(number):
    if number < 0:
        raise NegativeValueError(number)
    return number

try:
    print(check_number(11))
    print(check_number(-4))
except NegativeValueError as e:
    print(e)