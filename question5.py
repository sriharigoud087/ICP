import math

# Given radius
radius = 30

# Calculate the area of a circle
area_of_circle = math.pi * radius ** 2

# Calculate the circumference of a circle
circum_of_circle = 2 * math.pi * radius

# Print out the results
print("Area of the circle:", area_of_circle)
print("Circumference of the circle:", circum_of_circle)

# Take radius as user input and calculate the area
user_radius = float(input("Enter the radius of the circle (in meters): "))
user_area_of_circle = math.pi * user_radius ** 2
print("Area of the circle with radius", user_radius, "is:", user_area_of_circle)
