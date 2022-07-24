import random
from sys import maxsize

num_task = int(input('Enter num task:'))
if num_task == 1:
    def rand_pin():

        ''' Генератор строки из четырех однозначных чисел. '''

        while True:
            pin = [random.randint(0, 9) for _ in range(4)]
            yield ''.join(map(str, pin))

    print(next(rand_pin()))

    def rand_pin_1():
        # return (''.join(map(str, [random.randint(0, 9) for _ in range(4)])) for i in range(maxsize**10))
        return ([random.randint(0, 9) for _ in range(4)] for i in range(maxsize**10))

    print(*(next(rand_pin_1())))


########################################################################################################
elif num_task == 2:
    comp_num = random.randint(1, 1000)
    print('Угадайте число за 5 попыток.')
    print(comp_num)
    user_num_1 = 0
    res = ''


    def gen_res():
        for i in range(5):
            result = 0
            user_num = int(input('Enter you int:'))
            if user_num == comp_num:
                result = 0
            elif abs(comp_num-user_num) < abs(comp_num-user_num_1):
                result = 1
            elif abs(comp_num-user_num) >= abs(comp_num-user_num_1):
                result = 2
            yield (['Угадал', 'Тепло', 'Холодно'][result], user_num)


    for r in gen_res():
        res, user_num_1 = r
        print(res)
        if res == 'Угадал':
            break

    else: print('Проиграл')

######################################################################################################

elif num_task == 3:

    def shift(lst: list, count_step: int):

        ''' Циклический сдвиг '''

        rev = 0
        if count_step < 0:
            rev = 1
        for i in range(abs(count_step)):
            if rev:
                lst.append(lst.pop(0))
                continue
            lst.insert(0, lst.pop(-1))

        return lst

    print(shift([1, 2, 3, 4, 5, 6], 2))

elif num_task == 4:

    def polind():

        ''' Самый большой полиндром. '''
        max_num = [0, 0, 0]
        for i in range(100, 1000):
            for r in range(100, 1000):
                num_cycle = str(i*r)
                if num_cycle == num_cycle[::-1]:
                    if max_num[0] < int(num_cycle):
                        max_num[0] = int(num_cycle)
                        max_num[1], max_num[2] = i, r

        return max_num

    print(*polind())


elif num_task == 5:

    def min_cr():
        ''' Наименьшее кратное'''
        num = 0
        while True:
            num += 1
            for i in range(2, 21):
                if num % i:
                    break
            else:
                break

        return num

    print(min_cr())

elif num_task == 6:
    def max_num():
        ''' Тринадцать соседних цифр'''
        mego_num = '''
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
        '''
        cur_str = mego_num.replace("\n", '').replace(' ', '')
        max_int = [0, [0, ]]

        for i in range(len(cur_str)):
            if len(cur_str)-i == 12:
                print(cur_str[i])
                break

            max_int_cycle = 1
            for r in range(13):
                max_int_cycle *= int(cur_str[i+r])
            if max_int_cycle > max_int[0]:
                max_int[0] = max_int_cycle
                max_int[1] = [int(cur_str[i+_]) for _ in range(13)]

        return max_int[0], max_int[1]

    max_int, num_seq = max_num()
    print(max_int, "".join(map(str, num_seq)))

elif num_task == 7:
    def sum_pr_int(n):
        '''Суммирование простых чисел'''
        max_sum = 1
        for i in range(1, n, 2):
            for r in range(2, i):
                if not i % r:
                    break
            else: max_sum += i
        return max_sum

    print(sum_pr_int(200_000))



elif num_task == 8:
    def comparison_lists(list_1: list, list_2: list) -> list:
        ''' Объединение списков'''
        list_res = []
        cycle_index = len(list_1)
        for i in range(cycle_index):
            list_res.append(list_1.pop(0))
            list_res.append(list_2.pop(0))

        return list_res

    print(comparison_lists([1, 2, 3], [11, 22, 33]))




















