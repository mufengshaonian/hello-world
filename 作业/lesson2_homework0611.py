#列表
a = ['red','green','black','pink','blue','green','pink']
print(a)
print("the color is : " + "_".join(a))
#增
a.append('white')
print(a)
#插入
a.insert(3,'grey')
print(a)
#删除
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
#排序
a.sort()
print(a)
a.reverse()
print(a)
#元组
test = ('star','moon','sun')
print(test[1])


squares = []
for x in range(10):
    squares.append(x**2)
print(squares)


#字典
subject_teacher = {'science':'Tom','music':'Andy','maths':'Shaz','PE':'Chad'}
#查询
print(subject_teacher['science'])
#增添
subject_teacher['art'] = 'Lancy'
#修改
subject_teacher['music'] = 'Joe'
#删除
del subject_teacher['PE']
print(subject_teacher)
#遍历
for subject, teacher in subject_teacher.items():
    print(subject.title() + "'s teacher is " + teacher + '.')

#嵌套
info_01 = {'name':'tom','age':32,'location':'shanghai'}
info_02 =  {'name':'lucy','age':25,'location':'hangzhou'}
info_03 =  {'name':'simon','age':15,'location':'changsha'}
info_all = [info_01, info_02, info_03]
for info in info_all:
    if info['age'] >= 20:
        info['location'] = 'beijing'
    else:
        info['location'] = 'guangzhou'
print(info_all)