# ord() 获取字符的整数表示
print(ord("A"))
print(ord("中"))
# chr() 把整数转为字符
print(chr(65))
print(chr(20013))
# len() 计算字符串长度
print(len("adf"))
print("中文")

# %d 整数 %s 字符串 %f 浮点数 %x 二进制数
print("hello %s" % "world")
print("hello %s this is %d" % ("world",2018))

#  list集合
names = ["a","b","c"]
print(names[1])
print(names[-1])

# 追加
names.append("d")
# 指定位置添加
names.insert(0,"0")
# 删除末尾
names.pop()
# 删除指定位置
names.pop(0)
# 替换指定位置
names[0] = "aa"

yuyan = ["java","python"]
names.append(yuyan)
print(names)
print(names[-1][0])

# tuple集合 不可变
t = ("a","b","c")

t1 = ("a","b",["A","B"])

t1[2][0] = "X"
t1[2][1] = "Y"

print(t1)

# 条件判断
sex = "df"
if sex == "男":
    print("小贱人")
elif sex == "女":
    print("小婊砸")
else:
    print("可怕")


if sex:
    print("sex有值")

temp = input("年龄:")
age = int(temp)
if age > 20:
    print("老男人")
else:
    print("小婊砸")

# for循环
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

sum = 0
for x in range(101):
    sum = sum + x
print(sum)

# while 循环
sum = 0
n = 0
while n < 100:
    n = n +1
    sum = sum + n
print(sum)

# break 跳出循环 continue 跳过此次循环
x = 0
while x <10:
    x += 1
    if x == 3:
        continue
    if x == 7:
        break
    print(x)

# dict 和 set
d = {"zhangsan":16,"lisi":17,"wangwu":18}
print(d.get("zhangsan"))
print(d.get("wangmazi"))
d.pop("zhangsan")
print(d)

s = set([1,2,3])
print(s)
s.add(4)
s.add(4)
s.remove(1)
print(s)

s1 = set([1,2,3])
s2 = set([2,3,4])
print(s1 & s2)
print(s1 | s2)

