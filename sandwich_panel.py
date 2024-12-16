import numpy as np

core_thickness=0
fabric_thickness=0


class sandwich_panel:
    def __init__(self,comp_mass,density: float,a: float,b: float):
        self.components_mass=comp_mass
        self.density=density 
        self.width=a
        self.length=b
    def compute_area(self,R):
        return self.width*self.length-np.pi*(R**2)

        

    