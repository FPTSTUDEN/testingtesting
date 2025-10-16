n = int(input("Enter a number: "))
def prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
print(f'{n} is {"" if prime(n) else "not "}a prime number')