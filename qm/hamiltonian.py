import numpy as np

from qm.kinetic import Kinetic

class Hamiltonian:

    def __init__(self, Potential, Kinetic=Kinetic()):

        self.K = Kinetic
        self.V = Potential

    def __call__(self, lattice):
        return self.K(lattice) + np.diag(self.V(lattice))

    def spectrum(self, lattice):
        return np.linalg.eigh(self(lattice))
    
    def energies(self, lattice, modes=None):
        e, _ = self.spectrum(lattice)
        if modes is None:
            return e
        return e[:modes]
