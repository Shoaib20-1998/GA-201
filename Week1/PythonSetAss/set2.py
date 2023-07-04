#Problem 1: Print the following pattern

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()


#Problem 2:
numbers = [12, 75, 150, 180, 145, 525, 50]
for num in numbers:
    if num > 500:
        break
    if num % 5 == 0 and num <= 150:
        print(num)



#Problem 3:
s1 = "Ault"
s2 = "Kelly"
middle_index = len(s1) // 2
s3 = s1[:middle_index] + s2 + s1[middle_index:]
print(s3)



#Problem 4:
str1 = "PyNaTive"
lowercase_chars = ""
uppercase_chars = ""
for char in str1:
    if char.islower():
        lowercase_chars += char
    else:
        uppercase_chars += char
arranged_str = lowercase_chars + uppercase_chars
print(arranged_str)


#Problem 5:
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
result = [x + y for x, y in zip(list1, list2)]
print(result)


#Problem 6:
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
result = [x + y for x in list1 for y in list2]
print(result)


#Problem 7:
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
for x, y in zip(list1, reversed(list2)):
    print(x, y)


#Problem 8:
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
result = {employee: defaults for employee in employees}
print(result)


#Problem 9:
sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New York"
}
keys = ["name", "salary"]
result = {key: sample_dict[key] for key in keys}
print(result)

#Problem 10:
tuple1 = (11, [22, 33], 44, 55)
tuple1[1][0] = 222
print(tuple1)


