import numpy as np

BOARD_ROWS = 3
BOARD_COLS = 4
WIN_STATE = (0, 3)
LOSE_STATE = (1, 3)
START = (2, 0)
ACTIONS = ["up", "down", "left", "right"]


class Board:
    def __init__(self, state=START):
        self.board = np.zeros([BOARD_ROWS, BOARD_COLS])
        self.board[1, 1] = -1
        self.state = state
        self.is_end = False

    def give_reward(self):
        if self.state == WIN_STATE:
            return 1
        elif self.state == LOSE_STATE:
            return -1
        else:
            return 0

    def is_end_func(self):
        if (self.state == WIN_STATE) or (self.state == LOSE_STATE):
            self.is_end = True

    @staticmethod
    def _choose_action_prob(action):
        if action == "up":
            return np.random.choice(["up", "left", "right"], p=[0.8, 0.1, 0.1])
        if action == "down":
            return np.random.choice(["down", "left", "right"], p=[0.8, 0.1, 0.1])
        if action == "left":
            return np.random.choice(["left", "up", "down"], p=[0.8, 0.1, 0.1])
        if action == "right":
            return np.random.choice(["right", "up", "down"], p=[0.8, 0.1, 0.1])

    def nxt_position(self, action):
        """
        action: up, down, left, right
        -------------
        0 | 1 | 2| 3|
        1 |
        2 |
        return next position on board
        """
        if action == "up":
            nxt_state = (self.state[0] - 1, self.state[1])
        elif action == "down":
            nxt_state = (self.state[0] + 1, self.state[1])
        elif action == "left":
            nxt_state = (self.state[0], self.state[1] - 1)
        else:
            nxt_state = (self.state[0], self.state[1] + 1)

        # if next state is legal
        if (nxt_state[0] >= 0) and (nxt_state[0] <= 2):
            if (nxt_state[1] >= 0) and (nxt_state[1] <= 3):
                if nxt_state != (1, 1):
                    return nxt_state
        return self.state

    def show_board(self):
        self.board[self.state] = 1
        for i in range(0, BOARD_ROWS):
            print('-----------------')
            out = '| '
            for j in range(0, BOARD_COLS):
                if self.board[i, j] == 1:
                    token = '*'
                if self.board[i, j] == -1:
                    token = 'z'
                if self.board[i, j] == 0:
                    token = '0'
                out += token + ' | '
            print(out)
        print('-----------------')
