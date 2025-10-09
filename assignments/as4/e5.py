U="python"
P="rules"
i=0
while i < 5:
    if (input("Username: ")==U and input("Password: ")==P):
        break # successful login
    print("Incorrect username or password")
    i += 1
else:
    print("Access denied")

print("Welcome")