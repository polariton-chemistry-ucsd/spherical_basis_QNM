import numpy as np

from src.spherical_basis_QNM.rayleigh_iteration import rayleigh_iteration as rit


def test_linear_rayleigh_nep_solver():
    test = False

    def linear_case(z):
        return np.array([[2. - z, 1.], [1., 2. - z]])

    res = rit.rayleigh_nep_solver(linear_case, np.array([1., 2.]), 2.)

    z = res[0]
    x = res[1]

    if z == [1, 3] or z == [3, 1]:
        test = True

    assert test


def test_nonlinear_rayleigh_nep_solver():
    test = False

    def linear_case(z):
        return np.array([[2. - 3 * z ** 2 + 2 * z, 1.], [1., 2. - 3 * z ** 2 + 2 * z]])

    res = rit.rayleigh_nep_solver(linear_case, np.array([1., 2.]), 2.)

    z = res[0]
    x = res[1]

    if z == [1, 3] or z == [3, 1]:
        test = True

    assert test
