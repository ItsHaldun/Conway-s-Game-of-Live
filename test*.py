import unittest
import numpy.testing
import numpy as np
from Board import Board
from time import time


class StateTests(unittest.TestCase):
    state_shape = (4, 4)
    board = Board(shape=state_shape)

    def test_read_state(self):
        self.assertIsInstance(self.board.state, np.ndarray)

    def test_state_size(self):
        self.assertEqual(self.board.state.shape, self.state_shape)

    def test_next_state_still(self):
        correct_next_state = np.array([[1, 1, 0, 0],
                                       [1, 1, 0, 0],
                                       [0, 0, 0, 0],
                                       [0, 0, 0, 0]], dtype=np.uint8)

        self.board.state = np.array([[1, 1, 0, 0],
                                     [1, 1, 0, 0],
                                     [0, 0, 0, 0],
                                     [0, 0, 0, 0]], dtype=np.uint8)

        self.board.calculate_next_state()
        numpy.testing.assert_equal(self.board.state, correct_next_state)

    def test_next_state_line(self):
        correct_next_state = np.array([[0, 0, 0, 0],
                                       [0, 0, 0, 0],
                                       [0, 1, 1, 1],
                                       [0, 0, 0, 0]], dtype=np.uint8)

        self.board.state = np.array([[0, 0, 0, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 1, 0],
                                     [0, 0, 1, 0]], dtype=np.uint8)

        self.board.calculate_next_state()
        numpy.testing.assert_equal(self.board.state, correct_next_state)

    def test_next_state_glider(self):
        correct_next_state = np.array([[0, 0, 0, 0],
                                       [1, 0, 1, 0],
                                       [0, 1, 1, 0],
                                       [0, 1, 0, 0]], dtype=np.uint8)

        self.board.state = np.array([[0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [1, 1, 1, 0],
                                     [0, 0, 0, 0]], dtype=np.uint8)

        self.board.calculate_next_state()
        numpy.testing.assert_equal(self.board.state, correct_next_state)

    def test_next_state_twice(self):
        correct_next_state = np.array([[0, 0, 0, 0],
                                       [0, 0, 1, 0],
                                       [1, 0, 1, 0],
                                       [0, 1, 1, 0]], dtype=np.uint8)

        self.board.state = np.array([[0, 1, 0, 0],
                                     [0, 0, 1, 0],
                                     [1, 1, 1, 0],
                                     [0, 0, 0, 0]], dtype=np.uint8)

        self.board.calculate_next_state()
        self.board.calculate_next_state()
        numpy.testing.assert_equal(self.board.state, correct_next_state)

    def test_computation_time(self):
        state_shape = (1024, 1024)
        board = Board(shape=state_shape, init='random')

        start_time = time()
        board.calculate_next_state()
        end_time = time()

        self.assertLess((end_time - start_time)*1000, 120)


if __name__ == '__main__':
    unittest.main()
