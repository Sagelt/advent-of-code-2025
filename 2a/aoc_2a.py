import unittest

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
  unittest.main()