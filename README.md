# qm-luescher-example

The Lüscher finite-volume formalism is a widely-applicable method but primarily leveraged by lattice QCD practitioners.

In this notebook we go through an extremely simple example, where we execute the method for one-dimensional quantum mechanics.  The notebook includes a brief introduction and review of lattice QCD literature and then introduces a generic one-dimensional two-particle Hamiltonian.  By moving to center-of-mass and relative coordinates, this is further reduced to single-particle quantum mechanics.

Periodic boundary conditions on a box of length L are used to derive the Lüscher formula for this one-dimensional problem in a straightforward way.

In the second half of the notebook, the Hamiltonian for a uniform spatial discretization with periodic boundary conditions is implemented as a matrix and directly diagonalized, yielding the exact lattice spectrum.  Those energy levels can then be transformed, using the Lüscher formula, into scattering information.  The given example is for the Dirac delta-function potential (or, in two-particle language, a contact interaction), where the exact result is known and can be compared against.

Of course, the Lüscher formalism is generic and the scattering of other short-range interactions can be studied equally well.  Going to higher spatial dimensions is, of course, more complicated, both in terms of finding the finite-volume spectrum and in terms of implementing the Lüscher formula.

# About

I first prepared this notebook for [Lattice Practices 2018][latprac18].
I updated it for [Lattice Practices 2023][latprac23].

[latprac18]:    https://indico-jsc.fz-juelich.de/event/80/
[latprac23]:    https://indico.desy.de/event/40590/
