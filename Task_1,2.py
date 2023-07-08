import math
radius = float(input("Enter the radius of the circle: " ))
area = math.pi * radius * radius
print(f"Area of the circle is for a radius {radius} : {area}")



File_name = input("Enter the file name : ")
extension = File_name.split(".")
print("Extension of the file : ", 'python' if extension[-1]=='py' 	else extension[-1])