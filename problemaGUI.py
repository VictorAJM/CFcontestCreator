import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk

class ProblemaGUI:
  
  def __init__(self, master, texto1, texto2, borde = 5, margen = 10, max_size=(50, 50)):
    self.master = master
    self.imagen_ruta = "assets/cf_logo.jpg"
    self.texto1 = texto1
    self.texto2 = texto2
    self.borde = borde
    self.margen = margen
    self.max_size = max_size

    self.img = Image.open(self.imagen_ruta)
    self.img = self.img.resize(self.max_size, Image.Resampling.LANCZOS)
    self.img_tk = ImageTk.PhotoImage(self.img)
    self.crear_widgets()

  def crear_widgets(self):
    self.frame = tk.Frame(self.master, bd=self.borde, padx=self.margen, pady=self.margen, relief="solid", bg="lightgrey")
    self.frame.pack(padx=self.margen, pady=self.margen, side=tk.LEFT, expand= True)

    img_label = tk.Label(self.frame, image=self.img_tk, bg="lightgrey")
    img_label.pack()

    text_label1 = tk.Label(self.frame, text=self.texto1, font=("Arial", 14), bg="lightgrey")
    text_label1.pack(pady=5)

    text_label2 = tk.Label(self.frame, text=self.texto2, font=("Arial", 14), bg="lightgrey")
    text_label2.pack(pady=5)

  def destroy(self):
    if self.frame:
      self.frame.destroy()  