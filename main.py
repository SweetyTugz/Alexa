from tkinter import *
root=Tk()
root.title('Chat Bot')
root.geometry('400x500')
main_menu=Menu(root)

file_menu=Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='Save As..')
file_menu.add_command(label='Exit')

main_menu.add_cascade(label='False')
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)


chat=Text(root,bd=1,bg='black',width=50,height=8)
chat.place(x=6,y=6,height=305,width=370)


message=Text(root,bg='black',width=30,height=4)
message.place(x=128,y=400,height=88,width=260)
root.mainloop()
