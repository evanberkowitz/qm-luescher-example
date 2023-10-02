import numpy as np
import matplotlib.pyplot as plt

def spectrum(ax, lattice, eigenvalues, eigenvectors, modes=None, potential=None):
    
    energies      = eigenvalues
    wavefunctions = eigenvectors.T
    if modes is not None:
        energies      = energies     [0:modes]
        wavefunctions = wavefunctions[0:modes]

    maximum = np.max(np.abs(wavefunctions))
    
    for energy, psi in zip(energies, wavefunctions):
        
        psi2 = (psi*psi.conj())
        psi2 *= np.sqrt(len(lattice))
        
        wavefunction, = lattice.plot(ax, (energy + psi2).real,
                                #linestyle='none',
                                marker='.')
        ax.hlines(energy,min(lattice.x),max(lattice.x), color=wavefunction.get_color(), linestyle = ":", label=f"E={energy}")

    if potential is not None:
        V = potential(lattice)
        minimum = min(-maximum, np.min(V))
        lattice.plot(ax, V, 
                color='black',
                marker='.', zorder=-1, label='V')
    
    ax.set_xlabel('$x$')
    ax.set_ylabel('$|\psi_n(x)|^2+E_n$')
    ax.legend(bbox_to_anchor=(1.04,1))


    #ax.set_ylim((minimum, np.max(energies) + 2*offset))

    return ax
