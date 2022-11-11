class Shape3D:

    def __init__(self, colour, type, location):
        self.colour = colour
        self.type = type
        self.location = location

    def volume(self):
        return 0

    def surface_area(self):
        return 0

    def draw(self):
        return 0

    def get_colour(self):
        return self.colour

    def get_type(self):
        return self.type

    def get_location(self):
        return self.location

    def set_colour(self, newcolour):
        self.colour = newcolour

    def set_location(self, newlocation):
        self.location = newlocation

