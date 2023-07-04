# 1
print("Hello, World!")


#2
integer_var = 10
float_var = 3.14
string_var = "Hello, World!"
boolean_var = True
list_var = [1, 2, 3]
tuple_var = (4, 5, 6)
dictionary_var = {"name": "John", "age": 25}
set_var = {7, 8, 9}

variables = [integer_var, float_var, string_var, boolean_var, list_var, tuple_var, dictionary_var, set_var]
for var in variables:
    print(f"Type of {var}: {type(var)}, value: {var}")


#3
numbers = list(range(1, 11))
print(numbers)

numbers.append(20)
print(numbers)

numbers.remove(3)
print(numbers)

#4
numbers = [10, 20, 30, 40]
total = sum(numbers)
average = total / len(numbers)
print(f"Sum: {total}, Average: {average}")


#5
def reverse_string(input_string):
    return input_string[::-1]

input_string = "Python"
reversed_string = reverse_string(input_string)
print(reversed_string)

#6
def count_vowels(input_string):
    vowel_count = 0
    vowels = "aeiouAEIOU"
    for char in input_string:
        if char in vowels:
            vowel_count += 1
    return vowel_count

input_string = "Hello"
num_vowels = count_vowels(input_string)
print(f"Number of vowels: {num_vowels}")


#7
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

num = 13
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")


numbers.sort()
print(numbers)


#8
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

num = 5
result = factorial(num)
print(f"Factorial of {num} is {result}.")

#9
def fibonacci(n):
    sequence = [0, 1]
    if n <= 2:
        return sequence[:n]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

n = 5
fib_sequence = fibonacci(n)
print(fib_sequence)


#10

squared_numbers = [num**2 for num in range(1, 11)]
print(squared_numbers)

