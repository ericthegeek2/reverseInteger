def reverse_integer(n):
    # Convert the integer to a string, reverse it, and convert it back to an integer
    reversed_str = str(n)[::-1]
    reversed_int = int(reversed_str)
    return reversed_int

# Test the function
input_integer = 12345
reversed_integer = reverse_integer(input_integer)
print("Reversed integer:", reversed_integer)  # Output: Reversed integer: 54321
