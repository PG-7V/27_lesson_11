import time

def get_nod(a, b):
    """Вычислянтся НОД для натуральных чисел a и b
        по быстрому алгоритму Евклида.

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: НОД
    """

    if a < b:
        a, b = b, a

    while b:
        a, b = b, a % b

    return a


def test_nod(func):
    # --- test 1 ---
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print("#test1 - ok")

    else: print("#test1 - fail")

    # --- test 2 ---
    a = 100
    b = 1
    res = func(a, b)
    if res == 1:
        print("#test2 - ok")

    else: print("#test2 - fail")

    # --- test 3 ---
    a = 2
    b = 100_000_000
    st = time.time()
    res = func(a, b)
    et = time.time() - st

    if res == 2 and et < 1:
        print("#test3 - ok")

    else:
        print("#test3 - fail")









test_nod(get_nod)

########################################################################






