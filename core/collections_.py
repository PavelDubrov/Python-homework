def even(some_not_even_list):
    # Есть список not_even_list, реализовать логику в функции even:
    # создать новый список с четными элементами из списка not_even_list

    even_list = []
    for i in some_not_even_list:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


def get_ages(some_years_of_birth):
    # Следующий код с циклом, переписать с использованием
    # спискового включения (list comprehension)

    ages = [2014 - i for i in some_years_of_birth]
    return ages


def get_first_n_last(some_list):
    # Есть список numbers, реализовать логику в функции get_first_n_last:
    # вернуть новый список состоящий из первого и последнего элемента переданного списка
    first_n_last = []
    if len(some_list) >= 1:
        first_n_last.append(some_list[0])
        first_n_last.append(some_list[-1])
    return first_n_last


def get_list_without_repetition(some_list):
    # Написать функцию, которая принимает список и возвращает новый список,
    # состоящий из элементов принятого, но без повторений
    return list(set(some_list))


def map_keys_and_values(some_keys, some_values):
    # Написать функцию, которая возвращает словарь,
    # ключи которого из списка keys, а значения из списка values
    the_dict = {}
    for i in range(len(some_keys)):
        the_dict[some_keys[i]] = some_values[i]
    return the_dict


def count_symbols(some_string):
    # Написать функцию, которая принимает строку и возвращает словарь
    # состоящий из ключей - символов из строки,
    # значений - количество повторений этих символов в строке
    the_dict = {}
    for i in some_string:
        the_dict[i] = some_string.count(i)
    return the_dict


not_even_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print(even(not_even_list))

years_of_birth = [1990, 1991, 1990, 1990, 1992, 1991]
print(get_ages(years_of_birth))

numbers = [5, 10, 15, 20, 25]
print(get_first_n_last(numbers))

list_with_repetition = [1, 1, 3, 4, 2, 2, 2, 6]
print(get_list_without_repetition(list_with_repetition))

keys = ['red', 'green', 'blue']
values = ['#FF0000', '#00FF00', '#0000FF']
print(map_keys_and_values(keys, values))

s = 'some string'
print(count_symbols(s))
