import argparse
from helper import *
import json



def main():
  # Open and read the JSON file
  with open('data.json', 'r') as file:
    data = json.load(file)
    print(data['handle'], data['problems'], data['difficulty'])


if __name__ == "__main__":
  main()