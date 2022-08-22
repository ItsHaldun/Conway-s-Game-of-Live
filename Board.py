import numpy as np
from scipy import signal


class Board:
    def __init__(self, shape, init='empty'):
        if init == 'empty':
            self._state = np.zeros(shape, dtype=np.uint8)
        elif init == 'random':
            self._state = np.random.randint(0, 2, shape, dtype=np.uint8)

    def calculate_next_state(self):
        kernel = np.array([[1, 1, 1],
                           [1, 0, 1],
                           [1, 1, 1]], dtype=np.uint8)
        neighbor_matrix = signal.convolve(self.state, kernel, mode='same')

        # Rule 3: Every other cell are dead
        buffer = np.zeros_like(self.state, dtype=np.uint8)

        # Rule 1: Any live cell with two or three live neighbours survives
        buffer[np.logical_and(self.state == 1,
                              np.logical_or(neighbor_matrix == 2, neighbor_matrix == 3))] = 1

        # Rule 2: Any dead cell with three live neighbours becomes a live cell
        buffer[np.logical_and(self.state == 0, neighbor_matrix == 3)] = 1

        self.state = buffer

    def set_cell(self, location, value=0, reverse=False):
        if reverse:
            self._state[location] = 1-self._state[location]
        else:
            self._state[location] = value

    def reset(self):
        self._state = np.zeros_like(self.state, dtype=np.uint8)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, new_state):
        self._state = new_state
