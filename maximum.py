def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)


numbers_input = input("Enter a list of numbers separated by spaces: ")

numbers_list = [int(num) for num in numbers_input.split()]

maximum = find_maximum(numbers_list)
if maximum is not None:
    print("Maximum number is:", maximum)
else:
    print("The list is empty.")
