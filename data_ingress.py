import pandas as pd
import math as m
import numpy as np
from pathlib import Path


class AttachmentConfig:
    def __init__(self, name) -> None:
        '''
        creates a AttachmentConfig from either a file, taking name as string (name of the config),
        '''
        self.n_holes_f, self.n_holes_b, self.thickness_f, self.thickness_b, self.bolt_diam, self.material = self.from_csv(name)

    def from_csv(self, name: str = "unnamed") -> list:
        configpath = Path("attachmentconfig/config_" + name + ".csv")
        config = pd.read_csv(configpath).to_numpy()
        attachmentconfig = [config[0, 1], config[1, 1], config[2, 1],
                     config[3, 1], config[4, 1], config[5, 1]]
        for i in range(len(attachmentconfig)):
            if str(attachmentconfig[i]).upper() == "TRUE":
                attachmentconfig[i] = True
            else:
                try:
                    attachmentconfig[i] = float(attachmentconfig[i])
                except:
                    print("material:", attachmentconfig[i])
        return attachmentconfig

    def to_csv(self, name: str = "unnamed") -> None:
        filename = "config_" + name + ".csv"
        writepath = "attachmentconfig/" + filename
        writepath = Path(writepath)
        config_dict: dict = vars(self)
        # the following line may be indicated as an error, it isn't, it just works
        config_df: pd.DataFrame = pd.DataFrame.from_dict(
            config_dict, orient='index', columns=['Values (all in base SI units)'])
        config_df.to_csv(writepath)
