import sys

import gym
from gomoku import gomoku
import numpy as np


class GomokuEnv(gym.Env):
    spec = None
    space_shape = np.zeros(gomoku.NUM_WIDTH * gomoku.NUM_HEIGHT).shape
    action_space = gym.spaces.Box(
        low=0,
        high=1,
        shape=space_shape
    )
    observation_space = gym.spaces.Box(
        low=0,
        high=2,
        shape=space_shape
    )

    def __init__(self):
        super().__init__()
        self.reward_range = [gomoku.REWARD_FOUL, gomoku.REWARD_WIN]
        self.game = None
        self.done = False
        self.reset()

    def set_reward(self,  win=gomoku.REWARD_WIN, lose=gomoku.REWARD_LOSE, foul=gomoku.REWARD_FOUL, none=gomoku.REWARD_NONE):
        self.game.set_reward(reward_win=win, reward_lose=lose, reward_foul=foul, reward_none=none)

    def reset(self):
        self.game = gomoku.Game()
        return self.observe()

    def step(self, action):
        state, reward, self.done = self.game.act(action)
        return state, reward, self.done

    def render(self, mode='', close=False):
        outfile = sys.stdout
        state = self.observe()
        for i in range(gomoku.NUM_WIDTH * gomoku.NUM_HEIGHT):
            if (i % gomoku.NUM_WIDTH) == 0:
                outfile.write('\n')
            outfile.write('%d ' % state[i])

    def close(self):
        pass

    def seed(self, seed=None):
        pass

    def observe(self):
        return self.game.get_state()

    def done(self):
        return self.done
