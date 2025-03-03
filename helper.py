import json
from tkinter import Tk, Menu, filedialog, messagebox, Toplevel, Label, Entry, Button, PhotoImage

JSON_PATH = 'data.json'

def open_json():
  try:
    data = None
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
      data = json.load(file)
      messagebox.showinfo("JSON Content", json.dumps(data, indent=4))
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
  window.title("Editar configuración")

  Label(window, text="Handle:").grid(row=0, column=0)
  handle_entry = Entry(window)
  handle_entry.grid(row=0, column=1)
  handle_entry.insert(0, data.get("handle", ""))

  Label(window, text="Problems:").grid(row=1, column=0)
  problems_entry = Entry(window)
  problems_entry.grid(row=1, column=1)
  problems_entry.insert(0, str(data.get("problems", "")))
  
  Label(window, text="Rating:").grid(row=2, column=0)
  rating_entry = Entry(window)
  rating_entry.grid(row=2, column=1)
  rating_entry.insert(0, str(data.get("rating", "")))

  def save_changes():
    data["handle"] = handle_entry.get()
    data["problems"] = int(problems_entry.get())
    data["rating"] = int(rating_entry.get())
    save_json(data, window)
    
  Button(window, text="Save", command=save_changes).grid(row=3, column=0, columnspan=2)


def edit_json():
  try:
    with open(JSON_PATH, 'r+', encoding='utf-8') as file:
      data = json.load(file)
      edit_json_window(data)
  except Exception as e:
    messagebox.showerror("Error", f'Failed to edit Json File: {e}') 