import numpy as np

class harmonic_oscillator:

    def __init__(self, ω=1.):
        self.ω = ω

    def __call__(self, x):
        return (0.5 * (self.ω * x)**2)

class square_well:

    def __init__(self, width=1, height=1):
        self.w = width
        self.h = height

    def __call__(self, x):
        return np.where( np.abs(x) < self.w/2, self.h, 0)

mystery_potential = square_well(1, -12)

