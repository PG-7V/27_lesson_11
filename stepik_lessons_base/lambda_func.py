def filter_lst(s, filter=None):
    if filter is None:
        return tuple(s)

    t = tuple()
    for i in s:
        if filter(i):
            t += i,
    return t


it = list(map(int, input().split()))

print(*filter_lst(it))
print(*filter_lst(it, lambda x: x < 0))
print(*filter_lst(it, lambda x: x >= 0))
print(*filter_lst(it, lambda x: 3 <= x <= 5))















