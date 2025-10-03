# Write a program that asks a fisher the length of a zander in centimeters. If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters or longer to meet the size limit.

# Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written description according to the list below. You must use an if/elif/else structure in your solution.

# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.

# Write a program that asks for the user's biological sex and hemoglobin value (g/l). The program the notifies the user if the hemoglobin value is low, normal or high.

# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.
# Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year. A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.
#1
z=input("length of zander: ")
print(f"Please release the fish back into the lake. The fish was {42-int(z)} cm below the size limit") if int(z)<42 else print("The fish meets the size limit")
#2
c=input("cabin class: ")
if c=="LUX":
    print("upper-deck cabin with a balcony.")
elif c=="A":
    print("above the car deck, equipped with a window.")
elif c=="B":
    print("windowless cabin above the car deck.")
elif c=="C":
    print("windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
#3
s=input("biological sex: ")
h=int(input("hemoglobin value (g/l): "))
if s=="female":
    hrange=range(117,156)
elif s=="male":
    hrange=range(134,168)
if h in hrange:
    print("normal")
elif h<min(hrange):
    print("low")
else:
    print("high")
#4
y=int(input("year: "))
if (y%4==0 and y%100!=0) or (y%400==0): #%400 included %100
    print("leap year")
else:
    print("not a leap year")
#small change
#another small change