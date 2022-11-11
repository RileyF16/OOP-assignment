from dodec import Dodecahedron
from sphere import Sphere
from location import Coordinates

def chooseOption(numberOfOptions):
  choice = 0
  while choice < 1 or choice > numberOfOptions:
    print('1 to ' + str(numberOfOptions) + '> ', end='')
    choice = input()
    if choice != '1' and choice != '2' and choice != '3' and choice != '4' and choice != '5' and choice != '6' and choice != '7':
      choice = 0
    if choice == '1' or choice == '2' or choice == '3' or choice == '4' or choice == '5' or choice == '6' or choice == '7':
      choice = int(choice)
    print('\n')
    return choice

def dodec_func():
  edge = int(input("please input edge length: "))
  colour = input("please input colour of the dodecahedron: ")
  print("please input x y z coordinates of the dodecahedron")
  x = input("x: ")
  y = input("y: ")
  z = input("z: ")
  location = Coordinates(x, y, z)
  loc = location.location()
  dodec = Dodecahedron(edge, colour, "dodecahedron", loc)
  while True:
    print('What do you want to get?')
    print('  1 Shape type')
    print('  2 Colour')  
    print('  3 Edge length')
    print('  4 Location')
    print('  5 Volume')  
    print('  6 Surface area')
    print('  7 If you want to change something')
    choice = chooseOption(7)
    if 1 == choice:
      print(dodec.get_type())
      break
    elif 2 == choice:
      print(dodec.get_colour())
      break
    elif 3 == choice:
      print(dodec.get_edge())
      break
    elif 4 == choice:
      print(dodec.get_location())
      break
    elif 5 == choice:
      volume = dodec.volume()
      print('How many digits after the decimal do you want?')
      choice = chooseOption(7)
      if 1 == choice:
        print("The volume is %0.1f squared units" % volume)
      elif 2 == choice:
        print("The volume is %0.2f squared units" % volume)
      elif 3 == choice:
        print("The volume is %0.3f squared units" % volume)
      elif 4 == choice:
        print("The volume is %0.4f squared units" % volume)
      elif 5 == choice:
        print("The volume is %0.5f squared units" % volume)
      elif 6 == choice:
        print("The volume is %0.6f squared units" % volume)
      elif 7 == choice:
        print("The volume is %0.7f squared units" % volume)
      else:
        print("Error")
      break
    elif 6 == choice:
      area = dodec.surface_area()
      print('How many digits after the decimal do you want?')
      choice = chooseOption(7)
      if 1 == choice:
        print("The surface area is %0.1f units" % area)
      elif 2 == choice:
        print("The surface area is %0.2f units" % area)
      elif 3 == choice:
        print("The surface area is %0.3f units" % area)
      elif 4 == choice:
        print("The surface area is %0.4f units" % area)
      elif 5 == choice:
        print("The surface area is %0.5f units" % area)
      elif 6 == choice:
        print("The surface area is %0.6f units" % area)
      elif 7 == choice:
        print("The surface area is %0.7f units" % area)
      else:
        print("Error")
      break
    elif 7 == choice:
      print('What would you like to change?')
      print('  1 Shape type')
      print('  2 Colour')  
      print('  3 Edge length')
      print('  4 Location')
      choice = chooseOption(4)
      if 1 == choice:
        change = input("What would you like to change it to \nthis does not change choosen class: ")
        dodec.set_type(change)
      elif 2 == choice:
        change = input("What would you like to change it to: ")
        dodec.set_colour(change)
      elif 3 == choice:
        change = input("What would you like to change it to: ")
        dodec.set_edge(change)
      elif 4 == choice:
        print('What would you like to change?')
        print('  1 x coordinate')
        print('  2 y coordinate')  
        print('  3 z coordinate')
        choice = chooseOption(3)
        if 1 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_x(coordinate)
        elif 2 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_y(coordinate)
        elif 3 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_z(coordinate)
        else:
          print("Error")
        loc = location.location()
        dodec.set_location(loc)
      else:
        print("Error")
    else:
      print("Error")
  input('Press enter to see shape.')
  print(dodec.draw())
  
