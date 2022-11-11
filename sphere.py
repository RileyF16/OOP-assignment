from shape3D import Shape3D
import math
from colored import fg

class Sphere(Shape3D):
    def __init__(self, radius, colour, type, location):
        self.radius = radius
        super().__init__(colour, type, location)

    def get_radius(self):
        return self.radius

    def set_radius(self, newradius):
        self.radius = newradius

    def volume(self):
        volume = (4/3)*math.pi*(self.radius**3)
        return volume

    def surface_area(self):
        area = 4*math.pi*(self.radius**2)
        return area

    def draw(self):
      self.colour = self.colour.lower()
      colour = fg(self.colour)
      ASCII_sphere = colour + r"""
                              &&&&&&&&&&#######                                 
                        &eeeeeeeeeeeeeeee&&&&&&#######%                          
                    &eoooo*******oooooooeeeee&&&&&########%                      
                 eoo****!!!!!!!!******oooooeeee&&&&&########%%                   
              eoo**!!!!::::::::!!!!!*****ooooeeee&&&&&########%%%                
            eo**!!::::::...:::::::!!!!!***ooooeeee&&&&&########%%%%              
          eo*!!:::.............:::::!!!!***ooooeeee&&&&&########%%%%%            
        eo*!!:::.................::::!!!!***ooooeeee&&&&#########%%%%%%          
       eo*!!::....................::::!!!****oooeeee&&&&&#########%%%%%%         
     &o**!::......................::::!!!****oooeeee&&&&&##########%%%%%%%       
    &o**!::.......................::::!!!****oooeeee&&&&&##########%%%%%%%%      
   &oo*!!::.......................:::!!!!***ooooeeee&&&&&##########%%%%%%%%%     
  &eo*!!::.......................::::!!!****ooooeeee&&&&&##########%%%%%%%%%%    
  eo**!!::......................::::!!!!***ooooeeeee&&&&&##########%%%%%%%%%%    
 &eo**!!:::...................:::::!!!!****ooooeeee&&&&&###########%%%%%%%%%%%   
 eeo**!!::::................:::::!!!!!****ooooeeee&&&&&&###########%%%%%%%%%%%   
&eeo***!!:::::...........::::::!!!!!****oooooeeee&&&&&&###########%%%%%%%%%%%%%  
&eeoo**!!!!::::::::::::::::::!!!!!*****ooooeeeee&&&&&&############%%%%%%%%%%%%%  
&eeooo***!!!!::::::::::::!!!!!!!*****oooooeeeee&&&&&&############%%%%%%%%%%%%%%  
&&eeooo***!!!!!!!!!!!!!!!!!!!******oooooeeeeee&&&&&&############%%%%%%%%%%%%%%%  
&&eeeooo******!!!!!!!!!!********ooooooeeeeee&&&&&&&############%%%%%%%%%%%%%%%%  
#&&eeeooooo******************oooooooeeeeee&&&&&&&#############%%%%%%%%%%%%%%%%%  
#&&&eeeeoooooooo******oooooooooooeeeeeee&&&&&&&&#############%%%%%%%%%%%%%%%%%%  
##&&&&eeeeeooooooooooooooooooeeeeeeee&&&&&&&&&##############%%%%%%%%%%%%%%%%%%%  
 ##&&&&&eeeeeeeeeeeeeeeeeeeeeeeeee&&&&&&&&&################%%%%%%%%%%%%%%%%%%%   
 ####&&&&&&eeeeeeeeeeeeeeeeeee&&&&&&&&&&&################%%%%%%%%%%%%%%%%%%%%%   
  #####&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&#################%%%%%%%%%%%%%%%%%%%%%%    
  %#######&&&&&&&&&&&&&&&&&&&&&&&&###################%%%%%%%%%%%%%%%%%%%%%%%%    
   %###########&&&&&&&&&&&&&#######################%%%%%%%%%%%%%%%%%%%%%%%%%     
    %############################################%%%%%%%%%%%%%%%%%%%%%%%%%%      
     %%#######################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%       
       %%#################################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%         
        %%%%%#########################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%          
          %%%%%%%%#############%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%            
            %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%              
              %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                
                 %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                   
                    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                      
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                          
                               %%%%%%%%%%%%%%%%%                                 """
      return ASCII_sphere