import json
from tkinter import Tk, Menu, filedialog, messagebox, Toplevel, Label, Entry, Button, PhotoImage

JSON_PATH = 'data.json'

def open_json():
  try:
    data = None
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
      data = json.load(file)
      return data
  except Exception as e:
    messagebox.showerror("Error", f'Failed to open Json file: {e}')

def save_json(data, window):
  try:
    with open(JSON_PATH, 'w', encoding='utf-8') as file:
      json.dump(data, file, indent=4)
      messagebox.showinfo("Success", "JSON file updated successfully.")
      window.destroy()
  except Exception as e:
    messagebox.showerror("Error", f'Failed to save JSON file: {e}')
  
def edit_json_window(data):
  window = Toplevel()
  window.geometry("400x300")
  window.title("Editar configuración")
  cnt = 0
  entries = []
  for key, value in data.items():
    
    Label(window, text=str(key)+":").grid(row=cnt, column=0)
    entries.append(Entry(window))
    entries[-1].grid(row=cnt, column=1)
    entries[-1].insert(0, value)
    cnt += 1

  def save_changes():
    cnt = 0
    for key, value in data.items():
      data[key] = entries[cnt].get()
      cnt += 1
    save_json(data, window)
    
  Button(window, text="Save", command=save_changes).grid(row=cnt, column=0, columnspan=2)


def edit_json():
  try:
    with open(JSON_PATH, 'r+', encoding='utf-8') as file:
      data = json.load(file)
      edit_json_window(data)
  except Exception as e:
    messagebox.showerror("Error", f'Failed to edit Json File: {e}') 