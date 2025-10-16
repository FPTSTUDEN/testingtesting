import random
#print(sum(random.sample(range(1, 6), n)))
print(sum([random.randint(1, 6) for _ in range(int(input("How many dice? ")))]))