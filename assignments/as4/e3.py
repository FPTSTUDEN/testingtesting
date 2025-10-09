m,M=-float("inf"),float("inf")
s=" "
while (s:=input("Enter a number: "))!="":
    n=int(s)
    m=max(m,n)
    M=min(M,n)
print(f"Max: {m}, Min: {M}")