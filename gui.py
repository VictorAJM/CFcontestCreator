from tkinter import *
from helper import *
from api.helper import *
from problemaGUI import ProblemaGUI
import random
import os

minutes = 120
created_widgets = []

def restart_root():
    for widget in created_widgets:
        widget.destroy()
    created_widgets.clear()

    data = open_json()
    problems = getProblems(data['handle'], data['problems'], data['minimumRating'],data['maximumRating'], data['minimumSolvedCount'], data['maximumSolvedCount'])
    
    problems_frame = Frame(root)
    problems_frame.pack(pady=10)
    
    for idx, problem in enumerate(problems):

      problema = ProblemaGUI(master=problems_frame, texto1=problem[0], texto2=problem[1])
      created_widgets.append(problema)
      
      row = idx // 2 
      col = idx % 2  
      
      problema.frame.grid(row=row, column=col, padx=10, pady=10)

    return

def showGUI():
  global root
  root = Tk()
  root.title('Codeforces practica')
  root.geometry("1000x800")
  current_dir = os.path.dirname(os.path.abspath(__file__))
  logo_path = os.path.join(current_dir, "assets", "logo.jpg")

  photo = PhotoImage(file=logo_path)
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

