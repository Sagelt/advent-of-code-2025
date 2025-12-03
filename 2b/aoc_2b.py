import unittest
import sys
import numpy

def is_invalid(product_id: str) -> bool:
  if len(product_id) == 1:
    return False

  if len(set(product_id)) == 1:
    return True

  for repeat_length in range(2, (len(product_id)//2) +1):
    if has_repeat_of_length(product_id, repeat_length):
      return True
  return False

def has_repeat_of_length(product_id: str, length: int) -> bool:
  id_length = len(product_id)
  if id_length % length != 0:
    return False

  parts = [product_id[i:i + length] for i in range(0, len(product_id), length)]
  return len(set(parts)) == 1



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
    self.assertEqual(is_invalid("111"), True)
    self.assertEqual(is_invalid("999"), True)
    self.assertEqual(is_invalid("222222"), True)
    self.assertEqual(is_invalid("565656"), True)
    self.assertEqual(is_invalid("824824824"), True)


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
