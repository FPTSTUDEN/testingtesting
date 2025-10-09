U="python"
P="rules"
i=0
while i < 5:
    u=input("Username: ")
    p=input("Password: ")
    if (u==U and p==P):
        break # successful login
    print("Incorrect username or password")
    i += 1
# else:
#     print("Access denied")

print("Welcome") if i<5 else print("Access denied")