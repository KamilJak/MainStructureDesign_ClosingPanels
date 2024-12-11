from loadcase import loadcase_calc

def lug_resultant() -> float:
    loads_lug = loadcase_calc(180,90,16)
    loads_lug.yz_plane_load(1.4)
    return loads_lug.resultant()

def tank_attach_resultant() -> float:
    raise NotImplementedError("no resultant load for the tank attachments yet")


def panel_density() -> float:
    kg_p_m2 = 0
    kg_p_m2 += 0.015 * 48.2
    kg_p_m2 += 4 * 1611 * 0.00019805
    return kg_p_m2
