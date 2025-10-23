while (g:= float(input("Gasoline in American gallons: "))) >=0:
    gtol=lambda g: g * 3.78541
    l = gtol(g)
    print(f"Gasoline in liters: {l:.2f}")