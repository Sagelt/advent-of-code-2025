import unittest
import sys
from itertools import combinations


def find_largest_rectangle(lines: [str]) -> int:
  all_red_tiles = parse_coordinates(lines)
  all_rectangles = sorted(
    build_all_possible_rectangles(lines).items(), key=lambda item: item[1])
  return all_rectangles[-1][1]


def build_all_possible_rectangles(lines: [str]):
  red_tiles = parse_coordinates(lines)
  result = dict()
  for pair in combinations(red_tiles, 2):
    result[pair] = area(pair[0], pair[1])
  return result

def parse_coordinates(lines: [str]) -> [(int, int, int)]:
  result = []
  for line in lines:
    line = line[:-1].strip()
    numbers = line.split(",")
    result.append((int(numbers[0]), int(numbers[1])))
  return result

def area(a, b):
  return (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)

class SmallestCircuitFinder(unittest.TestCase):

  def test_sample_case(self):
    sample_floor = [
      "7,1\n",
      "11,1\n",
      "11,7\n",
      "9,7\n",
      "9,5\n",
      "2,5\n",
      "2,3\n",
      "7,3\n",
    ]
    self.assertEqual(find_largest_rectangle(sample_floor), 50)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(find_largest_rectangle(lines))


