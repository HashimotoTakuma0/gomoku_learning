# -*- coding: utf-8 -*-
from gomoku.envs.gomoku_env import GomokuEnv
import gym

import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import torch.utils.data
import torchvision
from torchvision import datasets, models, transforms

lr = 0.1

# env = gym.make('gomoku-v0')
# env.set_reward(win=10)

env = gym.make("CartPole-v0")

observation = env.reset()

done = False
while not done:
    action = env.action_space.sample()
    env.render()
    observation, reward, done, info = env.step(action)
    print(f"observation: {observation}\nreward: {reward}\ndone: {done}\ninfo: {info}\n")
    if done:
        break

env.close()
print("done")

