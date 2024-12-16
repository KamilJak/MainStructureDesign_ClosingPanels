import numpy as np
from material_data import MaterialProperties




class L_Attachment():

    def __init__(self,n_attachments: float, n_f: int,n_b: int,thickness_b: float, thickness_f: float, hole_diameter: float, material: MaterialProperties):
        self.n_f=n_f
        self.n_b=n_b
        self.n_attachments=n_attachments
        self.hole_diameter=hole_diameter
        self.thickness_f=thickness_f
        self.thickness_b=thickness_b
        self.material = material

    '''
    def coordinate_transform(self,x,y,z):

        #this function takes as input vectors in their respective directions and transfroms them to a local coordinate system of each attachment
        #each attachment is defined by an alpha, which is an angle defined w.r.t to the positive

        x_prime=x*np.cos((self.alpha-90)*np.pi/180)-y*np.cos((self.alpha)*np.pi/180)
        y_prime=x*np.cos((self.alpha)*np.pi/180)+y*np.cos((self.alpha-90)*np.pi/180)
        z_prime=z
        return(x_prime,y_prime,z_prime)
    #'''


    def mass_attachment(self):
        width_f, width_b = 0, 0
        length_f, length_b = 0, 0
        if self.n_f==1:
            width_f=2*1.5*self.hole_diameter
            length_f=2*1.5*self.hole_diameter
        if self.n_f>1:
            width_f=2*1.5*self.hole_diameter+2.5*self.hole_diameter
            if self.n_f%2==0:
                length_f=((self.n_f//2)-1)*2.5*self.hole_diameter+2*1.5*self.hole_diameter
            else:
                length_f=(self.n_f//2)*2.5*self.hole_diameter+2*1.5*self.hole_diameter

        if self.n_b==1:
            width_b=2*1.5*self.hole_diameter
            length_b=2*1.5*self.hole_diameter
        if self.n_b>1:
            width_b=2*1.5*self.hole_diameter+2.5*self.hole_diameter
            if self.n_b%2==0:
                length_f=((self.n_b//2)-1)*2.5*self.hole_diameter+2*1.5*self.hole_diameter
            else:
                length_b=(self.n_b//2)*2.5*self.hole_diameter+2*1.5*self.hole_diameter

        total_mass=(width_f*length_f-(np.pi*0.25*(self.hole_diameter**2))*self.n_f)*self.thickness_f*self.material.density+(width_b*length_b-(np.pi*0.25*(self.hole_diameter**2))*self.n_b)*self.thickness_b*self.material.density
        return total_mass
    

    def compute_attachment_forces(self,a_x,a_y,a_z,mass_panel):

        f_x=mass_panel*a_x/(self.n_attachments*self.n_f)
        f_y=mass_panel*a_y/(self.n_attachments*self.n_f)
        f_z=mass_panel*a_z/(self.n_attachments*self.n_f)

        b_x=(self.mass_attachment()*a_x+f_x)/self.n_b
        b_y=(self.mass_attachment()*a_y+f_y)/self.n_b
        b_z=(self.mass_attachment()*a_z+f_z)/self.n_b

        return np.array(((f_x,f_y,f_z),(b_x,b_y,b_z)))
    
