from functools import reduce
L = list(range(1,11))
print(L)
def fx(x):
    return x * x

print(list(map(fx,L)))
print(list(map(str,L)))
print(list(map(float,L)))

def fn(x,y):
    return x * 10 + y

def char2num(s):
    digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
    return digits[s]

print(reduce(fn,map(char2num , "12345")))

print(reduce(fn,[1,2,3,4,5]))

def name2up(s):
    a = s[0]
    b = s[0:-1]
    return  a.upper() +  b.lower()

print(list(map(name2up,['adam', 'LISA', 'barT'])))

def pro(x,y):
    return x * y

print(reduce(pro , [3, 5, 7, 9]))

def str2float(s):
    n = s.find(".")
    n = len(s)-n
    def fn(x,y):
        if y == -1:
            return x
        else:
            return x * 10 + y
    def char2num(m):
        DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        if m == ".":
            return -1
        else:
            return DIGITS[m]
    mm = map(char2num , s)
    sum = 1
    for x in range(n-1 ):
        sum = sum * 10
    return reduce(fn , mm) / sum

print(str2float("1616.11"))

