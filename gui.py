from tkinter import *
from helper import *
from api.helper import *
from problemaGUI import ProblemaGUI
import random

minutes = 120
created_widgets = []

def restart_root():
  for widget in created_widgets:
    widget.destroy()

  data = open_json()
  problems = getProblems(data['handle'], data['problems'], data['rating'])
  for problem in problems:
    problema = ProblemaGUI(master=root, texto1=problem[0], texto2=problem[1])
    created_widgets.append(problema)
  return

def showGUI():
  global root
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

  restart_button = Button(root, text="Generar problemas", command=restart_root)
  restart_button.pack(pady=20)

  root.mainloop()

