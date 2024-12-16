import pandas as pd
import math as m
import numpy as np
from pathlib import Path



class MaterialProperties:
    def __init__(self, density, elasticity_modulus: float = 0, yield_stress: float = 0, metal: bool = True, ultimate_stress: float = 0, curve_n: float = 0, transverse_n: float = 0, thermal_coeff: float = 0, poisson_ratio: float = 0) -> None:
        if isinstance(density, str):
            (density, elasticity_modulus, yield_stress, metal,
             ultimate_stress, curve_n, transverse_n, thermal_coeff, poisson_ratio) = self.from_csv(density)
        self.density: float = density
        self.elasticity_modulus: float = elasticity_modulus
        self.yield_stress: float = yield_stress
        self.ismetal: bool = metal
        self.ultimate_tensile_str: float = ultimate_stress
        self.axial_curve_number: int = int(curve_n)
        self.transverse_curve_number: int = int(transverse_n)
        self.thermal_coeff: float = thermal_coeff
        self.poisson_ratio: float = poisson_ratio

    def from_csv(self, name: str = "unnamed"):
        materialpath = Path("materials/material_" + name + ".csv")
        material = pd.read_csv(materialpath).to_numpy()
        material = [material[0, 1], material[1, 1], material[2, 1],
                    material[3, 1], material[4, 1], material[5, 1], material[6, 1], material[7, 1], material[8, 1]]
        for i in range(len(material)):
            if str(material[i]).upper() == "TRUE":
                material[i] = True
            else:
                try:
                    material[i] = float(material[i])
                except:
                    print("here's the string")
        return material

    def to_csv(self, name: str = "unnamed") -> None:
        filename = "material_" + name + ".csv"
        writepath = "materials/" + filename
        writepath = Path(writepath)
        config_dict: dict = vars(self)
        # the following line may be indicated as an error, it isn't, it just works
        config_df: pd.DataFrame = pd.DataFrame.from_dict(
            config_dict, orient='index', columns=['Values (all in base SI units)'])
        config_df.to_csv(writepath)
