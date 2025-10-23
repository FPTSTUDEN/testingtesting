def Sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def mainprogram():
    nums = [int(i) for i in input("Enter numbers separated by spaces: ").split()]
    s=Sum(nums)
    print(f"The sum is: {s}")
mainprogram()