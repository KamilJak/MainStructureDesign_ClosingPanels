from component_mass import components, Component
from loadcase import tank_loadcase, loadcase_calc
import math as m

def lug_resultant() -> float:
    loads_lug = loadcase_calc(180,90,16)
    loads_lug.yz_plane_load(1.4)
    return loads_lug.resultant()


def tank_attachment_mass(n_attachments) -> float:
    tank_mass = components['propellant'].mass + components['propellant tank'].mass
    tank_f = m.sqrt(tank_loadcase(tank_mass).dot(tank_loadcase(tank_mass)))
    lug_f = lug_resultant()
    ratio = tank_f/lug_f
    ratio /= n_attachments

    lug_mass = 0.00533

    tank_attachment_mass = lug_mass * ratio

    return tank_attachment_mass



