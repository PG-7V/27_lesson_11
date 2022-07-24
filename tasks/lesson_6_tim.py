# -*- coding: utf-8 -*-
num_task = int(input('Enter number task:'))
############################# -- 1 -- #############################
##
if num_task == 1:
    n = int(input('Enter int:'))
    res = True

    i = 2
    while i <= n**.5:
        if n % i == 0:
            res = False
            break
        i += 1
    print(res)

############################# -- 2 -- #############################
##
elif num_task == 2:
    n = int(input("Enter integer:"))
    d = int(input("Enter degree"))

    for i in range(1, n + 1):
        print(i ** d, end=" ")

############################# -- 3 -- #############################
elif num_task == 3:
    count = 0
    list_int = list(input('Enter int:'))
    for i in list_int:
        if i.isdigit():
            if int(i) % 2 == 0:
                count += 1
    print('Четных ' + str(count) + '\nНечетных ' + str(len(list_int)-count))

############################# -- 4 -- #############################
elif num_task == 4:

    ''' Task **'''

    a = float(input('How much money?:'))
    years = int(input('What is the period in years?:'))
    add_deposit = int(input('Top up your account every month or not enter 0:'))*12
    inflation = 0.17
    usd = 2.62
    eur = 2.79

    for i in range(1, years+1):
        a *= 1-inflation
        a += (a+add_deposit) * .1

    print(f'{int(a)} - RUB\n{int(a/usd)} - USD\n{int(a/eur)} - EUR\n '
          f'At the current level of inflation - {inflation*100}%, 1 usd = {usd} RUB, 1 eur = {eur}.')





