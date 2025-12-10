import unittest
import sys
from itertools import combinations

def find_fewest_button_presses(line: str) -> int:
	light_array = []
	for light in line.split("]")[0][1:]:
		if light == ".":
			light_array.append(False)
		elif light == "#":
			light_array.append(True)
	target = tuple(light_array)
	
	buttons = []
	for button in line.split()[1:-1]:
		button_effect = []
		for l in button[1:-1].split(","):
			button_effect.append(int(l))
		buttons.append(button_effect)

	presses = 0
	lights = tuple([False for _ in range(len(target))])
	possible_states = set()
	possible_states.add(lights)
	while target not in possible_states:
		next_states = set()
		for state in possible_states:
			for button in buttons:
				next_states.add(apply_button_to_state(button, state))
		possible_states = next_states
		presses += 1

	return presses


def apply_button_to_state(button: [int], state: [bool]) -> [bool]:
	next_state = list(state)
	for light in button:
		next_state[light] = not next_state[light]
	return tuple(next_state)




class FewestButtonFinder(unittest.TestCase):

	def test_sample_1(self):
		sample_1 = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
		self.assertEqual(find_fewest_button_presses(sample_1), 2)

	def test_sample_2(self):
		sample_2 = "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
		self.assertEqual(find_fewest_button_presses(sample_2), 3)

	def test_sample_3(self):
		sample_3 = "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
		self.assertEqual(find_fewest_button_presses(sample_3), 2)

if __name__ == '__main__':
  # If no file name is provided, unit test and exit
  if len(sys.argv) == 1:
    unittest.main()
    sys.exit()

  # At this point we have a file to parse
  filename = sys.argv[1]
  lines = open(filename).readlines()
  presses = 0
  for line in lines:
  	presses += find_fewest_button_presses(line[:-1])
  print(presses)
