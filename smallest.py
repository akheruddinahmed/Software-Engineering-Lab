def find_smallest(numbers):
    if not numbers:
        return None
    return min(numbers)


numbers_input = input("Enter a list of numbers separated by spaces: ")


numbers_list = [int(num) for num in numbers_input.split()]

smallest = find_smallest(numbers_list)
if smallest is not None:
    print("Smallest number is:", smallest)
else:
    print("The list is empty.")
