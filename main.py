#
# Домашнее задание по сроку 25/05/2023
#

import tasks
import random

print('''
1)  6.8. Дано число n. Из чисел 1, 4, 9, 16, 25, ... напечатать те, которые не превышают n.
2)  6.22.(г) Дано натуральное число. Определить: г) сумму его цифр, больших пяти;
3)  6.22.(д) Дано натуральное число. Определить: д) произведение его цифр, больших семи;
4)  6.23.(а) Дано натуральное число. Определить: а) сколько раз в нем встречается цифра а;
5)  6.23.(в) Дано натуральное число. Определить: в) сумму его цифр, больших a 
            (значение a вводится с клавиатуры; 0 <= a <= 8);
6)  6.27.(б) Дано натуральное число. б) Определить, на сколько его максимальная цифра превышает минимальную.
    ''')

taskNumber = int(input('\nВведите номер запускаемой задачи: '))
# taskNumber = 1
taskExecute = None

if 1 < taskNumber > 6:
    print('Ошибка! Значение введено неверно!')
elif taskNumber == 1:
    taskExecute = tasks.doTask_6_8
elif taskNumber == 2:
    taskExecute = tasks.doTask_6_22_g
elif taskNumber == 3:
    taskExecute = tasks.doTask_6_22_d
elif taskNumber == 4:
    taskExecute = tasks.doTask_6_23_a
elif taskNumber == 5:
    taskExecute = tasks.doTask_6_23_v
elif taskNumber == 6:
    taskExecute = tasks.doTask_6_27_b

if taskExecute is not None:
    doRandomTest = True if input('Провести тестирование случайными величинами (1 - да, 0 - нет): ') == '1' else False
    if doRandomTest:
        print(f'\nБудет произведено тестирование задачи <{taskNumber}> 10-ю случайными условиями.')
        if taskNumber == 1:
            for i in range(1, 11): taskExecute(random.randint(1, 100))
        else:
            for i in range(1, 11):
                taskExecute(int(''.join(str(random.randint(0, 9)) for item in range(1, 11))))
    else:
        taskExecute()
