import unittest
from adventofcode.advent2019.day16.solution import solution

class TestSolution(unittest.TestCase):
    def test_results(self):
        self.assertEqual(solution("12345678", 1), "48226158")
        self.assertEqual(solution("12345678", 2), "34040438")
        self.assertEqual(solution("12345678", 3), "03415518")
        self.assertEqual(solution("12345678", 4), "01029498")
        self.assertEqual(solution("80871224585914546619083218645595", 100), "24176176")
        self.assertEqual(solution("19617804207202209144916044189917", 100), "73745418")
        self.assertEqual(solution("69317163492948606335995924319873", 100), "52432133")
        # part 2
        self.assertEqual(solution("03036732577212944063491565474664", 100, True), "84462026")
        self.assertEqual(solution("02935109699940807407585447034323", 100, True), "78725270")
        self.assertEqual(solution("03081770884921959731165446850517", 100, True), "53553731")