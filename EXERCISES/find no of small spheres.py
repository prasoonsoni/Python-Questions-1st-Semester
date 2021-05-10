                              # OPERATORS
""" Q.1 --- TO FIND NO OF SMALL SPHERES OF RADIUS 'r' THAT CAN BE STORED IN 
THE LARGE SPHERE OF RADIUS  'R'   """



R = float(input("ENTER RADIUS OF LARGE SPHERE(in cm) : "))


r = float(input("ENTER RADIUS OF SMALL SPHERE(in cm) : "))


V = (4/3)*3.14*R*R*R # V = VOLUME OF LARGE SPHERE!!


v = (4/3)*3.14*r*r*r # v = volume of small sphere!!


n = V/v # n = NO OF SMALL SPHERES THAT CAN BE STORED IN LARGE SPHERE


print("NUMBER OF SMALL SPHERES : ", (n))

## MY FIRST PYTHON PROGRAM ##
