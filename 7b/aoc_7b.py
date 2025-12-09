import unittest
import sys

def count_tachyon_manifold_paths(lines: [str]) -> int:
  start_point = lines[0].find("S")
  if start_point == -1:
    raise ValueError("No start point in first line")
  beam_locations = {start_point: 1}

  for line in lines[1:-1]:
    next_beam_locations = dict()
    for location in beam_locations.keys():
      if line[location] == "^":
        if location > 0:
          next_beam_locations[location-1] = next_beam_locations.get(location-1, 0) + beam_locations.get(location)
        if location < len(line)-1:
          next_beam_locations[location+1] = next_beam_locations.get(location+1, 0) + beam_locations.get(location)
      else:
        next_beam_locations[location] = next_beam_locations.get(location, 0) + beam_locations.get(location)
    beam_locations = next_beam_locations

  return sum(beam_locations.values())

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


