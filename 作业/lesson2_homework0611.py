#列表
a = ['red','green','black','pink','blue','green','pink']
print(a)
print("the color is : " + "_".join(a))
a.append('white')
print(a)
a.insert(3,'grey')
print(a)
a.remove("black")
print(a)
a.pop(2)
print(a.pop(2))
print(a)
del a[0]
print(a)
b = a.count('pink')
print(b)
c = a.index('green')
print(c)
a.sort()
print(a)
a.reverse()
print(a)
#元组
'''test = ('star','moon','sun')
print(test)
del test['star']
print(test)'''

squares = []
for x in range(10):
    squares.append(x**2)
print(squares)
#字典
location = {'hangzhou':'zhejiang','huangshan':'anhui','jinan':'shandong'}
#'''location. {'chengdu':'sichuan'}'''
print(location['huangshan'])
del location['huangshan']
print(location)