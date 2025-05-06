import json
from tkinter import END, MULTIPLE, Tk, Menu, filedialog, messagebox, Toplevel, Label, Entry, Button, PhotoImage, StringVar, OptionMenu, Listbox
from enum import Enum
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
  window.geometry("600x600")
  window.title("Editar configuración")
  cnt = 0
  entries = {}
  tag_listbox = None 
  for key, value in data.items():
    Label(window, text=str(key)+":").grid(row=cnt, column=0)
    if key == "filterTagsBy":
      var = StringVar(value=value)
      option_menu = OptionMenu(window, var, "OR", "AND")
      option_menu.grid(row=cnt, column=1)
      entries[key] = var 
    elif key == "tags":
      cnt += 1
      Label(window, text="Tags (selección múltiple):").grid(row=cnt, column=0, sticky="nw")
      tag_listbox = Listbox(window, selectmode=MULTIPLE, height=10, exportselection=False)
      tag_listbox.grid(row=cnt, column=1, sticky="w")

      all_tags = [tag.name for tag in Tags]
      selected_tags = [t.strip() for t in value.split(",")]

      for i, tag in enumerate(all_tags):
          tag_listbox.insert(END, tag)
          if tag in selected_tags:
              tag_listbox.selection_set(i)

      entries[key] = tag_listbox
    else:
      entry = Entry(window)
      entry.grid(row=cnt, column=1)
      entry.insert(0, value)
      entries[key] = entry
    cnt += 1

  def save_changes():
    try:
      for i, key in enumerate(data.keys()):
        if key == "filterTagsBy":
          data[key] = entries[key].get()
        elif key == "tags":
          selected_indices = entries[key].curselection()
          selected_tags = [entries[key].get(i) for i in selected_indices]
          data[key] = ",".join(selected_tags)
        else:
          data[key] = entries[key].get()  
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