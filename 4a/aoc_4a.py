import unittest
import sys


class WrappingPaperFloor(object):

  def __init__(self, loading_diagram: [str]):
    self.__floor__ = []
    for line in loading_diagram:
      floor_row = []
      for position in line:
        if position == '@':
          floor_row.append(1)
        else:
          floor_row.append(0)
      self.__floor__.append(floor_row)

  def count_movable_paper(self) -> int:
    total = 0
    for y in range(0, len(self.__floor__)):
      for x in range(0, len(self.__floor__[y])):
        if self.__floor__[y][x] == 1:
          total += self.can_be_moved(x, y)
    return total

  def can_be_moved(self, x: int, y: int) -> int:
    if self.sum_of_neighbors(x, y) < 4:
      return 1
    else:
      return 0

  def sum_of_neighbors(self, x: int, y: int) -> int:
    total = 0
    directions = [-1, 0, 1]
    for dX in directions:
      for dY in directions:
        if dX == 0 and dY == 0:
          continue
        total += self.paper_at_coordinates(x + dX, y + dY)
    return total

  def paper_at_coordinates(self, x: int, y: int) -> int:
    if y < 0 or y > len(self.__floor__)-1:
      return 0

    # Y coordinate is valid if we're here
    if x < 0 or x > len(self.__floor__[y])-1:
      return 0

    # If we're here both X and Y are valid
    return self.__floor__[y][x]
  

class TestWrappingPaperFloor(unittest.TestCase):

  def test_sample_case(self):
    sample_case = [
      "..@@.@@@@.",
      "@@@.@.@.@@",
      "@@@@@.@.@@",
      "@.@@@@..@.",
      "@@.@@@@.@@",
      ".@@@@@@@.@",
      ".@.@.@.@@@",
      "@.@@@.@@@@",
      ".@@@@@@@@.",
      "@.@.@@@.@.",
    ]
    test_floor = WrappingPaperFloor(sample_case)
    self.assertEqual(test_floor.count_movable_paper(), 13)



if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  floor = WrappingPaperFloor(open(filename).readlines())
  print(floor.count_movable_paper())
