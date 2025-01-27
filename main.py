import argparse
from helper import *

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--handle', type=str, help="Codeforces handle", required=True)
  parser.add_argument('--problems', type=int, help="Number of problems", required=True)
  parser.add_argument('--min', type=int, help="Minimum difficulty", required=True)
  parser.add_argument('--max', type=int, help="Maximum difficulty", required=True)
  args = parser.parse_args()

  print(args.handle, args.problems, args.min, args.max)


if __name__ == "__main__":
  main()