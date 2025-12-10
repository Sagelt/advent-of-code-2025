import unittest
import sys
from itertools import combinations


class FloorAreaFinder(object):

  def __init__(self, lines: [str]):
    self.__parse_coordinates__(lines)
    self.__setup_floor__()

  def __parse_coordinates__(self, lines: [str]):
    self._red_tiles = []
    for line in lines:
      line = line[:-1].strip()
      numbers = line.split(",")
      self._red_tiles.append((int(numbers[0]), int(numbers[1])))

  def __setup_floor__(self):
    max_x = -1
    max_y = -1
    for tile in self._red_tiles:
      if tile[0] > max_x:
        max_x = tile[0]
      if tile[1] > max_y:
        max_y = tile[1]
    self._floor = []
    for y in range(0, max_y+2):
      self._floor.append(["."] * (max_x+2))
    
    previous_tile = self._red_tiles[0]
    self._floor[previous_tile[1]][previous_tile[0]] = "#"
    for tile in self._red_tiles[1:]:
      self._floor[tile[1]][tile[0]] = "#"
      self.__draw_line_between__(previous_tile, tile)
      previous_tile = tile
    self.__draw_line_between__(previous_tile, self._red_tiles[0])
    self.print_floor()

    for y in range(0, len(self._floor)):
      self.print_floor()
      transitions = []
      for x in range(0, len(self._floor[y])):
        if self._floor[y][x] in ["#", "O"] and self._floor[y][x+1] not in ["#", "O"]:
          transitions.append(x)
      for i in range(0, len(transitions), 2):
        if i+1 < len(transitions):
          for x in range(transitions[i]+1, transitions[i+1]):
            self._floor[y][x] = "O"
      

  def __draw_line_between__(self, previous_tile, tile):
    if tile[0] == previous_tile[0]:
      x = tile[0]
      min_y = min(tile[1], previous_tile[1])
      max_y = max(tile[1], previous_tile[1])
      for y in range(min_y+1, max_y):
        self._floor[y][x] = "O"
    elif tile[1] == previous_tile[1]:
      y = tile[1]
      min_x = min(tile[0], previous_tile[0])
      max_x = max(tile[0], previous_tile[0])
      for x in range(min_x+1, max_x):
        self._floor[y][x] = "O"
    else:
      raise ValueError("Tiles do not share row or column: %s, %s" % (tile, previous_tile))

  def build_all_possible_rectangles(self):
    result = []
    for pair in combinations(self._red_tiles, 2):
      min_y = min(pair[0][1], pair[1][1])
      max_y = max(pair[0][1], pair[1][1])
      min_x = min(pair[0][0], pair[1][0])
      max_x = max(pair[0][0], pair[1][0])
      filled = True
      for y in range(min_y, max_y):
        for x in range(min_x, max_x):
          if self._floor[y][x] not in ["#", "O"]:
            filled = False
            break
      if filled:
        print(pair)
        print(area(pair[0], pair[1]))
        result.append(area(pair[0], pair[1]))
    return result

  def find_largest_rectangle(self):
    areas = sorted(self.build_all_possible_rectangles())
    return areas[-1]

  def print_floor(self):
    for row in self._floor:
      print("".join(row))
    print()


def area(a, b):
  return (abs(a[0] - b[0])+1) * (abs(a[1] - b[1])+1)

class FloorAreaFinderTest(unittest.TestCase):

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
    f = FloorAreaFinder(sample_floor)
    self.assertEqual(f.find_largest_rectangle(), 24)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(find_largest_rectangle(lines))


