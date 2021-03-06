# this class implements a symbolic particle. The particle class contains the geometrical and physical properties of the
# particle. The physical properties of the particle are implemented by the material class. The particle is embedded
# in a dielectric medium represented as a material with real valued permittivity.

import numpy as np
from src.spherical_basis_QNM.mathfunctions import mathfunctions

from src.spherical_basis_QNM.material import material


class particle:
    def __init__(self, pos, R, mat: material, medium: material = material.material(1.0)):
        self.R = R  # Radius
        self.pos = pos  # Position of the particle in cartesian coordinate
        self.mat = mat  # Material structure
        self.med = medium  # Medium in which the particle is embedded
        pass

    def cart_sph_cen_coord(self, r):
        """Transforms a cartesian coordinate vector to spherical coordinates centered on the particle"""
        if len(r.shape) == 2:
            x = np.stack([r[0] - self.pos[0], r[1] - self.pos[1], r[2] - self.pos[2]])
        elif len(r.shape) == 1:
            x = np.stack([np.array([r[0] - self.pos[0]]), np.array([r[1] - self.pos[1]]),
                          np.array([r[2] - self.pos[2]])])
        else:
            raise IndexError("Input cartesian array must be a 3 vector or an array or 3-vectors")

        sph = np.zeros(x.shape)
        mathfunctions.pcart_to_spher(x[0], x[1], x[2], sph[0], sph[1], sph[2])

        if len(r.shape) == 1:
            sph = np.array([sph[0,0],sph[1,0],sph[2,0]])

        return sph

    def inout(self, r):
        if isinstance(r, np.ndarray):
            if len(r.shape) == 1 and r.shape[0] == 3:
                return float(
                    self.R ** 2 > (r[0] - self.pos[0]) ** 2 + (r[1] - self.pos[1]) ** 2 + (r[2] - self.pos[2]) ** 2)
            elif len(r.shape) == 2 and r.shape[1] == 3:
                result = np.zeros(len(r.shape), dtype=float)
                for i in range(len(r.shape)):
                    result[i] = float(
                        self.R ** 2 > (r[i, 0] - self.pos[0]) ** 2 + (r[i, 1] - self.pos[1]) ** 2 +
                        (r[i, 2] - self.pos[2]) ** 2)
                return result
            else:
                raise ValueError("Invalid dimensionality for coordinate array in inout function. Expected numpy \
                    ndarray with shape (n, 3); got ", r.shape)
        else:
            raise TypeError("Invalid coordinate array in inout function. Expected numpy ndarray, got ", type(r))

    def k(self, f):
        k = self.mat.k(f)
        return k
