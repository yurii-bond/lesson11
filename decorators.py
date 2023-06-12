from datetime import datetime


def my_decorator(func):
    def wrapper():
        print('start of the decorator')
        func()
        print('end of the decorator')

    return wrapper


def not_during_the_night(func):
    def wrapper():
        if not 7 <= datetime.now().hour <= 22:
            func()
        else:
            print('Tsss!!!')

    return wrapper


def do_twice(func):
    def wrapper():
        func()
        func()
    return wrapper


@do_twice
@not_during_the_night
@my_decorator
def say_yuppi():
    print('Yuppi!')


say_yuppi()
