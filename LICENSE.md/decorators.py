# Здесь необходимо реализовать декоратор, print_result который принимает на вход функцию,
# вызывает её, печатает в консоль имя функции, печатает результат и возвращает значение
# Если функция вернула список (list), то значения должны выводиться в столбик
# Если функция вернула словарь (dict), то ключи и значения должны выводить в столбик через знак равно
# Пример из ex_4.py:
# @print_result
# def test_1():
#     return 1
#
# @print_result
# def test_2():
#     return 'iu'
#
# @print_result
# def test_3():
#     return {'a': 1, 'b': 2}
#
# @print_result
# def test_4():
#     return [1, 2]
#
# test_1()
# test_2()
# test_3()
# test_4()
#
# На консоль выведется:
# test_1
# 1
# test_2
# iu
# test_3
# a = 1
# b = 2
# test_4
# 1
# 2
def print_result(function_to_decorate):
    def wrapper_function(*args):
        print(function_to_decorate.__name__)
        if (type(function_to_decorate(*args)) == type(list())):
            a = function_to_decorate(*args)
            for i in range(len(a)):
                print(a[i])
        elif (type(function_to_decorate(*args)) == type(dict())):
            b = function_to_decorate(*args)
            for key in b:
                print(key,' = ', b[key])
        else:
            print(function_to_decorate(*args))
        return function_to_decorate(*args)
    return wrapper_function
