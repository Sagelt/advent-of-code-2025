import unittest
import sys

def highest_joltage(battery_array: str) -> int:
  battery_charges = [int(c) for c in battery_array]
  max_charge = max(battery_charges)
  index_of_max_charge = battery_charges.index(max_charge)
  if index_of_max_charge == len(battery_charges) - 1:
    second_charge = max(battery_charges[:-1])
    return (second_charge * 10) + max_charge
  else:
    second_charge = max(battery_charges[index_of_max_charge+1:])
    return (max_charge * 10) + second_charge
  

class TestHighestJoltage(unittest.TestCase):

  def test_length_two_array(self):
    self.assertEqual(highest_joltage("21"), 21)
    self.assertEqual(highest_joltage("91"), 91)

  def test_sample_cases(self):
    self.assertEqual(highest_joltage("987654321111111"), 98)
    self.assertEqual(highest_joltage("811111111111119"), 89)
    self.assertEqual(highest_joltage("234234234234278"), 78)
    self.assertEqual(highest_joltage("818181911112111"), 92)



if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()
