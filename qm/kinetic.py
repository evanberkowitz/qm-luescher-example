import numpy as np

stencils = {
        # Coefficients lifted from https://en.wikipedia.org/wiki/Finite_difference_coefficient#Central_finite_difference
        # Accuracy: ((∆x, weight) pairs)
        2:  ((-1,+1), (0,-2), (+1,+1)),
        4:  ((-2, -1/12), (-1,4/3), (0,-5/2), (+1,4/3), (+2,-1/12)),
        6:  ((-3, +1/90), (-2, -3/20), (-1, 3/2), (0, -49/18), (+1, 3/2), (+2, -3/20), (+3, +1/90)),
        8:  ((-4, -1/560), (-3, 8/315), (-2, -1/5), (-1, 8/5), (0, -207/72), (+1, 8/5), (+2, -1/5), (+3, 8/315), (+4, -1/560)),
        }


class CentralSecondDifference:

    def __init__(self, order=2):
        self.order   = order
        try:
            self.stencil = stencils[order]
        except KeyError as e:
            raise ValueError(f'Order-{order} Laplacian stencil unavailable.') from e


    def __call__(self, lattice):

        x  = len(lattice)
        d2 = np.zeros((x, x))

        # This implicitly leverages periodic boundary conditions.
        for Δx, weight in self.stencil:
            d2 += weight * np.roll(np.eye(x), Δx, axis=0)

        return d2 / lattice.dx**2

class PerfectSecondDerivative:

    def __init__(self):
        pass

    def __call__(self, lattice):
        
        momentum_space_d2 = np.diag(-(lattice.p)**2)

        return np.fft.ifft( np.fft.fft(momentum_space_d2, axis=0), axis=1)

class Kinetic:

    def __init__(self, mass=1, laplacian=PerfectSecondDerivative()):

        self.mass = mass
        self.laplacian = laplacian

    def __call__(self, lattice):

        return - self.laplacian(lattice) / (2*self.mass)
