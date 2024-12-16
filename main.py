#!/usr/bin/python3

from fastener import FastenerConfig, fastener_area
from loadcase import loadcase_calc
from material_data import MaterialProperties
from sandwich_panel import sandwich_panel_get
from data_ingress import AttachmentConfig
from L_attachment_stress_checks import *
import L_attachments as attachments

spacecraft_thickness = 0.0012

if __name__ == "__main__":
    axial_acceleration = 8.5 * 1.5 * 1.25
    lateral_acceleration = 3 * 1.5 * 1.25
    head_diam = 0.01
    butt_diam = 0.01
    attachment_material = MaterialProperties("7075-T6")
    fastener_material = MaterialProperties("4130_steel")
    spacecraft_material = MaterialProperties("7075-T6")
    panels = sandwich_panel_get()
    for panel in panels:
        attachmentcfg = AttachmentConfig("name")
        attachment = attachments.L_Attachment(4, attachmentcfg.n_holes_f, attachmentcfg.n_holes_b, attachmentcfg.thickness_f, attachmentcfg.thickness_b, attachmentcfg.bolt_diam, attachment_material)
        panel_mass = panel.total_mass
        # (f_loads, b_loads)
        loads = attachment.compute_attachment_forces(lateral_acceleration, lateral_acceleration, axial_acceleration, panel_mass)

        
        print('''==== "B-side checks" ====''')
        fst = FastenerConfig(attachment.hole_diameter, spacecraft_thickness+attachment.thickness_b, head_diam, butt_diam)

        pull_out_check(loads[1, 1], attachment.thickness_b, fst.head_diam, attachment.material.yield_stress, attachment.hole_diameter)

        bearing_check(loads[1, 0], loads[1, 2], attachment.material.yield_stress, attachment.hole_diameter, attachment.thickness_b)

        print('''==== "F-side checks" ====''')
        fst = FastenerConfig(attachment.hole_diameter, 10.7922+attachment.thickness_b, head_diam, butt_diam)

        pull_out_check(loads[0, 1], attachment.thickness_f, fst.head_diam, attachment.material.yield_stress, attachment.hole_diameter)

        bearing_check(loads[0, 0], loads[0, 2], attachment.material.yield_stress, attachment.hole_diameter, attachment.thickness_f)





