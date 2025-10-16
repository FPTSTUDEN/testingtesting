N=[]
while (n:= (input("Enter a number: "))) != "":
    N.append(int(n))
print(sorted(N)[:-6:-1])