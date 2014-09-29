from game_of_life import (
    Cell, getNeighbours,
    getNeighbourCount, generateBoard,
    advanceBoard, boardToString)
import unittest


class GameOfLifeTest(unittest.TestCase):
    def testNeighbours(self):
        cell = Cell(1, 1)
        expected = set([
            Cell(0, 0), Cell(0, 1), Cell(0, 2),
            Cell(1, 0), Cell(1, 2), Cell(2, 0),
            Cell(2, 1), Cell(2, 2)])
        actual = set(getNeighbours(cell))
        self.assertEqual(expected, actual)

    def testNeighbourCount(self):
        alive = set([Cell(0, 0), Cell(1, 1)])
        expected = {
            Cell(-1, -1): 1,
            Cell(0, -1): 1,
            Cell(1, -1): 1,
            Cell(-1, 0): 1,
            Cell(0, 0): 1,
            Cell(1, 0): 2,
            Cell(2, 0): 1,
            Cell(-1, 1): 1,
            Cell(0, 1): 2,
            Cell(1, 1): 1,
            Cell(2, 1): 1,
            Cell(0, 2): 1,
            Cell(1, 2): 1,
            Cell(2, 2): 1,
        }
        actual = getNeighbourCount(alive)
        self.assertEqual(expected, actual)

    def testAdvanceEmptyBoard(self):
        alive = set()
        self.assertEqual(alive, set(advanceBoard(alive)))

    def testAdvanceSingleCellBoard(self):
        board = set([Cell(0, 0)])
        expected = set()
        actual = set(advanceBoard(board))
        self.assertEqual(expected, actual)

    def testGenerateBoard(self):
        alive_string = 'X.\n.X'
        expected = set([Cell(0, 0), Cell(1, 1)])
        actual = set(generateBoard(alive_string))
        self.assertEqual(expected, actual)

    def testAdvanceBoard(self):
        board_string = '....\n.XXX\nXXX.'
        actual = set(generateBoard(board_string))
        expected_string = '..X.\nX..X\nX..X\n.X..'
        expected_0 = set(generateBoard(board_string))
        expected_1 = set(generateBoard(expected_string))
        for _ in range(3):
            self.assertEqual(expected_0, actual)
            actual = set(advanceBoard(actual))
            self.assertEqual(expected_1, actual)
            actual = set(advanceBoard(actual))

    def testToString(self):
        board_string = '..X.\n.XXX\nXXX.'
        board = set(generateBoard(board_string))
        self.assertEquals(boardToString(board), board_string)
