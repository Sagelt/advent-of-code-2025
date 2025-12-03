import unittest
import sys

def highest_joltage(battery_array: str, number_of_batteries: int) -> int:
  battery_charges = [int(c) for c in battery_array]
  remaining_batteries = number_of_batteries - 1

  if remaining_batteries == 0:
    return max(battery_charges)
  else:
    max_charge = max(battery_charges[:-remaining_batteries])
    max_charge_index = battery_charges.index(max_charge)
    additional_charge = highest_joltage(
      str(battery_array[max_charge_index+1:]), 
      remaining_batteries)
    return int(str(max_charge)+str(additional_charge))
  

class TestHighestJoltage(unittest.TestCase):

  def test_length_two_array(self):
    self.assertEqual(highest_joltage("21", 2), 21)
    self.assertEqual(highest_joltage("91", 2), 91)

  def test_sample_cases(self):
    self.assertEqual(highest_joltage("987654321111111", 12), 987654321111)
    self.assertEqual(highest_joltage("811111111111119", 12), 811111111119)
    self.assertEqual(highest_joltage("234234234234278", 12), 434234234278)
    self.assertEqual(highest_joltage("818181911112111", 12), 888911112111)



if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  total = 0
  filename = sys.argv[1]
  for battery_array in open(filename).readlines():
    total += highest_joltage(battery_array[:-1], 12)
  print(total)
