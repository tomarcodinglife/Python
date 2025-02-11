import math

print(math.pi) # 3.141592653589793

def circle_area(radius):
    return math.pi * radius ** 2
print(circle_area(10)) # 314.1592653589793

def circle_circumference(radius):
    return 2 * math.pi * radius
print(circle_circumference(10)) # 62.83185307179586

def sphere_volume(radius):
    return 4/3 * math.pi * radius ** 3
print(sphere_volume(10)) # 4188.790204786391

def sphere_surface_area(radius):
    return 4 * math.pi * radius ** 2    
print(sphere_surface_area(10)) # 1256.6370614359173

def cylinder_volume(radius, height):
    return math.pi * radius ** 2 * height
print(cylinder_volume(10, 10)) # 3141.592653589793

def cylinder_surface_area(radius, height):
    return 2 * math.pi * radius * (radius + height)
print(cylinder_surface_area(10, 10)) # 1256.6370614359173

def cone_volume(radius, height):
    return 1/3 * math.pi * radius ** 2 * height
print(cone_volume(10, 10)) 

def cone_surface_area(radius, height):
    return math.pi * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
print(cone_surface_area(10, 10)) 

def ellipse_area(major_axis, minor_axis):
    return math.pi * major_axis * minor_axis
print(ellipse_area(10, 10)) 

def ellipse_circumference(major_axis, minor_axis):
    return math.pi * (3/2 * (major_axis + minor_axis) - math.sqrt(major_axis * minor_axis))
print(ellipse_circumference(10, 10)) 

def sphere_cap_volume(radius, height):
    return 1/3 * math.pi * height ** 2 * (3 * radius - height)
print(sphere_cap_volume(10, 10)) 

def sphere_cap_surface_area(radius, height):
    return 2 * math.pi * radius * height
print(sphere_cap_surface_area(10, 10)) 

def frustum_volume(radius1, radius2, height):
    return 1/3 * math.pi * height * (radius1 ** 2 + radius2 ** 2 + radius1 * radius2)
print(frustum_volume(10, 10, 10)) 

def frustum_surface_area(radius1, radius2, height):
    return math.pi * (radius1 + radius2) * math.sqrt((radius1 - radius2) ** 2 + height ** 2) + math.pi * radius1 ** 2 + math.pi * radius2 ** 2
print(frustum_surface_area(10, 10, 10)) 

def pyramid_surface_area(base_perimeter, base_area, height):
    return 1/2 * base_perimeter * math.sqrt((base_perimeter / 2) ** 2 + height ** 2) + base_area
print(pyramid_surface_area(10, 10, 10)) 

def cylinder_cone_volume(radius, height):
    return 1/3 * math.pi * radius ** 2 * height
print(cylinder_cone_volume(10, 10)) 

def cylinder_cone_surface_area(radius, height):
    return math.pi * radius * (radius + math.sqrt(height ** 2 + radius ** 2))
print(cylinder_cone_surface_area(10, 10))

def torus_volume(major_radius, minor_radius):
    return 2 * math.pi ** 2 * major_radius * minor_radius ** 2
print(torus_volume(10, 10)) 