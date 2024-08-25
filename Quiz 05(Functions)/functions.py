# 1. Function to check if a number is even or odd
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# Example usage:
# check_even_odd(5)

# 2. Function to return the maximum of three numbers
def maximum_of_three(num1, num2, num3):
    return max(num1, num2, num3)

# Example usage:
# print(maximum_of_three(4, 9, 2))

# 3. Function to reverse a word or sentence
def reverse_input():
    user_input = input("Enter a word or sentence: ")
    reversed_input = user_input[::-1]
    print(f"Reversed: {reversed_input}")

# Example usage:
# reverse_input()

# 4. Function to count vowels in a string
def count_vowels(input_string):
    vowels = 'aeiou'
    count = sum(1 for char in input_string.lower() if char in vowels)
    return count

# Example usage:
# print(count_vowels("Hello World"))

# 5. Function to return a list of even numbers from the input list
def filter_even_numbers(numbers_list):
    even_numbers = [num for num in numbers_list if num % 2 == 0]
    return even_numbers

# Example usage:
# print(filter_even_numbers([1, 2, 3, 4, 5, 6]))
