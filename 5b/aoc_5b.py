import unittest
import sys


def count_in_ranges(ranges: [(int, int)]) -> int:
  sorted_ranges = sorted(ranges, key=lambda r: r[0])
  for r in sorted_ranges:
    print(r)
  i = 0
  total = 0
  start = -1
  end = -2
  while i < len(sorted_ranges):
    if sorted_ranges[i][0] > end:
      # The new interval does not overlap
      # Close the previous interval
      total += (end+1 - start)
      print("Ending range at %d" % end)
      print("Total is %d" % total)

      # Start a new interval
      start = sorted_ranges[i][0]
      end = sorted_ranges[i][1]
      print("Starting new range at %d" % start)
    else:
      # The new interval overlaps
      if sorted_ranges[i][1] > end:
        end = sorted_ranges[i][1]
        print("Overlapping rage to %d" % end)
      else:
        print("New range is within previous range")
    i += 1
  total += (end+1 - start)
  print("Total is %d" % total)
  return total

  

class TestIngredientDatabase(unittest.TestCase):

  def test_sample_case(self):
    sample_fresh_ranges = [
      (3, 5),
      (10, 14),
      (16, 20),
      (12, 18),
    ]
    self.assertEqual(count_in_ranges(sample_fresh_ranges), 14)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  ranges = []
  for line in open(filename).readlines():
    if "-" in line:
      ends = line[:-1].split("-")
      ranges.append((int(ends[0]), int(ends[1])))

  print(count_in_ranges(ranges))


