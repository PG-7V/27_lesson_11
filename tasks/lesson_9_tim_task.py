import time

n = int(input('Enter your integer:'))
start_time = time.time()

a_c = 0
a = dict()

s_i = 2
s_c = 2

for i in range(2, n):
    r = i
    a_c = 0

    while r != 1:
        r = int(r)
        if r in a.keys():
            a_c += a[r]
            a[i] = a_c
            break

        if r % 2 == 0:
            r = r / 2
            a_c += 1
        else:
            r = r * 3 + 1
            a_c += 1
    else:
        a[i] = a_c

    if a_c > s_c:
        s_i = i
        s_c = a_c

print(time.time()-start_time)
print(s_i, s_c)


