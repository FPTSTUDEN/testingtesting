import random
def dice(sides): return random.randint(1,sides)
def mainprogram(sides):
    while (ans:=dice(sides))!=sides:
        print(ans)
    print(sides) #final result is 6 anyways lol
sides=int(input("Number of dice sides: "))
mainprogram(sides)