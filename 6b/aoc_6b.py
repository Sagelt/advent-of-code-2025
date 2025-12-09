import unittest
import sys
import operator
from functools import reduce


def build_math_problems_and_solve(lines: [str]) -> int:
  operation = None
  total = 0
  operands = []
  for i in range(0, len(lines[0])):
    if is_column_empty(lines, i):
      total += resolve_equation(operation, operands)
      operation = None
      operands = []
    else:
      if lines[-1][i] != " ":
        # Found an operation
        operation = lines[-1][i]
      operands.append(column_to_number(lines[:-1], i))

  return total

def resolve_equation(operation: str, operands: [int]) -> int:
  if operation == "+":
    print(" + ".join(str(o) for o in operands))
    return reduce(operator.add, operands, 0)
  elif operation == "*":
    print(" * ".join(str(o) for o in operands))
    return reduce(operator.mul, operands, 1)
  else:
    raise NotImplementedError("Unsupported operation: %s" % operation)

def column_to_number(lines: [str], column: int) -> int:
  column_as_string = ""
  for line in lines:
    column_as_string += line[column]

  result = int(column_as_string.strip())
  return result

def is_column_empty(lines: [str], column: int) -> bool:
  for line in lines:
    if line[column] not in [" ", "\n"]:
      return False
  return True

class TestMath(unittest.TestCase):

  def test_sample_case(self):
    sample_math = [
      "123 328  51 64 \n",
      " 45 64  387 23 \n",
      "  6 98  215 314\n",
      "*   +   *   +  \n",
    ]
    self.assertEqual(build_math_problems_and_solve(sample_math), 3263827)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(build_math_problems_and_solve(lines))


