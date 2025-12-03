import unittest
import sys

def is_invalid(product_id: str) -> bool:
  id_length = len(product_id)
  if id_length % 2 != 0:
    return False

  mid_point = id_length // 2
  first_half = product_id[:mid_point]
  second_half = product_id[mid_point:]
  if(first_half == second_half):
    return True
  return False

class TestValidProductIds(unittest.TestCase):

  def test_odd_length_ids(self):
    self.assertEqual(is_invalid("1"), False)
    self.assertEqual(is_invalid("101"), False)
    self.assertEqual(is_invalid("10001"), False)

  def test_invalid_ids(self):
    self.assertEqual(is_invalid("11"), True)
    self.assertEqual(is_invalid("22"), True)
    self.assertEqual(is_invalid("99"), True)
    self.assertEqual(is_invalid("1010"), True)
    self.assertEqual(is_invalid("1188511885"), True)


if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  total = 0
  filename = sys.argv[1]
  raw_ranges = open(filename).readline()
  for id_range in raw_ranges.split(","):
    id_range_ends = id_range.split("-")
    for product_id in range(int(id_range_ends[0]), int(id_range_ends[1])+1):
      if is_invalid(str(product_id)):
        total += product_id
  print(total)
