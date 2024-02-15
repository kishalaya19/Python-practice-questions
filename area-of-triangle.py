def area(b,h):
    ar = 0.5*b*h
    return ar

b = int(input("Enter base: "))
h = int(input("Enter height: "))
area_result = area(b, h)
print(f"Area of the triangle is {area_result}")