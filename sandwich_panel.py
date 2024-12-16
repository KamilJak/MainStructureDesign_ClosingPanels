import numpy as np

core_thickness=0
fabric_thickness=0


class sandwich_panel:
    def __init__(self,comp_mass,a: float,b: float):
        self.components_mass=comp_mass
        self.density=self.panel_density()
        self.width=a
        self.length=b

    def compute_area(self,R):
        return self.width*self.length-np.pi*(R**2)

    def panel_density(self) -> float:
        kg_p_m2 = 0
        kg_p_m2 += 0.015 * 48.2
        kg_p_m2 += 4 * 1611 * 0.00019805
        return kg_p_m2

    def compute_panel_mass(self):
        return self.density*self.compute_area()

    def compute_total_mass(self):
        total_mass=0
        for j in self.components_mass:
            total_mass+=float(j)
        return total_mass+self.compute_panel_mass()
