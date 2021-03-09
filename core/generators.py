from random import randint


def gen(num):
    # написать генераторную функцию, которая
    # возвращает num рандомных чисел от 1 до 100
    for i in range(num):
        yield randint(1, 100)


my_gen1 = gen(4)
for i in my_gen1:
    print(i)

print("-----")

# написать генераторное выражение, которое делает то же самое
n = 3
my_gen2 = (randint(1, 100) for i in range(n))

for i in my_gen2:
    print(i)
