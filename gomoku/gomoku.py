# -*- coding: utf-8 -*-

REWARD_WIN = 1
REWARD_NONE = 0
REWARD_LOSE = -1
REWARD_FOUL = -1
COLOR = {'None': 0, 'Black': 1, 'White': 2}
NUM_WIDTH = 9
NUM_HEIGHT = 9


class Game:
    def __init__(self, reward_win=REWARD_WIN, reward_lose=REWARD_LOSE, reward_foul=REWARD_FOUL, reward_none=REWARD_NONE):
        self.state = [0 for i in range(NUM_HEIGHT * NUM_HEIGHT)]
        self.reward_win = reward_win
        self.reward_lose = reward_lose
        self.reward_foul = reward_foul
        self.reward_none = reward_none
        self.winner = 'None'
        self.turn = 'Black'
        self.done = False

    def set_reward(self,  reward_win=REWARD_WIN, reward_lose=REWARD_LOSE, reward_foul=REWARD_FOUL, reward_none=REWARD_NONE):
        self.reward_win = reward_win
        self.reward_lose = reward_lose
        self.reward_foul = reward_foul
        self.reward_none = reward_none

    def act(self, action):
        my_color = self.turn
        others_color = self.get_others_color(my_color)

        index = 0
        for val in action:
            if val == 1:
                pos = index
            index = index + 1

        if self.state[pos] != COLOR['None']:
            self.winner = others_color
            self.done = True
            return self.get_state(), self.reward_foul, self.done

        self.state[pos] = COLOR[my_color]

        reward = self.reward_none
        if self.check_win(pos):
            reward = self.reward_win
            self.done = True

        self.turn = others_color

        return self.get_state(), reward, self.done

    def get_state(self):
        return self.state.copy()

    @staticmethod
    def get_others_color(my_color):
        if my_color == 'Black':
            return 'White'
        else:
            return 'Black'

    def get_blank_positions(self):
        positions = []
        for x in range(NUM_WIDTH):
            for y in range(NUM_HEIGHT):
                if self.state[x + y * NUM_WIDTH] == COLOR['None']:
                    positions.append([x, y])

        return positions

    def check_win(self, pos):
        my_color = COLOR[self.turn]

        pos_x = pos % NUM_WIDTH
        pos_y = int(pos / NUM_HEIGHT)

        # 横
        num = 1
        # 左
        for i in range(4):
            x = pos_x - (i + 1)
            if x < 0:
                break

            if self.state[pos - (i + 1)] == my_color:
                num = num + 1
            else:
                break

        # 右
        for i in range(4):
            x = pos_x + (i + 1)
            if x >= NUM_WIDTH:
                break

            if self.state[pos + (i + 1)] == my_color:
                num = num + 1
            else:
                break

        if num >= 5:
            return True

        # 縦
        num = 1
        # 上
        for i in range(4):
            y = pos_y - (i + 1)
            if y < 0:
                break

            if self.state[pos - NUM_WIDTH * (i + 1)] == my_color:
                num = num + 1
            else:
                break

        # 下
        for i in range(4):
            y = pos_y + (i + 1)
            if y >= NUM_HEIGHT:
                break

            if self.state[pos + NUM_WIDTH * (i + 1)] == my_color:
                num = num + 1
            else:
                break

        if num >= 5:
            return True

        # 斜め①
        num = 1
        for i in range(4):
            x = pos_x - (i+1)
            y = pos_y - (i+1)

            if x < 0 or y < 0:
                break

            if self.state[x + y * NUM_WIDTH] == my_color:
                num = num + 1
            else:
                break

        for i in range(4):
            x = pos_x + (i + 1)
            y = pos_y + (i + 1)

            if x >= NUM_WIDTH or y >= NUM_HEIGHT:
                break

            if self.state[x + y * NUM_WIDTH] == my_color:
                num = num + 1
            else:
                break

        if num >= 5:
            return True

        # 斜め②
        num = 1
        for i in range(4):
            x = pos_x - (i+1)
            y = pos_y + (i+1)

            if x < 0 or y >= NUM_HEIGHT:
                break

            if self.state[x + y * NUM_WIDTH] == my_color:
                num = num + 1
            else:
                break

        for i in range(4):
            x = pos_x + (i + 1)
            y = pos_y - (i + 1)

            if x >= NUM_WIDTH or y < 0:
                break

            if self.state[x + y * NUM_WIDTH] == my_color:
                num = num + 1
            else:
                break

        if num >= 5:
            return True

        return False
