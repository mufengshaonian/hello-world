#多个输入框
import easygui as g
msg = '请填写以下信息(其中*项为必填)'
title = '信息表'
fieldNames = ['*name', '*age', '*email', 'phone number','address', 'social account']
fieldValues = []
fieldValues = g.multenterbox(msg, title, fieldNames)
#print(fieldValues)
while True:
	if fieldValues == None :
		break
	errmsg = ''
	for i in range(len(fieldNames)):
		option = fieldNames[i].strip()
		if fieldValues[i].strip =='' and option[0] == '*':
			errmsg += ('【%s】为必填项  ' %fieldNames[i])
	if errmsg == '':
		break
	fieldValues = g.multenterbox(errmsg, title, fieldNames,fieldValues)
print('你填写的资料如下：%s' %str(fieldValues))
