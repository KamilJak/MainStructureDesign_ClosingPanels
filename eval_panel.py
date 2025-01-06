import L_attachments as attachments
from L_attachment_stress_checks import *
from data_ingress import AttachmentConfig
from fastener import FastenerConfig, shear_check

def eval_iteration(panel_mass, attachmentcfg: AttachmentConfig, attachment_material, fastener_material, spacecraft_thickness):
    axial_acceleration = 8.5 * 1.5 * 1.25 * 9.81
    lateral_acceleration = 3 * 1.5 * 1.25 * 9.81
    head_diam = attachmentcfg.bolt_diam + 0.003
    butt_diam = attachmentcfg.bolt_diam + 0.003

    succeeds = True

    # print("total panel mass:", panel_mass)
    attachment = attachments.L_Attachment(attachmentcfg.number, attachmentcfg.n_holes_f, attachmentcfg.n_holes_b, attachmentcfg.thickness_f, attachmentcfg.thickness_b, attachmentcfg.bolt_diam, attachment_material)
    loads = attachment.compute_attachment_forces(lateral_acceleration, lateral_acceleration, axial_acceleration, panel_mass)
    # (f_loads, b_loads)
    # print(loads)

    # print("attachment mass: ", attachment.mass_attachment()*attachmentcfg.number)

    total_system_mass = attachment.mass_attachment()*attachmentcfg.number

    # print('''==== "B-side checks" ====''')
    fst = FastenerConfig(attachment.hole_diameter, spacecraft_thickness+attachment.thickness_b, head_diam, butt_diam, fastener_material)

    total_system_mass += fst.mass*attachment.n_b*attachmentcfg.number

    succeeds = pull_out_check(loads[1, 1], attachment.thickness_b, fst.head_diam, attachment.material.yield_stress, attachment.hole_diameter) and succeeds

    succeeds = bearing_check(loads[1, 0], loads[1, 2], attachment.material.yield_stress, attachment.hole_diameter, attachment.thickness_b) and succeeds

    # print('''==== "F-side checks" ====''')
    fst = FastenerConfig(attachment.hole_diameter, 0.0107922+attachment.thickness_b, head_diam, butt_diam, fastener_material)

    total_system_mass += fst.mass*attachment.n_f*attachmentcfg.number

    succeeds = pull_out_check(loads[0, 1], attachment.thickness_f, fst.head_diam, attachment.material.yield_stress, attachment.hole_diameter) and succeeds

    succeeds = bearing_check(loads[0, 0], loads[0, 2], attachment.material.yield_stress, attachment.hole_diameter, attachment.thickness_f) and succeeds

    succeeds = shear_check(loads[0, 0], loads[0, 1], loads[1, 0], loads[1, 2], attachment, fastener_material) and succeeds

    # print("total system mass: ", total_system_mass)

    return succeeds, total_system_mass, loads


