"""
http://pythontutor.ru/lessons/functions/problems/reverse_rec/
Дана последовательность целых чисел, заканчивающаяся числом 0. Выведите эту последовательность в обратном порядке.
При решении этой задачи нельзя пользоваться массивами и прочими динамическими структурами данных. Рекурсия вам поможет.

Эту задачу невозможно решить самостоятельно. Обратитесь к своему преподавателю за помощью.
"""


def smth():
    a = int(input())
    if a != 0:
        smth()
    print(a)


smth()