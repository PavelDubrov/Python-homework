from decorators import cache_decorator


@cache_decorator
def calculator(a, b, operation):
    # Здесь нужно реализовать функцию,
    # которая реализует основные арифметические операции между числами: +, -, /, *, **.
    # Так же следует сделать проверку, что поступивший оператор корректен (присутствует в этом списке +, -, /, *, **)
    if operation not in ("+", "-", "/", "*", "**"):
        raise Exception("You insert wrong operator.")
    if operation == "+":
        return a + b
    if operation == "-":
        return a - b
    if operation == "/":
        return a / b
    if operation == "*":
        return a * b
    if operation == "**":
        return a ** b


if __name__ == '__main__':
    # Тут было бы неплохо обрабатывать ошибку в случае передачи некорректных символов
    while True:
        try:
            a = int(input('Введите число a: '))
            break
        except ValueError:
            print("You should insert a number. Try it again.")
    while True:
        try:
            b = int(input('Введите число b: '))
            break
        except ValueError:
            print("You should insert a number. Try it again.")
    operation = input('Введите операцию: ')

    print('Результат: ', calculator(a, b, operation))
