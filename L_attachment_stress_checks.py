
import math as m



def pull_out_check(y_force: float, thickness: float, head_diam: float, allowable_stress: float,bolt_diam: float):
    allowable_stress = float(allowable_stress)
    tau = (y_force/ (m.pi * head_diam * thickness))
    sigma = (y_force/(0.25*m.pi*(head_diam**2-bolt_diam**2)))
    print("Pullout normal stress: ", sigma)
    print("Pullout shear stress: ", tau,
            " and Von Mises stress is:", (m.sqrt((3 * tau**2)+sigma**2)))
    print("Safety factor is: ", ((allowable_stress/m.sqrt((3 * tau**2)+sigma**2))-1))

def bearing_check(x_force: float, z_force: float, plate: str, allowable_stress: float,bolt_diameter: float,thickness: float):
    allowable_stress = float(allowable_stress)
    p = m.sqrt(x_force**2 + z_force**2)
    print(p, "p force")
    sigma = p / (bolt_diameter * thickness)
    print("The bearing stress is:", sigma)
    print("Safety margin is:", ((allowable_stress/sigma)-1))

def bearing_check_thermal_included(x_force: float, z_force: float, thickness: float,bolt_diameter: float, allowable_stress: float, thermal_force: float):
    print(thermal_force)
    allowable_stress = float(allowable_stress)
    p = m.sqrt(x_force**2 + z_force**2) + thermal_force
    sigma = p / (bolt_diameter*thickness)
    print("The bearing stress at hole is:", sigma)
    print("Safety margin is:", ((allowable_stress/abs(sigma))-1))