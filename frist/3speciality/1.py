from collections import Iterable
import os
L = ["张三","李四","王五","二麻子"]
print(L[0:3])
print(L[:4])
print(L[-3:])
print(L[:])

T = (1,2,3,4)
print(T[0:3])
print(T[-2:])
print(T[:])
print(T[:4])

S = "ABCDEF"
print(S[:])
print(S[0:3])
print(S[-3:])
print(S[:2])

def trim(s):
    if not s:
        raise Exception("字符串不能为空")
    if s[:1] == "":
        raise Exception("该字符串首字符不是空格")
    if s[-1:] == "":
        raise Exception("该字符串最后一个字符不是空格")
    return s[1:-1]
s = " sdf "

print(trim(s))


# 迭代
D = {"name":"张三","age":19,"gender":"男"}
for value in D.values():
    print(value)


print(isinstance([1,2,3],Iterable))

for i,value in enumerate([1,2,3]):
    print(i,value)

for x,y in {(1,2),(3,4)}:
    print(x,y)

def findMinAndMax(L):
    if len(L) == 0:
        raise Exception("集合长度为空")
    if len(L) == 1:
        return (L[0],L[0])
    if len(L) == 2:
        if L[0] > L[1]:
            return [L[1],L[0]]
        else:
            return [L[0],L[1]]
    min = L[0]
    max = L[0]
    for x in L:
        if x <= min:
            min = x
        if x >= max:
            max = x
    return (min,max)

print(findMinAndMax([1,2,3,4,-1,34,53]))

print(list(range(1,10)))

print([x * x for x in range(1,10)])

print([m + n for m in [1,2,3] if m ==2 for n in [1,2,3] if n == 3])

# 列出文件路径
print([d for d in os.listdir("E:")])

D = {"name":"张三","age":"19","gender":"男"}

print([k + "=" + v for k,v in D.items()])

L3 = ["Zhang","San"]
print([v.lower() for v in L3])

L4 = ['Hello', 'World', 18, 'Apple', None]
print([v.lower() for v in L4 if isinstance(v,str)])

# 生成器
g = (x for x in range(11))
for v in g:
    print(v)

def fib(max):
    n ,a ,b = 1,0,1
    while n < max:
        print(n)
        b = n
        n = n + a
        a = b
    else:
        return

print(fib(20))

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
print(next(o))
print(next(o))
print(next(o))

def fib2(max):
    n ,a ,b = 1,0,1
    while n < max:
        yield n
        b = n
        n = n + a
        a = b
    else:
        return
print([y for y in fib2(20)])

for y in fib2(20):
    print(y)

f = fib2(20)
while True:
    try:
        y = next(f)
        print(y)
    except StopIteration as e:
        print("迭代异常,已经没有值了")
        break

