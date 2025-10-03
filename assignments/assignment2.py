#1
print("Hello, "+input("What is your name? ")+"!")
#2
print(int(input("Circle's radius? "))**2*3.14)
#3
length=int(input("Length of rectangle? "))
width=int(input("Width of rectangle? "))
print(f'Perimeter: {(length+width)*2}'
      f'\nArea: {length*width}')
#4
ints=[]
products=lambda lis,count: lis[count-1]*products(lis,count-1) if count!=0 else 1
for i in range(3):
    ints.append(int(input(f'Int no. {i+1}: ')))
print(f'Sum: {sum(ints)}'
      f'\nProduct: {products(ints,3)}'
      f'\nAverage: {sum(ints)/3}')
#5
mass=float(input("Enter talents: "))*20*32*13.3
mass+=float(input("Enter pounds: "))*32*13.3
mass+=float(input("Enter lots "))*13.3
print(f'The weight in modern units: '
      f'\n{mass//1000} kilograms and {mass%1000} grams.')
#6
import random
lockgen=lambda size,start,end: str(random.randint(start,end))+lockgen(size-1,start,end) if size!=0 else ""
print(f'Random 3-digit code where each number is between 0 and 9:'
      f' {lockgen(3,0,9)}')
print(f'Random 4-digit code where each number is between 1 and 6:'
      f' {lockgen(4,1,6)}')