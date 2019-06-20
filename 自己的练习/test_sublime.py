import easygui as g
import sys
image = "C:\\Users\\杭州编程少年-3-01\\Downloads\\pikaqiu.gif"
msg = "你觉得皮卡丘可爱吗?"
choices=("可爱","不可爱")
title = '皮卡丘'
'''g.buttonbox(msg, title,  choices, image)'''
'''if g.indexbox(msg,title,choices,image):
	g.msgbox('Same with you.', 'wow', 'wonderful')
else:
	sys.exit(0)'''
msg2 = 'What will you do when you are free?'
title = 'hobby'
choice_list = ('reading', 'swimming', 'riding', 'cooking')
#单项选择
'''a = g.choicebox(msg2, title, choice_list)
g.msgbox(a + ' is your hobby')'''
#多项选择
#g.multchoicebox(msg2, title, choice_list)
#输入框
'''k = g.enterbox('tell me something', 'communication')
g.msgbox('I like ' + k)'''
#输入整型数字
#num = g.integerbox('What is your score?','test result',lowerbound =15, upperbound =75)







