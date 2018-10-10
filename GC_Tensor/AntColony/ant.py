import pygame

import random
import math
import numpy as np

from gameObject import GameObject

from NN.model import Model
from NN.memory import Memory

class Ant(GameObject):
    def __init__(self, x, y, w, h, sess, max_eps, min_eps, decay, gamma, batch_size):
        GameObject.__init__(self, x, y, w, h)
        self.color = (0, 0, 0)
        self.speed = 1

        # NN stuff
        self.sess = sess
        self.max_eps = max_eps # Epsilon value, not episodes
        self.min_eps = min_eps
        self.decay = decay # lambda
        self.gamma = gamma
        self.eps = self.max_eps
        self.steps = 0

        # num_tiles, tile_types, num_actions
        self.model = Model(50, 2, 6, batch_size)
        self.memory = Memory(50000)

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.bounds)

    def update(self, state):
        action = self.choose_action(state)
        next_state, reward, done = self.take_action(state, action)
        # analyze next_state, which is updated map
        # reward should be -1 from hunger unless food found
        # done if food found
        if done:
            next_state = None

        # TODO: One hot encode state and next_state before passing into training
        self.memory.addSample((state, action, reward, next_state))
        self.replay() # Q training step

        self.steps += 1
        self.eps = self.min_eps + (self.max_eps - self.min_eps) * math.exp(-self.decay * self.steps)

        # increment reward total
        # return stuff to inform game of done

    def choose_action(self, state):
        if random.random() < self.eps:
            return random.randint(0, self.model.num_actions - 1)
        else:
            return np.argmax(self.model.predict_one(state, self.sess))

    def take_action(self, state, action):
        pass

    def replay(self):
        batch = self.memory.sample(self.model.batch_size)
        states = np.array([val[0] for val in batch]) # index 0 is state in tuple
        next_states = np.array([np.zeros(self.model.num_tiles * self.model.num_tile_types) \
            if val[3] is None else val[3] for val in batch])

        # Predict Q values
        q_s_a = self.model.predict_batch(states, self.sess)
        # Predict Q' vlaues
        q_s_a_d = self.model.predict_batch(next_states, self.sess)

        x = np.zeros((len(batch), self.model.num_tiles * self.model.num_tile_types))
        y = np.zeros((len(batch), self.model.num_actions))

        for i, b in enumerate(batch): # i = batch index, b = batch item
            state, action, reward, next_state = b[0], b[1], b[2], b[3]
            current_q = q_s_a[i]
            if next_state is None:
                # 
                current_q[action] = reward
            else:
                # Gamma is discount factor, close to 1 for delayed rewards
                current_q[action] = reward + self.gamma * np.amax(q_s_a_d[i])

            x[i] = state # maps batch index to state (2d tensor)
            y[i] = current_q

        self.model.train_batch(self.sess, x, y)