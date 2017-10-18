import random


class EpsilonGreedy:
    @staticmethod
    def _linear(x1, y1, x2, y2, x):
        k = (y2 - y1) / (x2 - x1)
        b = y1 - k * x1
        return k * x + b

    def exploration_prob(self, step):
        exploration = self._linear(0.0, 1.0, 2e6, 0.25, step)
        if exploration > 0.25:
            return exploration
        exploration = self._linear(2e6, 0.25, 5e6, 0.05, step)
        if exploration > 0.05:
            return exploration
        return 0.05  # minimum exploration

    def action(self, step, explore, exploit):
        if random.random() < self.exploration_prob(step):
            return explore()
        return exploit()