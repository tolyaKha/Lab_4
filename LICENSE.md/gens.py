import random

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

def field(items, *args):
     if (len(args) == 1):
         for n in items:            #перебор словарей
             if (args[0] in n):
                 yield n[args[0]]

     if (len(args) > 1):
         for n in items:
             buf = {}
             #for i in range(len(args)):     #i-номер текущего аргумента
             i=0
             while (i < len(args)):
                 if (args[i] in n):
                     buf[args[i]] = n[args[i]]          #!!??если {'price': 7000, 'color': 'white'}, то 'price':, 'title':
                 i+=1
             if (buf != {}):
                yield buf


def gen_random(begin, end, quantity):   #quantity-количество
    for i in range(quantity):
       yield random.randint(begin, end)