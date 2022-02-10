print("Coding Exercise 7 ")

List = []
for i in range(1500, 2700, 1):
    if i % 5 == 0 or i % 7 == 0:
        List.append(i)
print(List)

fahrenheit = 45
celsius = 60


def fahrenheitToCelsius(x):
    return int((x - 32) * 5 / 9)


def celsiusToFahrenheit(x):
    return int((1.8 * x) + 32)


ans = 6
userInput = 0
print("Try guessing the number: ")
while userInput != ans:
    userInput = int(input())
    if userInput == ans:
        print("Well guess!")
    else:
        print("Wrong answer try again: ")


print(fahrenheitToCelsius(fahrenheit))
print(celsiusToFahrenheit(celsius))

n = 5
for i in range(n):
    for j in range(i):
        print("*", end="")
    print("")
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print("")

userInput = input("Please enter a word : ")
print("".join(userInput[::-1]))

numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
even = 0
odd = 0
for i in range(0, len(numbers), 1):
    if (i % 2) == 0:
        even += 1
    else:
        odd += 1

print("Number of even numbers: {}".format(even))
print("Number of odd numbers: {}".format(odd))

datalist = [
    1452,
    11.23,
    1 + 2j,
    True,
    "w3resource",
    (0, -1),
    [5, 12],
    {"class": "V", "section": "A"},
]
for i in range(0, len(datalist), 1):
    print("{0}  {1}".format(datalist[i], type(datalist[i])))

for i in range(0, 6):
    if i == 3 or i == 6:
        continue
    else:
        print("{} ".format(i), end="")
