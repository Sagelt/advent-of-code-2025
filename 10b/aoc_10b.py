import unittest
import sys
from itertools import combinations
import math


def find_fewest_button_presses(line: str) -> int:
	joltage_array = [int(x) for x in line.split("{")[1][:-1].split(",")]
	print("Original target array: %s" % str(joltage_array))
	repeats = math.gcd(*joltage_array)
	for i in range(len(joltage_array)):
		joltage_array[i] = joltage_array[i] // repeats
	print("Simplified target array: %s" % str(joltage_array))
	target = tuple(joltage_array)
	
	buttons = []
	incidence = [0] * len(target)
	for button in line.split()[1:-1]:
		button_effect = []
		for l in button[1:-1].split(","):
			i = int(l)
			incidence[i] += 1
			button_effect.append(i)
		buttons.append(button_effect)



	order_of_approach = []
	unique_incidences = sorted(set(incidence))
	print(incidence)
	for u in unique_incidences:
		order_of_approach.extend([i for i, x in enumerate(incidence) if x == u])

	print("Order of apprach: %s" % order_of_approach)

	presses = 0
	joltages = tuple([0 for _ in range(len(target))])
	states = dict()
	states[joltages] = 0
	print("Finding shortest way to get to %s with %s" % (target, buttons))

	already_solved = set()
	for i in order_of_approach:
		print("  Starting search for index %d: %d" % (i, target[i]))
		possible_buttons = []
		for button in buttons:
			if i in button and already_solved.isdisjoint(button):
				possible_buttons.append(button)

		print("  Trying buttons: %s" % possible_buttons)

		all_paths_found = False
		new_states = set(states.keys())
		while new_states:
			next_states = set()
			previous_states = list(new_states)
			for state in previous_states:
				for button in possible_buttons:
					new_state = apply_button_to_state(button, state, target)
					if new_state and new_state not in states.keys():
						next_states.add(new_state)
						states[new_state] = states[state] + 1
				print(" Found %d new states. Tracking %d states." % (len(new_states), len(states)))

			new_states = next_states

		if target in states.keys():
			break
		found_states = list(states.keys())
		print("  Found %d paths" % len(found_states))
		already_solved.add(i)
		for state in found_states:
			for x in already_solved:
				if state[x] != target[x]:
					del states[state]
		print("  Trimmed to %d paths" % len(states.keys()))

		already_solved.add(i)

	result = states[target]
	del states
	return result


def apply_button_to_state(button: [int], state: [int], target: [int]) -> [int]:
	next_state = list(state)
	for i in button:
		if state[i] >= target[i]:
			return None
		next_state[i] += 1
	return tuple(next_state)


class FewestButtonFinder(unittest.TestCase):

	def test_sample_1(self):
		sample_1 = "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}"
		self.assertEqual(find_fewest_button_presses(sample_1), 10)

	def test_sample_2(self):
		sample_2 = "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}"
		self.assertEqual(find_fewest_button_presses(sample_2), 12)

	def test_sample_3(self):
		sample_3 = "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"
		self.assertEqual(find_fewest_button_presses(sample_3), 11)

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
