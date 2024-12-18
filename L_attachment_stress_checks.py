
import math as m

from material_data import MaterialProperties
from fastener import FastenerConfig, force_ratio_head, force_ratio_butt

def pull_out_check(y_force: float, thickness: float, head_diam: float, allowable_stress: float,bolt_diam: float):
    allowable_stress = float(allowable_stress)
    tau = (y_force/ (m.pi * head_diam * thickness))
    sigma = (y_force/(0.25*m.pi*(head_diam**2-bolt_diam**2)))
    # print("Pullout normal stress: ", sigma)
    # print("Pullout shear stress: ", tau,
    #         " and Von Mises stress is:", (m.sqrt((3 * tau**2)+sigma**2)))
    safety_margin = (allowable_stress/m.sqrt((3 * tau**2)+sigma**2))-1
    # print("Safety margin is: ", safety_margin)
    if safety_margin >= 0.5:
        return True
    else:
        return False


def bearing_check(x_force: float, z_force: float, allowable_stress: float,bolt_diameter: float,thickness: float):
    allowable_stress = float(allowable_stress)
    p = m.sqrt(x_force**2 + z_force**2)
    # print(p, "p force")
    sigma = p / (bolt_diameter * thickness)
    # print("The bearing stress is:", sigma)
    safety_margin = allowable_stress/sigma - 1
    # print("Safety margin is:", safety_margin)
    if safety_margin >= 0.5:
        return True
    else:
        return False


def bearing_check_thermal_included(x_force: float, z_force: float, thickness: float,bolt_diameter: float, allowable_stress: float, thermal_force: float):
    print(thermal_force)
    allowable_stress = float(allowable_stress)
    p = m.sqrt(x_force**2 + z_force**2) + thermal_force
    sigma = p / (bolt_diameter*thickness)
    print("The bearing stress at hole is:", sigma)
    print("Safety margin is:", ((allowable_stress/abs(sigma))-1))


#thermal stress calculations
def evaluate_thermal(base_thickness_sc,base_thickness_attachment,bolt_diameter, lug_material: MaterialProperties, sc_material: MaterialProperties, fst_material: MaterialProperties, fastener: FastenerConfig, delta_T_max):
    phi_backplate = force_ratio_head(base_thickness_attachment,bolt_diameter, lug_material, fst_material, fastener)
    phi_vehicle = force_ratio_butt(base_thickness_sc ,bolt_diameter, sc_material, fst_material, fastener)

    load_lug_maxT = (lug_material.thermal_coeff - fst_material.thermal_coeff) * delta_T_max * fst_material.elasticity_modulus * fastener.area * (1 - phi_backplate)
    load_sc_maxT = (sc_material.thermal_coeff - fst_material.thermal_coeff) * delta_T_max * fst_material.elasticity_modulus * fastener.area * (1 - phi_vehicle)

    return load_lug_maxT, load_sc_maxT

