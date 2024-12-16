

# Organisation

`main_structure.py` calculates the maximum loads for the main structural shell, from section `5.3` in the manual.

`material_data.py` defines `MaterialProperties` and is pretty much copied from wp4.

`panel_mass.py` only serves to calculate the panel density, and should be merged into `sandwich_panel.py`

`sandwich_panel.py` handles calculation of relevant loads and mass of the honeycomb sandwich panels.

`tank_attachments.py` gets the mass of the attachment lugs for the propellant tank

`loadcase.py` gets the loads on the propellant tank and the wp4 lug

`component_mass.py` is a dict of all component's mass and number
