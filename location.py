from shape3D import Shape3D

class Coordinates(Shape3D):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z

  def location(self):
    location = [self.x, self.y, self.z]
    return location

  def set_x(self, value):
    self.x = value

  def set_y(self, value):
    self.y = value

  def set_z(self, value):
    self.z = value