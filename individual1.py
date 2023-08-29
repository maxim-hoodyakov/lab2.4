#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = list(map(int, input().split()))
    x = int(input("Введите число для поиска: "))

    indices = [i for i, val in enumerate(A) if val == x]

    if len(indices) == 0:
        print(f"Число {x} не найдено в списке.")
    else:
        print(f"Индекс числа {x} в списке: {indices}")