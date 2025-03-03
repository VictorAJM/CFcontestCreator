from tkinter import *
from helper import *
from problemaGUI import ProblemaGUI

minutes = 120

def showGUI():
  root = Tk()
  root.title('Codeforces practica')
  root.geometry("900x720")
  photo = PhotoImage(file = "assets/logo.jpg")
  root.iconphoto(False, photo)

  menu = Menu(root)
  root.config(menu=menu)

  settings_menu = Menu(menu, tearoff=0)
  menu.add_cascade(label='Settings', menu=settings_menu)
  settings_menu.add_command(label='Open JSON', command=open_json)
  settings_menu.add_command(label='Edit JSON', command=edit_json)

  helpmenu = Menu(menu)
  menu.add_cascade(label='Help', menu=helpmenu)
  helpmenu.add_command(label='About')

  problema = ProblemaGUI(root, "assets/cf_logo.jpg", "Primera", "Segunda")
  problema1 = ProblemaGUI(root, "assets/cf_logo.jpg", "Primera", "Segunda")

  problema2 = ProblemaGUI(root, "assets/cf_logo.jpg", "Primera", "Segunda")
  problema3 = ProblemaGUI(root, "assets/cf_logo.jpg", "Primera", "Segunda")

  root.mainloop()