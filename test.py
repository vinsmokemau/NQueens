import unittest

from algorithm import NQueens


class TestNQueens(unittest.TestCase):
    def test_1_queen(self):
        self.assertEqual(NQueens(1).solutions, 1)

    def test_2_queen(self):
        self.assertEqual(NQueens(2).solutions, 0)

    def test_3_queen(self):
        self.assertEqual(NQueens(3).solutions, 0)

    def test_4_queen(self):
        self.assertEqual(NQueens(4).solutions, 2)

    def test_5_queen(self):
        self.assertEqual(NQueens(5).solutions, 10)

    def test_6_queen(self):
        self.assertEqual(NQueens(6).solutions, 4)

    def test_7_queen(self):
        self.assertEqual(NQueens(7).solutions, 40)

    def test_8_queen(self):
        self.assertEqual(NQueens(8).solutions, 92)
