from ufl import Identity, det, inner, ln, exp
import dolfinx


class GuccioneMaterial:
    def __init__(self, mesh, **params):
        self._mesh = mesh
        params = params or {}
        self._parameters = self.default_parameters()
        self._parameters.update(params)

    @staticmethod
    def default_parameters():
        p = {
            "C": 2.0,
            "bf": 8.0,
            "bt": 2.0,
            "bfs": 4.0,
            "e1": None,
            "e2": None,
            "e3": None,
            "kappa": None,
            "Tactive": None,
        }
        return p

    def is_isotropic(self):
        """
        Return True if the material is isotropic.
        """
        p = self._parameters
        return p["bt"] == 1.0 and p["bf"] == 1.0 and p["bfs"] == 1.0

    def is_incompressible(self):
        """
        Return True if the material is incompressible.
        """
        return self._parameters["kappa"] is None

    def strain_energy(self, F, p=None):
        """
        UFL form of the strain energy.
        """
        params = self._parameters

        I = Identity(3)
        J = det(F)
        C = pow(J, -float(2) / 3) * F.T * F
        E = 0.5 * (C - I)

        CC = dolfinx.fem.Constant(self._mesh, params["C"])
        if self.is_isotropic():
            # isotropic case
            Q = inner(E, E)
        else:
            # fully anisotropic
            bt = dolfinx.fem.Constant(self._mesh, params["bt"])
            bf = dolfinx.fem.Constant(self._mesh, params["bf"])
            bfs = dolfinx.fem.Constant(self._mesh, params["bfs"])

            e1 = params["e1"]
            e2 = params["e2"]
            e3 = params["e3"]

            E11, E12, E13 = inner(E * e1, e1), inner(E * e1, e2), inner(E * e1, e3)
            E21, E22, E23 = inner(E * e2, e1), inner(E * e2, e2), inner(E * e2, e3)
            E31, E32, E33 = inner(E * e3, e1), inner(E * e3, e2), inner(E * e3, e3)

            Q = (
                bf * E11**2
                + bt * (E22**2 + E33**2 + E23**2 + E32**2)
                + bfs * (E12**2 + E21**2 + E13**2 + E31**2)
            )

        # passive strain energy
        Wpassive = CC / 2.0 * (exp(Q) - 1)

        # active strain energy
        if params["Tactive"] is not None:
            self.Tactive = dolfinx.fem.Constant(self._mesh, params["Tactive"])
            I4 = inner(C * e1, e1)
            Wactive = self.Tactive / 2.0 * (I4 - 1)
        else:
            Wactive = 0.0

        # incompressibility
        if params["kappa"] is not None:
            kappa = dolfinx.fem.Constant(self._mesh, params["kappa"])
            Winc = kappa * (J * ln(J) - J + 1)
        else:
            Winc = -p * (J - 1)

        return Wpassive + Wactive + Winc

    def set_active_stress(self, value):
        self.Tactive.value = value

    def get_active_stress(self):
        return float(self.Tactive.value)
