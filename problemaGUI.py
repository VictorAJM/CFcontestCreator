import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
import webbrowser
import os

class ProblemaGUI:
  
  def __init__(self, master, texto1, texto2, filePath='', fileName = 'dummyText', borde = 5, margen = 10, max_size=(50, 50), row = 0, column = 0):
    self.master = master
    current_dir = os.path.dirname(os.path.abspath(__file__))
    logo_path = os.path.join(current_dir, "assets", "logo.jpg")
    self.fileName = fileName
    joined_path = os.path.join(current_dir, filePath, self.fileName + ".cpp")
    self.filePath = os.path.abspath(os.path.normpath(joined_path))
    self.imagen_ruta = logo_path
    
    self.template_path = os.path.join(current_dir, "template.cpp")
    with open(self.template_path, "r") as template_file:
        self.default_code = template_file.read()    
    
    self.texto1 = texto1
    self.texto2 = texto2
    self.borde = borde
    self.margen = margen
    self.max_size = max_size
    self.url = texto2
    self.row = row
    self.column = column

    self.img = Image.open(self.imagen_ruta)
    self.img = self.img.resize(self.max_size, Image.Resampling.LANCZOS)
    self.img_tk = ImageTk.PhotoImage(self.img)
    self.crear_widgets()

  def crear_widgets(self):
    self.frame = tk.Frame(self.master, bd=self.borde, padx=self.margen, pady=self.margen, relief="solid", bg="lightgrey")
    self.frame.grid(row=self.row, column=self.column, padx=self.margen, pady=self.margen)

    img_label = tk.Label(self.frame, image=self.img_tk, bg="lightgrey")
    img_label.grid(row=0, column=0, columnspan=2)

    text_label1 = tk.Label(self.frame, text=self.texto1, font=("Arial", 14), bg="lightgrey")
    text_label1.grid(row=1, column=0, columnspan=2, pady=5)

    text_label2 = tk.Label(self.frame, text=self.texto2, font=("Arial", 14), bg="lightgrey")
    text_label2.grid(row=2, column=0, columnspan=2, pady=5)

    self.frame.bind("<Enter>", self.resaltar)
    self.frame.bind("<Leave>", self.restaurar_color)
    self.frame.bind("<Button-1>", self.abrir_pagina)


  def resaltar(self, event):
    self.frame.config(bg="lightblue")

  def restaurar_color(self, event):
    self.frame.config(bg="lightgrey")

  def abrir_pagina(self, event):
  
    os.makedirs(os.path.dirname(self.filePath), exist_ok=True)
    if not os.path.exists(self.filePath):
        with open(self.filePath, "w") as f:
            f.write(self.default_code)  
    
    webbrowser.open(self.url)

  def destroy(self):
    if self.frame:
      self.frame.destroy()  