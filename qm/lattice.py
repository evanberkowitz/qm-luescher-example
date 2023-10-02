import numpy as np

class Lattice:

    def __init__(self, L, n):

        self.n = np.array(
                list(range(0, n // 2 + 1)) + list(range( - n // 2 + 1, 0)),
                dtype=int)

        self.dx = L / n
        self.x = self.dx * self.n
        self.p = 2*np.pi * self.n / L


    def __len__(self):

        return len(self.n)

    def center_origin(self, f):
        return np.roll(f, (len(self) - 1) // 2)

    def plot(self, ax, f, **kwargs):
        
        return ax.plot(self.center_origin(self.x), self.center_origin(f),
                **kwargs
                )

