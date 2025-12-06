import unittest
import sys
import operator
from functools import reduce


def build_math_problems_and_solve(lines: [str]) -> int:
  operations = lines[-1].split()
  operand_columns = lines[:-1]
  equations = []
  for i in range(0, len(operand_columns[0].strip().split())):
    equations.append([])
  for operand_list in operand_columns:
    operands = operand_list.strip().split()
    for i in range(0, len(operands)):
      if operands[i] != "\n":
        equations[i].append(int(operands[i]))

  print(equations)
  print(operations)
  total = 0
  for i in range(0, len(equations)):
    if operations[i] == "+":
      total += reduce(operator.add, equations[i], 0)
    elif operations[i] == "*":
      total += reduce(operator.mul, equations[i], 1)
  return total

class TestMath(unittest.TestCase):

  def test_sample_case(self):
    sample_math = [
      "123 328  51 64 ",
      "45 64  387 23 ",
      "6 98  215 314",
      "*   +   *   + ",
    ]
    self.assertEqual(build_math_problems_and_solve(sample_math), 4277556)

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


