def remove_uneven(lst):
    return [x for x in lst if x % 2 == 0]
def main_program():
    numbers = [int(i) for i in input("Enter numbers separated by spaces: ").split()]
    print(f'Initial list: {numbers}')
    even_numbers = remove_uneven(numbers)
    print(f'Even numbers: {even_numbers}')

main_program()
