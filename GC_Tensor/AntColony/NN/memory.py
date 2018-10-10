import random

class Memory:
    def __init__(self, max_memory):
        self.max_memory = max_memory
        self.samples = []

    def addSample(self, sample):
        self.samples.append(sample)
        if len(self.samples) > self.max_memory:
            self.samples.pop(0)

    def sample(self, num_samples):
        if num_samples > len(self.samples):
            return random.sample(self.samples, len(self.samples))
        else:
            return random.sample(self.samples, num_samples)
