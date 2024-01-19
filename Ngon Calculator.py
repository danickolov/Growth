import math
def get_area_of_ngon(radius,side):
    return side*math.sin(math.radians(180/side))*math.cos(math.radians(180/side))*pow(radius,2)
r = float(input("Enter the radius of the n-gon: "))
n = int(input("Enter the number of sides in the n-gon: "))
number = get_area_of_ngon(r,n)
print("The area is " + str(number))