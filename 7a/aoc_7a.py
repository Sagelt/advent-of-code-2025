import unittest
import sys

def count_tachyon_manifold_splits(lines: [str]) -> int:
  start_point = lines[0].find("S")
  if start_point == -1:
    raise ValueError("No start point in first line")
  beam_locations = set([start_point])
  splits = 0

  for line in lines[1:]:
    next_beam_locations = set()
    for location in beam_locations:
      if line[location] == "^":
        splits += 1
        next_beam_locations.add(location+1)
        next_beam_locations.add(location-1)
      else:
        next_beam_locations.add(location)
    beam_locations = next_beam_locations

  return splits

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
    self.assertEqual(count_tachyon_manifold_splits(sample_manifold), 21)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(count_tachyon_manifold_splits(lines))


