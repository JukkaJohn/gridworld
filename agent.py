import numpy as np

from board import BOARD_ROWS, BOARD_COLS, Board, ACTIONS


class Agent:

    def __init__(self, ):
        self.states = []  # record position and action taken at the position
        self.actions = ACTIONS
        self.board = Board()
        self.isEnd = self.board.is_end
        self.lr = 0.2
        self.exploration_rate = 0.1
        self.decay_gamma = 0.9

        # initial Q values
        self.q_values = {}
        for i in range(BOARD_ROWS):
            for j in range(BOARD_COLS):
                self.q_values[(i, j)] = {}
                for a in self.actions:
                    self.q_values[(i, j)][a] = 0  # Q value is a dict of dict

    def choose_action(self):
        # choose action with most expected value
        mx_nxt_reward = -10
        action = ''

        if np.random.uniform(0, 1) <= self.exploration_rate:
            action = np.random.choice(self.actions)
        else:
            # greedy action
            for a in self.actions:
                current_position = self.board.state
                nxt_reward = self.q_values[current_position][a]
                if nxt_reward >= mx_nxt_reward:
                    action = a
                    mx_nxt_reward = nxt_reward
            # print("current pos: {}, greedy action: {}".format(self.State.state, action))
        return action

    def take_action(self, action):
        position = self.board.nxt_position(action)
        return Board(state=position)

    def reset(self):
        self.states = []
        self.board = Board()
        self.isEnd = self.board.is_end

    def play(self, rounds=10):
        i = 0
        while i < rounds:
            # to the end of game back propagate reward
            if self.board.is_end:
                # back propagate
                reward = self.board.give_reward()
                for a in self.actions:
                    self.q_values[self.board.state][a] = reward
                print("Game End Reward", reward)
                for s in reversed(self.states):
                    current_q_value = self.q_values[s[0]][s[1]]
                    reward = current_q_value + self.lr * (self.decay_gamma * reward - current_q_value)
                    self.q_values[s[0]][s[1]] = round(reward, 3)
                self.reset()
                i += 1
            else:
                action = self.choose_action()
                # append trace
                self.states.append([self.board.state, action])
                # print("current position {} action {}".format(self.board.state, action))
                # by taking the action, it reaches the next state
                self.board = self.take_action(action)
                # mark is end
                self.board.is_end_func()
                # print("nxt state", self.board.state)
                # print("---------------------")
                self.is_end = self.board.is_end

    def print_q_values(self):
        print('-------------------------------------')
        for i in range(0, BOARD_ROWS):
            for action in ACTIONS:
                out = '| '
                for j in range(0, BOARD_COLS):
                    out += f'{action:<6}:{self.q_values[(i, j)][action]:6.3f} | '
                print(out)
            print('-------------------------------------')
