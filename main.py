#!/usr/bin/python3

from fastener import FastenerConfig, fastener_area
from loadcase import loadcase_calc
from material_data import MaterialProperties
from sandwich_panel import sandwich_panel_get
from data_ingress import AttachmentConfig
from L_attachment_stress_checks import *
from eval_panel import eval_iteration
import L_attachments as attachments

spacecraft_thickness = 0.0012

if __name__ == "__main__":
    n_length = 4
    attachment_material = MaterialProperties("7075-T6")
    fastener_material = MaterialProperties("4130_steel")
    spacecraft_material = MaterialProperties("7075-T6")
    panels = sandwich_panel_get()
    panel_idx = 0
    for panel in panels:
        print("\n\npanel", panel_idx)
        print("\npanel mass:", panel.panel_mass)
        print("total panel mass:", panel.total_mass)
        panel_mass = panel.total_mass
        iteration = 0
        attachment_cfg = AttachmentConfig("name")
        best_mass = 1000000000000000000000000000000000000
        calcnumber = 0
        for n_attachments in range(6, 1, -1):
            for n_holes_f in range(1, 7):
                for n_holes_b in range(1, 7):
                    for thickness_f in map(lambda x: x/10000, range(4, 50)):
                        for thickness_b in map(lambda x: x/10000, range(4, 50)):
                            for bolt_diam in map(lambda x: x/1000, range(1, 6)):
                                attachment_cfg.n_holes_f = n_holes_f
                                attachment_cfg.n_holes_b = n_holes_b
                                attachment_cfg.thickness_f = thickness_f
                                attachment_cfg.thickness_b = thickness_b
                                attachment_cfg.bolt_diam = bolt_diam
                                attachment_cfg.number = n_attachments
                                succeeds, mass, loads = eval_iteration(panel_mass, attachment_cfg, attachment_material, fastener_material, spacecraft_thickness)
                                attachment_cfg.mass = mass
    
                                calcnumber+=1
    
                                if succeeds and mass < best_mass:
                                    version_number = (n_length-len(str(iteration)))*"0" + str(iteration)
                                    attachment_cfg.name = "panel_" + str(panel_idx) + "_iter-0.0." + version_number
                                    attachment_cfg.to_csv()
                                    print(calcnumber, iteration, mass, "kg")
                                    iteration += 1
                                    best_mass = mass
                                    break
        print("done! : for panel:", panel_idx, "\n")
        panel_idx+=1
    print("done for all")