def sphere_func():
  radius = int(input("please input radius length: "))
  colour = input("please input colour of the sphere: ")
  print("please input x y z coordinates of the sphere")
  x = input("x: ")
  y = input("y: ")
  z = input("z: ")
  location = Coordinates(x, y, z)
  loc = location.location()
  sphere = Sphere(radius, colour, "sphere", loc)
  while True:
    print('What do you want to get?')
    print('  1 Shape type')
    print('  2 Colour')  
    print('  3 Radius length')
    print('  4 Location')
    print('  5 Volume')  
    print('  6 Surface area')
    print('  7 If you want to change something')
    choice = chooseOption(7)
    if 1 == choice:
      print(sphere.get_type())
      break
    elif 2 == choice:
      print(sphere.get_colour())
      break
    elif 3 == choice:
      print(sphere.get_radius())
      break
    elif 4 == choice:
      print(sphere.get_location())
      break
    elif 5 == choice:
      volume = sphere.volume()
      print('How many digits after the decimal do you want?')
      choice = chooseOption(7)
      if 1 == choice:
        print("The volume is %0.1f units squared" % volume)
      elif 2 == choice:
        print("The volume is %0.2f units squared" % volume)
      elif 3 == choice:
        print("The volume is %0.3f units squared" % volume)
      elif 4 == choice:
        print("The volume is %0.4f units squared" % volume)
      elif 5 == choice:
        print("The volume is %0.5f units squared" % volume)
      elif 6 == choice:
        print("The volume is %0.6f units squared" % volume)
      elif 7 == choice:
        print("The volume is %0.7f units squared" % volume)
      else:
        print("Error")
      break
    elif 6 == choice:
      area = sphere.surface_area()
      print('How many digits after the decimal do you want?')
      choice = chooseOption(7)
      if 1 == choice:
        print("The surface area is %0.1f units" % area)
      elif 2 == choice:
        print("The surface area is %0.2f units" % area)
      elif 3 == choice:
        print("The surface area is %0.3f units" % area)
      elif 4 == choice:
        print("The surface area is %0.4f units" % area)
      elif 5 == choice:
        print("The surface area is %0.5f units" % area)
      elif 6 == choice:
        print("The surface area is %0.6f units" % area)
      elif 7 == choice:
        print("The surface area is %0.7f units" % area)
      else:
        print("Error")
      break
    elif 7 == choice:
      print('What would you like to change?')
      print('  1 Shape type')
      print('  2 Colour')  
      print('  3 radius length')
      print('  4 Location')
      choice = chooseOption(4)
      if 1 == choice:
        change = input("What would you like to change it to \nthis does not change choosen class: ")
        sphere.set_type(change)
      elif 2 == choice:
        change = input("What would you like to change it to: ")
        sphere.set_colour(change)
      elif 3 == choice:
        change = input("What would you like to change it to: ")
        sphere.set_radius(change)
      elif 4 == choice:
        print('What would you like to change?')
        print('  1 x coordinate')
        print('  2 y coordinate')  
        print('  3 z coordinate')
        choice = chooseOption(3)
        if 1 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_x(coordinate)
        elif 2 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_y(coordinate)
        elif 3 == choice:
          coordinate = input("please input new coordinate: ")
          location.set_z(coordinate)
        else:
          print("Error")
        loc = location.location()
        sphere.set_location(loc)
      else:
        print("Error")
    else:
      print("Error")
  input('Press enter to see shape.')
  print(sphere.draw())
  
print("Shape options are sphere or a dodecahedron.")
shapeop = input("Please select the shape: ")
shapeop = shapeop.lower()
if shapeop == "dodecahedron":
    dodec_func()
elif shapeop == "sphere":
    sphere_func()
else:
  print("Error! Wrong input detected! \nPlease check spelling")
  



