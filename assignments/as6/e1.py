import random
def dice(): return random.randint(1,6)
def mainprogram():
    while (ans:=dice())!=6:
        print(ans)
    print(6) #final result is 6 anyways lol
mainprogram()