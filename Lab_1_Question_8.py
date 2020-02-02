PI = 3.17
radius = float(input("Enter radius"))

def area(radius):
    return PI * (radius ** 2)

print("Aread of circle is " + str(area(radius)))