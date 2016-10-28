#!/usr/bin/env python3
from librip.gens import gen_random
from librip.iterators import Unique

data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 'Aaa', 'aaa']
data2 = gen_random(1, 3, 10)

# Реализация задания 2
data_1 = [1, 4, 1, 1, 90, 5, 2, 3, 2, 2]
for i in sorted(Unique(data_1)):
    print(i, end = ' ')

print()

for i in Unique(list(gen_random(1, 3, 10))):
    print(i, end = ' ')

print()

data_2 = ['a', 'A', 'b', 'c', 'B', 'C']
print(list(Unique(data_2)))

print(list(Unique(data_2, ignore_case=True)))