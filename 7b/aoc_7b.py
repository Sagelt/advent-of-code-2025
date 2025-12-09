import unittest
import sys

def count_tachyon_manifold_paths(lines: [str]) -> int:
  start_point = lines[0].find("S")
  if start_point == -1:
    raise ValueError("No start point in first line")

  return trace_paths(lines[1:], start_point)

def trace_paths(lines: [str], current_column: int) -> int:
  if len(lines) == 1:
    return 1

  if lines[0][current_column] == "^":
    paths = 0
    if current_column > 0:
      paths += trace_paths(lines[1:], current_column - 1)
    if current_column < len(lines[0]) - 1:
      paths += trace_paths(lines[1:], current_column + 1)
    return paths
  
  return trace_paths(lines[1:], current_column)

class TestTachyonManifoldSplits(unittest.TestCase):

  def test_sample_case(self):
    sample_manifold = [
      ".......S.......\n",
      "...............\n",
      ".......^.......\n",
      "...............\n",
      "......^.^......\n",
      "...............\n",
      ".....^.^.^.....\n",
      "...............\n",
      "....^.^...^....\n",
      "...............\n",
      "...^.^...^.^...\n",
      "...............\n",
      "..^...^.....^..\n",
      "...............\n",
      ".^.^.^.^.^...^.\n",
      "...............\n",
    ]
    self.assertEqual(count_tachyon_manifold_paths(sample_manifold), 40)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(count_tachyon_manifold_paths(lines))


