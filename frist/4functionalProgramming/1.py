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
    pass
