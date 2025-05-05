import json
from tkinter import Tk, Menu, filedialog, messagebox, Toplevel, Label, Entry, Button, PhotoImage

from exceptions.invalidJsonData import InvalidJsonDataError
from api.tags import Tags

JSON_PATH = 'data.json'

def validate_json_data(data):
  rawTags = data["tags"] if "tags" in data else ""
  rawTags = rawTags.split(',')
  rawTags = [tag.strip().upper() for tag in rawTags]
  for tag in rawTags:
    if tag not in Tags.__members__:
      raise InvalidJsonDataError(f"{tag} is not a valid tag in Tags")
    
  if data["filterTagsBy"] not in ["OR", "AND"]:
    raise InvalidJsonDataError(f"filterTags is not OR or AND")

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
      try:
          for i, key in enumerate(data.keys()):
              data[key] = entries[i].get()
          validate_json_data(data)
          save_json(data, window)
      except InvalidJsonDataError as ve:
          messagebox.showerror("Validation Error", str(ve))
      except Exception as e:
          messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")

    
  Button(window, text="Save", command=save_changes).grid(row=cnt, column=0, columnspan=2)


def edit_json():
  try:
    with open(JSON_PATH, 'r+', encoding='utf-8') as file:
      data = json.load(file)
      edit_json_window(data)
  except Exception as e:
    messagebox.showerror("Error", f'Failed to edit Json File: {e}') 