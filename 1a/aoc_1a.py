import unittest

class ElfSafeDial(object):

  def __init__(self):
    self.__current_number__ = 50
    self.__times_at_zero__ = 0

  def __turn_left__(self, distance: int):
    new_number = self.__current_number__ - distance
    while new_number < 0:
      new_number = 100 + new_number
    self.__current_number__ = new_number

  def __turn_right__(self, distance: int):
    new_number = self.__current_number__ + distance
    while new_number > 99:
      new_number = new_number - 100
    self.__current_number__ = new_number

  def turn(self, instruction: str):
    direction = instruction[0]
    distance = int(instruction[1:])
    if direction == "L":
      self.__turn_left__(distance)
    elif direction == "R":
      self.__turn_right__(distance)
    else:
      raise ValueError("Unknow direction: " + direction)
    if self.__current_number__ == 0:
      self.__times_at_zero__ += 1

  @property
  def zero_count(self) -> int:
    return self.__times_at_zero__

  @property
  def current_number(self) -> int:
    return self.__current_number__

class TestElfSafeDial(unittest.TestCase):

  def test_default_state(self):
    dial = ElfSafeDial()
    self.assertEqual(dial.current_number, 50)
    self.assertEqual(dial.zero_count, 0)

  def test_turn_left(self):
    dial = ElfSafeDial()
    dial.turn("R1")
    self.assertEqual(dial.current_number, 51)
    self.assertEqual(dial.zero_count, 0)
    dial.turn("R10")
    self.assertEqual(dial.current_number, 61)
    self.assertEqual(dial.zero_count, 0)

  def test_turn_right(self):
    dial = ElfSafeDial()
    dial.turn("L1")
    self.assertEqual(dial.current_number, 49)
    self.assertEqual(dial.zero_count, 0)
    dial.turn("L10")
    self.assertEqual(dial.current_number, 39)
    self.assertEqual(dial.zero_count, 0)

  def test_turn_to_zero(self):
    dial = ElfSafeDial()
    dial.turn("L50")
    self.assertEqual(dial.current_number, 0)
    self.assertEqual(dial.zero_count, 1)
    dial.turn("R1")
    self.assertEqual(dial.current_number, 1)
    self.assertEqual(dial.zero_count, 1)

  def test_turn_to_zero_multiple_times(self):
    dial = ElfSafeDial()
    dial.turn("L50")
    self.assertEqual(dial.current_number, 0)
    self.assertEqual(dial.zero_count, 1)
    dial.turn("R1")
    self.assertEqual(dial.current_number, 1)
    self.assertEqual(dial.zero_count, 1)
    dial.turn("L1")
    self.assertEqual(dial.current_number, 0)
    self.assertEqual(dial.zero_count, 2)

  def test_underflow(self):
    dial = ElfSafeDial()
    dial.turn("L51")
    self.assertEqual(dial.current_number, 99)
    self.assertEqual(dial.zero_count, 0)

  def test_overflow(self):
    dial = ElfSafeDial()
    dial.turn("R51")
    self.assertEqual(dial.current_number, 1)
    self.assertEqual(dial.zero_count, 0)

  def test_full_rotation(self):
    dial = ElfSafeDial()
    dial.turn("L100")
    self.assertEqual(dial.current_number, 50)
    self.assertEqual(dial.zero_count, 0)
    dial.turn("R100")
    self.assertEqual(dial.current_number, 50)
    self.assertEqual(dial.zero_count, 0)
    dial.turn("L100")
    self.assertEqual(dial.current_number, 50)
    self.assertEqual(dial.zero_count, 0)

  def test_sample_solution(self):
    dial = ElfSafeDial()
    dial.turn("L68")
    self.assertEqual(dial.current_number, 82)
    dial.turn("L30")
    self.assertEqual(dial.current_number, 52)
    dial.turn("R48")
    self.assertEqual(dial.current_number, 0)
    dial.turn("L5")
    self.assertEqual(dial.current_number, 95)
    dial.turn("R60")
    self.assertEqual(dial.current_number, 55)
    dial.turn("L55")
    self.assertEqual(dial.current_number, 0)
    dial.turn("L1")
    self.assertEqual(dial.current_number, 99)
    dial.turn("L99")
    self.assertEqual(dial.current_number, 0)
    dial.turn("R14")
    self.assertEqual(dial.current_number, 14)
    dial.turn("L82")
    self.assertEqual(dial.current_number, 32)
    self.assertEqual(dial.zero_count, 3)


if __name__ == '__main__':
  unittest.main()
