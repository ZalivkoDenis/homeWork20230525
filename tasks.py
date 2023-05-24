# 1)  6.8. Дано число n. Из чисел 1, 4, 9, 16, 25, ... напечатать те, которые не превышают n.
# 2)  6.22.(г) Дано натуральное число. Определить: г) сумму его цифр, больших пяти;
# 3)  6.22.(д) Дано натуральное число. Определить: д) произведение его цифр, больших семи;
# 4)  6.23.(а) Дано натуральное число. Определить: а) сколько раз в нем встречается цифра а;
# 5)  6.23.(в) Дано натуральное число. Определить: в) сумму его цифр, больших a
#             (значение a вводится с клавиатуры; 0 <= a <= 8);
# 6)  6.27.(б) Дано натуральное число. б) Определить, на сколько его максимальная цифра превышает минимальную.

# Служебная функция
def inputN(request: str, n: int = None, paramName: str = 'n') -> int:
    if request != '': print(f'\n-----\n{request}')
    if n is None:
        n = int(input(f'Введите {paramName}: '))
    else:
        print(f'Входное значение {paramName}: {n}')
    return n


def doTask_6_8(n: int = None):
    n = inputN('6.8. Дано число n. Из чисел 1, 4, 9, 16, 25, ... напечатать те, которые не превышают n.', n)
    i = 1
    while i ** 2 <= n:
        print(f'число i({i}) = {i ** 2} < {n}')
        i += 1
    print(f'===== i({i}) = {i ** 2} >= {n}')
    return None


def doTask_6_22_g(n: int = None):
    n = inputN('6.22.(г) Дано натуральное число. Определить: г) сумму его цифр, больших пяти.', n)
    result = 0
    while n > 0:
        lastDigit = n % 10
        if lastDigit > 5:
            result += lastDigit
        n = n // 10
    print(f'Сумма = {result}\n')
    return result


def doTask_6_22_d(n: int = None):
    n = inputN('6.22.(д) Дано натуральное число. Определить: д) произведение его цифр, больших семи.', n)
    result = 1
    while n > 0:
        lastDigit = n % 10
        if lastDigit > 7:
            result = result * lastDigit
        n = n // 10
    if result == 1: result = 0
    print(f'Произведение = {result}\n')
    return result


def doTask_6_23_a(n: int = None, a: int = None):
    n = inputN('6.23.(а) Дано натуральное число. Определить: а) сколько раз в нем встречается цифра а.', n)
    a = inputN('', a, 'a') % 10
    counter = 0
    while n > 0:
        if n % 10 == a: counter += 1
        n = n // 10
    print(f'Цифра {a} встречается раз: {counter}')
    return counter



def doTask_6_23_v(n: int = None, a: int = None):
    n = inputN('''6.23.(в) Дано натуральное число. Определить: в) сумму его цифр, больших a
    (значение a вводится с клавиатуры; 0 <= a <= 8)''', n)
    a = inputN('', a, 'a') % 10
    summC = 0
    print('0', end=' ')
    while n > 0:
        cifer = n % 10
        if cifer > a:
            summC += cifer
            print(f'+ {cifer}', end=' ')
        n = n // 10
    print(f'= {summC}')
    return summC


def doTask_6_27_b(n: int = None):
    n = inputN('6.27.(б) Дано натуральное число. б) Определить, на сколько его '
               'максимальная цифра превышает минимальную.', n)
    maxC = None
    minC = None
    while n > 0:
        cifer = n % 10
        if maxC is None or cifer > maxC: maxC = cifer
        if minC is None or cifer < minC: minC = cifer
        n = n // 10
    print(f'Максимальная цифра {maxC} превышает минимальную {minC} на {maxC - minC}.')
    return (maxC - minC)
