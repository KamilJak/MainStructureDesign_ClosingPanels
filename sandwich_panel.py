from component_mass import Component, components, gc
import numpy as np

core_thickness=0
fabric_thickness=0


class Sandwich_Panel:
    def __init__(self,components: list[list],a: float,b: float, radius: float):
        self.components = components
        self.density=self.panel_density()
        self.width=a
        self.length=b
        self.area = a * b - np.pi * radius**2

        self.panel_mass = self.density * self.area

    def panel_density(self) -> float:
        kg_p_m2 = 0
        kg_p_m2 += 0.015 * 48.2
        kg_p_m2 += 4 * 1611 * 0.00019805
        return kg_p_m2

    def component_mass(self) -> float:
        mass = 0
        for cmp in self.components:
            mass += cmp[0].get(cmp[1])
        return mass

    def compute_total_mass(self):
        total_mass= self.panel_mass + self.component_mass()
        return total_mass


def sandwich_checks():
    panel_1_cmp: list[list] = [gc('HRSC camera'), gc('HRSC electronics'), gc('UV spectrometer'), gc('UV electronics')]

    panel_1 = Sandwich_Panel(panel_1_cmp, 1, 1, 0.4)
    print(panel_1.component_mass())

