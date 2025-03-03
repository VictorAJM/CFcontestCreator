import argparse
from helper import *
import json
from gui import *


def main():
  # Open and read the JSON file
  data = None
  with open('data.json', 'r') as file:
    data = json.load(file)
  print(data['handle'], data['problems'], data['rating'])
  #getProblems(data['handle'], data['problems'], data['rating'])
  showGUI()

if __name__ == "__main__":
  main()