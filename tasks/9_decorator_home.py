from functools import wraps
t = int(input('ВВедите номер задачи:'))

if t == 1:

    print('декоратор разворачивающий аргументы')

    def dec(func):
        def wrapper(*args):
            res = func(*args[::-1])
            return res
        return wrapper


    @dec
    def test_m(a, b, c):
        return a-b-c


    print(test_m(5, 1, 1))

elif t == 2:

    print('декоратор фильтрующий указаный элемент')

    def dec(filt):
        def f_dec(func):
            @wraps(func)
            def wrapper(*args, **kwargs):
                if filt in args:
                    raise Exception

                res = func(*args, **kwargs)
                return res
            return wrapper
        return f_dec

    @dec(filt='Oleg')
    def func_a(a, b, c):
        pass


    func_a(1, 2, 'Oleg')


elif t == 3:

    print('кеширующий декоратор')
    cache = {}

    def dec_cache(func):
        def wrapper(*args):
            t = tuple(args)
            if t in cache:
                print('return cache')
                return cache.get(t)
            res = func(*args)
            cache[t] = res
            print('Calculated the value')
            return res
        return wrapper


    @dec_cache
    def func_a(a, b, c):
        return a * b * c


    for i in range(10):
        print(f"cache -- {cache}")
        res = func_a(*map(int, input('Enter three number sep="," mask 1,2,3 >>>').split(',')))
        print(f" result - {res}")











