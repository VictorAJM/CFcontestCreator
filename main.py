import argparse
from helper import *

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--handle', type=str, help="Codeforces handle", required=True)
  args = parser.parse_args()

  print(averageRatingSolvedProblems(args.handle))


if __name__ == "__main__":
  main()