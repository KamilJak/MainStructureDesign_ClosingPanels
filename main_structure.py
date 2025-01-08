#!/usr/bin/python3
from material_data import MaterialProperties
import math as m

def column_buckling_load(r, t, l, material: MaterialProperties) -> float:
    moi = (m.pi/2) * (r**4 - (r-t)**4)
    load = m.pi**2 * material.elasticity_modulus * moi / l**2
    return load

def shell_buckling_load(r, t, l, pressure, material: MaterialProperties) -> float:
    q = (pressure/material.elasticity_modulus) * (r/t)**2
    sigma_cr = (1.983 - 0.983*m.exp(-23.14 * q)) * minimise_k(r, t, l, material.poisson_ratio) * (m.pi**2 * material.elasticity_modulus)/(12 * (1-material.poisson_ratio**2)) *  (t/l)**2
    area = m.pi * (r**2 - (r-t)**2)
    return sigma_cr*area

def minimise_k(r, t, l, v) -> float:
    k = m.inf
    lam = 10000
    delta = 0.1
    step = 100
    prev_sign = 0
    for i in range(10000):
        k = get_k(r, t, l, v, lam)
        # print("lambda: ", lam, "k ", k)
        dkdl = (get_k(r, t, l, v, lam+delta) - k)/delta
        if m.isclose(abs(m.copysign(1, dkdl) - prev_sign), 2):
            step /= 2
            # print("reducing step")
        prev_sign = m.copysign(1, dkdl)
        lam -= m.copysign(1, dkdl)*step

    return k

def get_k(r, t, l, v, lam) -> float:
    return (lam + (12 * (l**4) * (1-v**2)) / (m.pi**4 * r**2 * t**2 * lam))

def maximum_load(radius, thickness, length, pressure, material: MaterialProperties) -> float:
    column = column_buckling_load(radius, thickness, length, material)
    shell = shell_buckling_load(radius, thickness, length, pressure, material)
    # print("\n", shell, column, "\n")
    return min(shell, column)


def get_mass(radius, thickness, length, material: MaterialProperties) -> float:
    return (m.pi*radius**2 - m.pi*(radius-thickness)**2)*length * material.density


volume = 1.207
other_structures = 4*3
other_mass = (56.5+33.2+57.2+3.66+other_structures+17.56)
length = 1.44 # max(0.715 + 0.282 + 4*(0.015+0.00019805*4), 2)
print(length)
material = MaterialProperties('7075-T6')
pmin = 500000
pmax = 1950000
min_mass = m.inf
r = m.sqrt((volume/length)/m.pi)
for t in map(lambda x: x/10000, range(5, 20)):
    mass = get_mass(r, t, length, material)
    total_mass = mass + other_mass
    maxload = maximum_load(r, t, length, pmin, material)
    load = 8.5*1.5*1.25*9.81*total_mass 
    hoopstress = pmax*r/(2*t)
    if total_mass <= min_mass and load*1.5 <= maxload and hoopstress*1.5 <= material.yield_stress:
        min_mass = total_mass
        print(r, t, total_mass, mass)
        


        


