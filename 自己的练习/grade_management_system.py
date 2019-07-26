#成绩管理系统练习
names = []
grades = []
while True:
	print('''这是一个学生成绩管理系统，具有以下功能：
1增加学生姓名和成绩
2删除学生姓名和成绩
3查询所有
4根据学生姓名查成绩
5根据姓名修改成绩
6退出	''')
	a = int(input('操作序号： '))
	if a == 1:
		name1 = input('请输入姓名： ')
		if name1 in names:
			print('this name already existed.')
			continue
		else:
			grade1 = input('成绩： ')
			names.append(name1)
			grades.append(grade1)
			print('添加成功！')
	elif a == 2:
		name2 = input('姓名： ')
		b = names.index(name2)
		del names[b]
		del grades[b]
		print('删除成功')
	elif a == 3:
		for i in names:
			c = names.index(i)
			print(names[c])
			print(grades[c])
	elif a == 4:
		name4 = input('学生姓名： ')
		if name4 in names:
			d = names.index(name4)
			print(grades[d])
		else:
			continue
	elif a == 5:
		name5 = input('学生姓名： ')
		d = names.index(name5)
		new_grade = input('新成绩： ')
		grades[d] = new_grade
		print(name5, grades[d])
	elif a == 6:
		print('退出')
		break
	else:
		continue


