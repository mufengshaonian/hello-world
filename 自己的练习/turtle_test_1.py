import turtle
'''
#螺旋线绘制
turtle.speed('fast')
turtle.pensize(2)
for x in range(100):
	turtle.forward(2*x)
	turtle.left(90)
turtle.done()
'''
#彩色螺旋线绘制
turtle.speed('fast')
turtle.pensize(2)
turtle.bgcolor('black')
colors =['red','yellow','purple','white','blue','green']
for x in range(360):
	turtle.forward(x/2)
	#turtle.color(colors[x % 6])
	turtle.color('blue')
	turtle.left(59)
turtle.done()

