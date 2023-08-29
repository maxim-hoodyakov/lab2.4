#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    # Вводим список
    lst = list(map(int, input("Введите список целых чисел через пробел: ").split()))

    # Находим минимальный по модулю элемент
    min_elem = min(lst, key=abs)
    print(f"Минимальный по модулю элемент списка: {min_elem}")

    # Вычисляем сумму модулей элементов после первого нуля
    if 0 in lst:
        idx = lst.index(0)
        sum_elems = sum(abs(x) for x in lst[idx + 1:])
        print(f"Сумма модулей элементов списка, расположенных после первого элемента, равного нулю: {sum_elems}")
    else:
        print("В списке нет элементов, равных нулю.")

    # Преобразуем список
    new_lst = lst[::2] + lst[1::2]
    print(f"Преобразованный список: {new_lst}")