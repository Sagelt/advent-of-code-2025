import unittest
import sys


class ElfServer(object):

	def __init__(self, lines: [str]):
		self._connections = dict()
		for line in lines:
			(origin, destinations) = line[:-1].split(":")
			for destination in destinations.strip().split():
				self.add_connection(origin, destination)

		print(self._connections)

	def add_connection(self, origin, destination):
		if origin not in self._connections.keys():
			self._connections[origin] = set()

		self._connections[origin].add(destination)

	def count_all_paths(self):
		found_paths = set()
		pending_paths = [tuple(["you"])]
		valid_paths = set()

		while len(pending_paths) > 0:
			path_to_extend = pending_paths.pop()
			node_to_extend = path_to_extend[-1]

			for next_node in self._connections[node_to_extend]:
				possible_path = tuple(list(path_to_extend) + [next_node])
				print(possible_path)
				if possible_path in found_paths:
					continue
				elif next_node == "out":
					valid_paths.add(possible_path)
					found_paths.add(possible_path)
				else:
					found_paths.add(possible_path)
					pending_paths.append(possible_path)

		return len(valid_paths)


class ElfServerTest(unittest.TestCase):

	def test_sample_1case(self):
		sample_case = [
			"aaa: you hhh\n",
			"you: bbb ccc\n",
			"bbb: ddd eee\n",
			"ccc: ddd eee fff\n",
			"ddd: ggg\n",
			"eee: out\n",
			"fff: out\n",
			"ggg: out\n",
			"hhh: ccc fff iii\n",
			"iii: out\n",
		]
		e = ElfServer(sample_case)
		self.assertEqual(e.count_all_paths(), 5)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  e = ElfServer(lines)
  print(e.count_all_paths())
