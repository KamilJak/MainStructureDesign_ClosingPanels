from component_mass import Component, components, gc
import numpy as np

core_thickness=0
fabric_thickness=0


class Sandwich_Panel:
    def __init__(self,components: list[list]):
        inner_radius = 0.58
        a = b = 1.679 # 2*(inner_radius+0.4) 1.679
        self.components = components
        self.density=self.panel_density()
        self.width=a
        self.length=b
        self.area = a * b - np.pi * inner_radius**2

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
    panel_upper_closing: list[list] = [gc('quarter solar panel'), gc('quarter radiator'), gc('quarter louver'), gc('rcs thruster', 3)]
    panel_upper_inner: list[list] = [gc('quarter solar panel'), gc('quarter radiator'), gc('quarter louver'), gc('HRSC camera'), gc('UV spectrometer'), gc('a-BELA'), gc('gyroscope', 2), gc('rcs thruster', 3)]
    panel_lower: list[list] = [gc('quarter solar panel'), gc('quarter radiator'), gc('quarter louver'), gc('HRSC electronics'), gc('UV electronics'), gc('reaction wheel', 4), gc('magnetometer electronics'), gc('battery'), gc('PCDS'), gc('cables'), gc('rcs thruster', 3)]
    panel_lower_closing: list[list] = [gc('quarter solar panel'), gc('quarter radiator'), gc('quarter louver'), gc('rcs thruster', 3)]

    panel_0 = Sandwich_Panel(panel_upper_closing)
    panel_1 = Sandwich_Panel(panel_upper_inner)
    panel_2 = Sandwich_Panel(panel_lower)
    panel_3 = Sandwich_Panel(panel_lower_closing)
    panels = [panel_0, panel_1, panel_2, panel_3]

    for panel in panels:
        panel.total_mass += 0.375 + (3*0.106/4) + 0.1 + panel.width * 1.44 * panel.density
        print(panel.total_mass)
        # sun sensor, star sensor, magnetometer and outer closing panels

    return panels



