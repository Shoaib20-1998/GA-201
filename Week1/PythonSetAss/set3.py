#problem1
data = [("John", 25), ("Jane", 30)]
for name, age in data:
    print(f"{name} is {age} years old.")


#problem2
ages = {"John": 25, "Jane": 30}

def add_person(name, age):
    ages[name] = age

def update_age(name, age):
    if name in ages:
        ages[name] = age

def delete_person(name):
    if name in ages:
        del ages[name]

# Add "John": 25
add_person("John", 25)
print(ages)  # Output: {'John': 25}

# Update "John": 26
update_age("John", 26)
print(ages)  # Output: {'John': 26}

# Delete "John"
delete_person("John")
print(ages)  # Output: {}


#problem3
def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []

nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1]


#problem4
def is_palindrome(word):
    reversed_word = word[::-1]
    if word == reversed_word:
        return True
    return False

word = "madam"
if is_palindrome(word):
    print(f"The word {word} is a palindrome.")
else:
    print(f"The word {word} is not a palindrome.")


#problem5
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [64, 25, 12, 22, 11]
sorted_arr = selection_sort(arr)
print(sorted_arr)  # Output: [11, 12, 22, 25, 64]


#problem6
from queue import Queue

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, data):
        self.q2.put(data)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: 1



#problem7
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")


#problem8
# with open("input.txt", "r") as file:
#     content = file.read()
#     word_count = len(content.split())

# with open("output.txt", "w") as file:
#     file.write(f"Number of words: {word_count}")


#problem9

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Cannot divide by zero.")

a = 5
b = 0
divide_numbers(a, b)  # Output: "Cannot divide by zero."


