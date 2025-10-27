seasons=("spring", "summer", "autumn", "winter")
month=int(input("Enter month number (1-12): "))
if month in [12, 1, 2]:
    print(seasons[3])  # winter
elif month <=5:
    print(seasons[0])  # spring
elif month <= 8:
    print(seasons[1])  # summer
else:
    print(seasons[2])  # autumn