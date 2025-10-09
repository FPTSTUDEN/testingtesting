import random
randomnum=random.randint(1,10)
while guessed:=int(input("Enter a number between 1 and 10: "))!=randomnum:
    print("Too high") if guessed>randomnum else print("Too low")
print("Correct!")