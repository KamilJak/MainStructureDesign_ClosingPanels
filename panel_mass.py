from loadcase import loadcase_calc

def lug_resultant():
    loads_lug = loadcase_calc(180,90,16)
    loads_lug.yz_plane_load(1.4)
    return loads_lug.resultant()
