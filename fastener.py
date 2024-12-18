import math as m

from material_data import MaterialProperties


class FastenerConfig:
    def __init__(self, bolt_diameter, length, head_d, butt_d, material: MaterialProperties) -> None:
        self.length = length
        self.head_diam = head_d
        self.butt_diam = butt_d
        self.shaft_diam = bolt_diameter
        self.area = (0.5 * bolt_diameter)**2 * m.pi
        self.mass = self.calc_mass(material)

    def calc_mass(self, material: MaterialProperties) -> float:
        vol = self.length * self.area
        vol += 0.003 * (0.5*self.head_diam)**2 * m.pi
        vol += 0.003 * (0.5*self.butt_diam)**2 * m.pi
        # print(vol)
        return vol * material.density


def sum_L_over_A(D_shaft, A_shaft, A_head, A_nut):
    return ((0.4*D_shaft/A_shaft)+(0.5*D_shaft/A_head)+(0.4*D_shaft/A_nut))


def force_ratio(t, E_a, E_b, D_fo, D_fi, sum_L_over_A):
    delta_a = (4 * t) / (E_a * m.pi * ((D_fo ** 2) - (D_fi ** 2)))
    delta_b = (1/E_b) * sum_L_over_A
    phi = delta_a / (delta_a + delta_b)
    return phi

def force_ratio_head(base_thickness ,bolt_diameter, material: MaterialProperties, fst_material: MaterialProperties, fastener: FastenerConfig):
    t = base_thickness
    E_a = float(material.elasticity_modulus)
    E_b = float(fst_material.elasticity_modulus)
    D_fo = fastener.head_diam
    D_fi = bolt_diameter
    sum_L_over_A = fastener.length/fastener.area
    delta_a = (4 * t) / (E_a * m.pi * ((D_fo ** 2) - (D_fi ** 2)))
    # print("delta_a is", delta_a)
    delta_b = (1/E_b) * sum_L_over_A
    # print("delta_b is", delta_b)
    phi = delta_a / (delta_a + delta_b)
    # print("phi is", phi)
    return phi

def force_ratio_butt(base_thickness,bolt_diameter, material: MaterialProperties, fst_material: MaterialProperties, fastener: FastenerConfig):
    t = base_thickness
    E_a = float(material.elasticity_modulus)
    E_b = float(fst_material.elasticity_modulus)
    D_fo = fastener.butt_diam
    D_fi = bolt_diameter
    sum_L_over_A = fastener.length/fastener.area
    delta_a = (4 * t) / (E_a * m.pi * ((D_fo ** 2) - (D_fi ** 2)))
    delta_b = (1/E_b) * sum_L_over_A
    phi = delta_a / (delta_a + delta_b)
    return phi

def fastener_area(D_fi):
    return m.pi*0.25*(D_fi**2)
