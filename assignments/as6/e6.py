def unit_price(p_diameter, p_price):
    r=p_diameter/2
    area=3.14159*r*r
    return p_price/(area/100/100) # price per square meter
def main_program():
    d1,p1= [float(i) for i in input("Enter diameter (cm) and price of first pizza separated by space: ").split()]
    d2,p2= [float(i) for i in input("Enter diameter (cm) and price of second pizza separated by space: ").split()]
    up1=unit_price(d1,p1)
    up2=unit_price(d2,p2)
    if up1 < up2:
        print(end="First")
    elif up2 < up1:
        print(end="Second")
    else:
        print(end="Both")
    print(" pizza is/are the better deal.")
main_program()