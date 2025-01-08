from component_mass import Component, components, gc
import numpy as np

core_thickness=0
fabric_thickness=0


class Sandwich_Panel:
    def __init__(self,components: list[list]):
        inner_radius = 0.58
        a = 1.679 # 2*(inner_radius+0.4) 1.679
        b = 1.44
        self.components = components
        self.density=self.panel_density()
        self.width=a
        self.length=b
        self.area = a * b # - np.pi * inner_radius**2

        self.panel_mass = self.density * self.area

        self.total_mass = self.compute_total_mass()

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



def sandwich_panel_get():
    panel_solar: list[list] = [gc('quarter solar panel', 2), gc('rcs thruster', 3)]
    panel_radiator: list[list] = [gc('quarter radiator', 4), gc('quarter louver', 4), gc('rcs thruster', 3)]

    panel_0 = Sandwich_Panel(panel_solar)
    panel_0.total_mass += 0.2 # magnetometer
    panel_1 = Sandwich_Panel(panel_radiator)
    panels = [panel_0, panel_1]

    for panel in panels:
        panel.total_mass += 0.375 + (3*0.106/4) + 0.1
        print(panel.total_mass)
        # sun sensor, star sensor

    return panels



