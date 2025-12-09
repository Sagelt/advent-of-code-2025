import unittest
import sys
from itertools import combinations
import operator
from functools import reduce
import math

def build_circuits_using_smallest_pairs(lines: [str], number_of_pairs: int) -> int:
  all_pairs_sorted = sorted(
    build_all_possible_connections(lines).items(), key=lambda item: item[1])
  shortest_pairs = all_pairs_sorted[:number_of_pairs]
  circuits = []
  for pair in [i[0] for i in shortest_pairs]:
    print("Processing %s" % str(pair))
    found_in_circuits = []
    for circuit in circuits:
      if pair[0] in circuit and pair[1] in circuit:
        print("  Already in the same circuit: %s" % circuit)
        found_in_circuits.append(circuit)
        break
      elif pair[0] in circuit or pair[1] in circuit:
        print("  Found in %s" % str(circuit))
        found_in_circuits.append(circuit)

    if len(found_in_circuits) > 2:
      raise ValueError("Found more then two circuits")
    elif len(found_in_circuits) == 2:
      print("  Merging circuits: %s" % str(found_in_circuits))
      new_circuit = set()
      for circuit in found_in_circuits:
        new_circuit |= circuit
        circuits.remove(circuit)

      circuits.append(new_circuit)
    elif len(found_in_circuits) == 1:
      found_in_circuits[0].add(pair[0])
      found_in_circuits[0].add(pair[1])
      print("  Extended circuit: %s" % str(found_in_circuits[0]))
    else:
      new_circuit = set(pair)
      print("  Creating new circuit: %s" % str(new_circuit))
      circuits.append(new_circuit)
  circuit_sizes = sorted([len(circuit) for circuit in circuits])
  return reduce(operator.mul, circuit_sizes[-3:], 1)


def build_all_possible_connections(lines: [str]):
  boxes = parse_coordinates(lines)
  result = dict()
  for pair in combinations(boxes, 2):
    result[pair] = distance_in_3space(pair[0], pair[1])
  return result

def parse_coordinates(lines: [str]) -> [(int, int, int)]:
  result = []
  for line in lines:
    line = line[:-1].strip()
    numbers = line.split(",")
    result.append((int(numbers[0]), int(numbers[1]), int(numbers[2])))
  return result

def distance_in_3space(a, b):
  return math.sqrt(((a[0]-b[0])**2) + ((a[1]-b[1])**2) + ((a[2]-b[2])**2))

class SmallestCircuitFinder(unittest.TestCase):

  def test_sample_case(self):
    sample_boxes = [
      "162,817,812\n",
      "57,618,57\n",
      "906,360,560\n",
      "592,479,940\n",
      "352,342,300\n",
      "466,668,158\n",
      "542,29,236\n",
      "431,825,988\n",
      "739,650,466\n",
      "52,470,668\n",
      "216,146,977\n",
      "819,987,18\n",
      "117,168,530\n",
      "805,96,715\n",
      "346,949,466\n",
      "970,615,88\n",
      "941,993,340\n",
      "862,61,35\n",
      "984,92,344\n",
      "425,690,689\n",
    ]
    print(build_circuits_using_smallest_pairs(sample_boxes, 10))
    #self.assertEqual(count_tachyon_manifold_paths(sample_manifold), 40)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  print(count_tachyon_manifold_paths(lines))


