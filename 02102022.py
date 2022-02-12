from operator import truediv


print("Coding Exercise 8 :")


def printMessage():
    print("Hello World!")


printMessage()


def func2(name):
    print("My name is {}".format(name))


func2("Google")


def func3(x, y, z):
    if z == True:
        print(x)
    elif z == False:
        print(y)


func3("Hello", "World", False)


def func4(x, y):
    return x * y


print(func4(5, 4))


def is_even(x):
    if x % 2 == 0:
        return True
    return False


print(is_even(10))


def is_greater(x, y):
    if x > y:
        return True
    return False


print(is_greater(10, 0))


def bothEvenOdd(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return ">"
    elif x % 2 == 1 and y % 2 == 1:
        return "<"


print(bothEvenOdd(2, 4))


def sameStartingLetter(x, y):
    if x[0] == y[0]:
        return True
    return False


sameStartingLetter("Hello", "World")


def capitalize(x):
    if len(x) > 4:
        x[0] = x[0].upper()
        x[3] = x[3].upper()
        return x
    return


print(capitalize("hello world!"))
