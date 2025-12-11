import unittest
import sys


class ElfServer(object):

	def __init__(self, lines: [str]):
		self._forward_connections = dict()
		self._backwards_connections = dict()
		self._ignorable_nodes = set()
		for line in lines:
			(origin, destinations) = line[:-1].split(":")
			for destination in destinations.strip().split():
				self.add_connection(origin, destination)

		self._can_reach_dac = self._find_nodes_that_can_reach("dac")
		self._can_reach_fft = self._find_nodes_that_can_reach("fft")
		self._can_reach_out = self._find_nodes_that_can_reach("out")
		

	def _find_nodes_that_can_reach(self, target):
		print("Findinf nodes that can reach %s" % target)
		can_reach_out = set()
		nodes_to_visit = [target]
		while len(nodes_to_visit) > 0:
			node = nodes_to_visit.pop()
			print("%s can reach %s" % (node, target))
			can_reach_out.add(node)
			for next_node in self._backwards_connections[node]:
				if next_node not in can_reach_out:
					nodes_to_visit.append(next_node)

		return can_reach_out


	def add_connection(self, origin, destination):
		if destination not in self._forward_connections.keys():
			self._forward_connections[destination] = set()
		if origin not in self._forward_connections.keys():
			self._forward_connections[origin] = set()

		self._forward_connections[origin].add(destination)

		if destination not in self._backwards_connections.keys():
			self._backwards_connections[destination] = set()
		if origin not in self._backwards_connections.keys():
			self._backwards_connections[origin] = set()

		self._backwards_connections[destination].add(origin)

	def count_all_paths_containing_dac_and_fft(self):
		print("Finding dac paths")
		paths_dac = self._extend_paths_to([tuple(["svr"])], "dac", ["fft", "out"], self._can_reach_dac)
		print("Finding dac->fft paths")
		paths_dac_fft = self._extend_paths_to(list(paths_dac), "fft", ["out"], self._can_reach_fft)


		print("Finding fft paths")
		paths_fft = self._extend_paths_to([tuple(["svr"])], "fft", ["dac", "out"], self._can_reach_fft)
		print("Finding fft->dac paths")
		paths_fft_dac = self._extend_paths_to(list(paths_fft), "dac", ["out"], self._can_reach_dac)

		base_paths = paths_dac_fft ^ paths_fft_dac

		print("Extending paths to out")
		exit_paths = self._extend_paths_to(list(base_paths), "out", [], self._can_reach_out)

		return len(exit_paths)

	def _extend_paths_to(self, current_paths, target, avoid, possible_nodes):
		pending_paths = list(current_paths)
		valid_paths = set()

		connections = self._forward_connections

		while len(pending_paths) > 0:
			path_to_extend = pending_paths.pop()
			node_to_extend = path_to_extend[-1]

			for next_node in connections[node_to_extend]:
				if next_node in avoid:
					continue
				if next_node not in possible_nodes:
					print("Skipping %s which cannot reach %s" % (next_node, target))
					continue
				possible_path = tuple(list(path_to_extend) + [next_node])
				print(possible_path)

				if next_node == target:
					valid_paths.add(possible_path)
				else:
					pending_paths.append(possible_path)

		return valid_paths



class ElfServerTest(unittest.TestCase):

	def test_sample_1case(self):
		sample_case = [
			"svr: aaa bbb\n",
			"aaa: fft\n",
			"fft: ccc\n",
			"bbb: tty\n",
			"tty: ccc\n",
			"ccc: ddd eee\n",
			"ddd: hub\n",
			"hub: fff\n",
			"eee: dac\n",
			"dac: fff\n",
			"fff: ggg hhh\n",
			"ggg: out\n",
			"hhh: out\n",
		]
		e = ElfServer(sample_case)
		self.assertEqual(e.count_all_paths_containing_dac_and_fft(), 2)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  e = ElfServer(lines)
  print(e.count_all_paths_containing_dac_and_fft())
