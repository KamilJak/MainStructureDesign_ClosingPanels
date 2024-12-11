import numpy as np




class l_attachment():

    def __init__(self,alpha: float):
        self.alpha=alpha
        
    def coordinate_transform(self,x,y,z):

        #this function takes as input vectors in their respective directions and transfroms them to a local coordinate system of each attachment
        #each attachment is defined by an alpha, which is an angle defined w.r.t to the positive

        x_prime=x*np.cos((self.alpha-90)*np.pi/180)-y*np.cos((self.alpha)*np.pi/180)
        y_prime=x*np.cos((self.alpha)*np.pi/180)+y*np.cos((self.alpha-90)*np.pi/180)
        z_prime=z
        return(x_prime,y_prime,z_prime)


def compute_attachment_forces(n,a_x,a_y,a_z,mass_panel,mass_attachment):

    f_x=mass_panel*a_x/n
    f_y=mass_panel*a_y/n
    f_z=mass_panel*a_z/n

    b_x=mass_attachment*a_x+f_x
    b_y=mass_attachment*a_y+f_y
    b_z=mass_attachment*a_z+f_z

    return f_x,f_y,f_z,b_x,b_y,b_z

