# print(abs(-1))
# print(max(1,2,3,-4,4))
# print(hex(12))
#
def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError("参数类型只能为int和float")
    if x < 0:
        return -x;
    else:
        return x
#
# print(my_abs(-5))
#
# print(my_abs("a"))

import math

def move(x,y,x_move,y_move):
    nx = x + x_move
    ny = y + y_move
    return nx,ny
print(move(1,2,4,4))
print(math.pi)

a = move(1,2,3,3,)
print(a)

def quadratic(a, b, c):
    z = math.sqrt(b*b - 4*a*c)
    if z > 0:
        x1 = (z -b) / 2 * a
        x2 = (z + b) / 2 * a
        return x1 , x2
    elif z == 0:
        return -(b / (2 * a))
    elif z < 0:
        return "此方程没有实数解"

print(quadratic(1,3,-4))

def power(x,n=2):
    temp = 1
    y = 0
    while y < n:
        temp = temp * x
        y += 1
    return temp

print(power(2,4))
print(power(n=4,x=2))

def add_end(L={}):
    if len(L) == 0:
        L = []
    L.append("END")
    return L
print(add_end(["name"]))
print(add_end())
print(add_end())

# 可变参数
def calc(*number):
    sum = 0
    for x in number:
        sum = sum + x * x
    return sum

jihe = [1,2,3]
print(calc(*jihe))
print(calc(1,2,3))

# 关键字参数
def person(name , age , **kw):
    if "city" in kw:
        print("有city参数")
    if "gender" in kw:
        print("有gender参数")
    print(name,age,kw)

person("张三",12,city="成都",gender="男")
names = {"city":"成都","gender":"男"}
person("张三",12,**names)

# 命名关键字参数
def person2(name,age , * , city,gender):
    print(name,age,city,gender)

person2("李四",14,gender="男",city="成都")

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(5))

def fact_other(num,product):
    if num == 1:
        return product
    return fact_other(num - 1 , num * product)

def fact2(n):
    return fact_other(n , 1)

print(fact2(5))


