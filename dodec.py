from shape3D import Shape3D
import math
from colored import fg

class Dodecahedron(Shape3D):
    def __init__(self, edge, colour, type, location):
        self.edge = edge
        super().__init__(colour, type, location)

    def get_edge(self):
        return self.edge

    def set_edge(self, newedge):
        self.edge = newedge

    def volume(self):
        volume = ((15+7*math.sqrt(5))/4)*(self.edge**3)
        return volume

    def surface_area(self):
        area = 3*math.sqrt(25+(10*math.sqrt(5)))*(self.edge**2)
        return area

    def draw(self):
        self.colour = self.colour.lower()
        colour = fg(self.colour)
        ASCII_dodec = colour + r"""
     _,--"^"--._     
   ,'\         /`.   
 ,'   \_______/   `. 
|     /       \     |
|    /         \    |
|  _/           \_  |
\'' `-.       ,-' ``/
 \     `-._,-'     / 
  \       |       /  
   `-.._  |  _,,-'         
        ``"''
"""
        return ASCII_dodec