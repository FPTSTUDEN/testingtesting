
import random


N=int(input("Number of random points: "))
R=(int(N**0.5)+1)/2
n=0
for _ in range(N):
    x,y=random.uniform(-R,R),random.uniform(-R,R)
    if x**2+y**2<R**2: n+=1
print(f"Approximation of pi: {4*n/N}")