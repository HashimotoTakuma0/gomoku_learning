# -*- coding: utf-8 -*-
from gomoku.envs.gomoku_env import GomokuEnv
import gym

env = gym.make('gomoku-v0')
env.set_reward(win=10)

for a in range(81):
    action = [0 for i in range(81)]
    action[int(a / 2) + 40 * (a % 2)] = 1

    state, reward, done = env.step(action)

    if done:
        print(reward, done)
        break

env.render()
