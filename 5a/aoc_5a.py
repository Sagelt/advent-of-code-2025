import unittest
import sys


class IngredientDatabase(object):

  def __init__(self, fresh_ranges: [(int, int)]):
    self.__fresh_ranges__ = fresh_ranges

  def is_fresh(self, ingredient: int) -> bool:
    for r in self.__fresh_ranges__:
      if ingredient in range(r[0], r[1]+1):
        return True
    return False
  

class TestIngredientDatabase(unittest.TestCase):

  def test_sample_case(self):
    sample_fresh_ranges = [
      (3, 5),
      (10, 14),
      (16, 20),
      (12, 18),
    ]
    test_databse = IngredientDatabase(sample_fresh_ranges)
    self.assertEqual(test_databse.is_fresh(1), False)
    self.assertEqual(test_databse.is_fresh(5), True)
    self.assertEqual(test_databse.is_fresh(8), False)
    self.assertEqual(test_databse.is_fresh(11), True)
    self.assertEqual(test_databse.is_fresh(17), True)
    self.assertEqual(test_databse.is_fresh(32), False)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
