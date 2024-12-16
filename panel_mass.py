from loadcase import loadcase_calc

def panel_density() -> float:
    kg_p_m2 = 0
    kg_p_m2 += 0.015 * 48.2
    kg_p_m2 += 4 * 1611 * 0.00019805
    return kg_p_m2
