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
        self.assertEqual(advanceBoard(alive), set())

    def testAdvanceSingleCellBoard(self):
        board = set([Cell(0, 0)])
        expected = set()
        actual = advanceBoard(board)
        self.assertEqual(expected, actual)

    def testGenerateBoard(self):
        alive_string = 'X.\n.X'
        expected = set([Cell(0, 0), Cell(1, 1)])
        actual = generateBoard(alive_string)
        self.assertEqual(expected, actual)

    def testAdvanceBoard(self):
        board_string = '....\n.XXX\nXXX.'
        actual = generateBoard(board_string)
        expected_string = '..X.\nX..X\nX..X\n.X..'
        expected_0 = generateBoard(board_string)
        expected_1 = generateBoard(expected_string)
        for _ in range(3):
            self.assertEqual(expected_0, actual)
            actual = advanceBoard(actual)
            self.assertEqual(expected_1, actual)
            actual = advanceBoard(actual)

    def testToString(self):
        board_string = '..X.\n.XXX\nXXX.'
        board = generateBoard(board_string)
        self.assertEqual(boardToString(board), board_string)

if __name__ == '__main__':
    unittest.main()
