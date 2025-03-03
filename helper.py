import json
from tkinter import Tk, Menu, filedialog, messagebox

JSON_PATH = 'data.json'

def open_json():
  try:
    data = None
    with open(JSON_PATH, 'r', encoding='utf-8') as file:
      data = json.load(file)
      messagebox.showinfo("JSON Content", json.dumps(data, indent=4))
  except Exception as e:
    messagebox.showerror("Error", f'Failed to open Json file: {e}')
  
def edit_json():
  try:
    with open(JSON_PATH, 'r+', encoding='utf-8') as file:
      data = json.load(file)
      #key = "new_key"
      #value = "new_value"
      #data[key] = value
      file.seek(0)
      json.dump(data, file, indent = 4)
      file.truncate()
      messagebox.showinfo("Success", f'Modified {key}: {value} to JSON file')
  except Exception as e:
    messagebox.showerror("Error", f'Failed to edit Json File: {e}') 