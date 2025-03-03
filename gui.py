from tkinter import *
from helper import *

minutes = 120

def showGUI():
  root = Tk()
  root.title('Codeforces practica')

  menu = Menu(root)
  root.config(menu=menu)

  settings_menu = Menu(menu, tearoff=0)
  menu.add_cascade(label='Settings', menu=settings_menu)
  settings_menu.add_command(label='Open JSON', command=open_json)
  settings_menu.add_command(label='Edit JSON', command=edit_json)

  helpmenu = Menu(menu)
  menu.add_cascade(label='Help', menu=helpmenu)
  helpmenu.add_command(label='About')

  root.mainloop()