'''#range(101)为0-100的整数，range(1,100)为1-99的整数，range（1，100，2）为1-99的奇数
sum = 0
for x in range(1,10,2): 
	sum += x
print(sum)'''
#猜数字游戏
#计算机出一个1~100之间的随机数由人来猜
#计算机根据人猜的数字分别给出提示大一点/小一点/猜对了

#乘法口诀表
'''
for i in range(1, 10):
	for j in range(1, i+1):
		print('%d*%d=%d'%(i,j,i*j),end='\t')
	print()
'''
row = int(input('row number: '))
for i in range(row):
	for a in range(i + 1):
		print('*',end='')
	print()