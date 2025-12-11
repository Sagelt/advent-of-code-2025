import unittest
import sys

class NodeInfo(object):

	def __init__(self):
		self.paths_to_out = 0
		self.paths_to_dac = 0
		self.paths_to_fft = 0
		self.paths_to_all = 0

	def __str__(self):
		return ",".join([
			str(self.paths_to_out),
			str(self.paths_to_dac),
			str(self.paths_to_fft),
			str(self.paths_to_all),
			])

class ElfServer(object):

	def __init__(self, lines: [str]):
		self._forward_connections = dict()
		self._backwards_connections = dict()
		self._ignorable_nodes = set()
		for line in lines:
			(origin, destinations) = line[:-1].split(":")
			for destination in destinations.strip().split():
				self.add_connection(origin, destination)


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
		node_info = dict()
		node_info["out"] = NodeInfo()
		node_info["out"].paths_to_out = 1
		nodes_to_visit = ["out"]
		visited = set()

		while len(nodes_to_visit) > 0:
			# print(nodes_to_visit)
			node = nodes_to_visit.pop(0)
			all_children_visited = True
			for child in self._forward_connections[node]:
				if child not in visited:
					all_children_visited = False
			if not all_children_visited:
				nodes_to_visit.append(node)
				continue


			visited.add(node)
			info = node_info[node]
			if node == "dac":
				info.paths_to_all = info.paths_to_fft
				info.paths_to_dac = info.paths_to_out
			elif node == "fft":
				info.paths_to_all = info.paths_to_dac
				info.paths_to_fft = info.paths_to_out


			print("Visiting %s, info: %s" % (node, info))
			for next_node in self._backwards_connections[node]:
				if next_node not in node_info.keys():
					node_info[next_node] = NodeInfo()
				next_info = node_info[next_node]
				next_info.paths_to_out += info.paths_to_out
				next_info.paths_to_dac += info.paths_to_dac
				next_info.paths_to_fft += info.paths_to_fft
				next_info.paths_to_all += info.paths_to_all
				if next_node not in nodes_to_visit and next_node not in visited:
					nodes_to_visit.append(next_node)

		
		return node_info["svr"].paths_to_all

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
