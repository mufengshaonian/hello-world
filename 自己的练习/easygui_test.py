import easygui as g
g.msgbox("Hello, it's your first time to program^_^",'Hello World')
msg ="Why do you want to learn programming？"
title = "interaction"
choices = ["No idea", "Design games", "learn the world", "Playing for fun"]
choice = g.choicebox(msg, title, choices)
g.msgbox('Your choice is: ' + str(choice), 'Consquence')