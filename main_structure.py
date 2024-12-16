from data_ingress import MaterialProperties
import math as m

def column_buckling_load(r, t, l, material: MaterialProperties) -> float:
    moi = (m.pi/4) * (r**4 - (r-t)**4)
    load = m.pi**2 * material.elasticity_modulus * moi / l**2
    return load

def shell_buckling_load(r, t, l, pressure, material: MaterialProperties) -> float:
    q = (pressure/material.elasticity_modulus) * (r/t)**2
    sigma_cr = (1.983 - 0.983*m.exp(-23.14 * q)) * minimise_k(r, t, l, material.poisson_ratio) * (m.pi**2 * material.elasticity_modulus)/(12 * (1-material.poisson_ratio**2)) *  (t/l)**2
    area = m.pi * (r**2 - (r-t)**2)
    return sigma_cr/area

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


