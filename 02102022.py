from unittest import result

from pandas import period_range


print("Coding Exercise 8 :")


# 1.Create a function func() which prints a text ‘Hello World’
def printMessage():
    """Take no parameter.

    Prints Hello World
    """
    print("Hello World!")


printMessage()


# 2.Create a function which func1(name)
# which takes a value name and prints the output “Hi My name is Google’
def func2(name):
    """Take one parameter, user's name.

    Prints "My name is {userName}
    """
    print("My name is {}".format(name))


func2("Google")


# 3.Define a function func3(x,y,z) that takes three arguments x,y,z where z
#  is true it will return   x and when z is false it should return y .
#  func3(‘hello’goodbye’,false)
def func3(x, y, z):
    """Take three parameter, x = string1, y = string2, z = boolean.

    if Z is true, print out x
    else print y
    """
    if z is True:
        print(x)
    elif z is False:
        print(y)


func3("Hello", "World", False)


# 4.define a function func4(x,y) which returns the product of both the values.
def func4(x, y):
    """Take two parameter, x = value 1, y = value 2.

    returns the multiplication of x and y
    """
    return x * y


print(func4(5, 4))


# 5.define a function called as is_even that takes one argument ,
#   which returns true when even values is passed and false if it is not.
def is_even(x):
    """Take one parameter, x = value.

    returns true if x is even
    return false if x is odd
    """
    if x % 2 == 0:
        return True
    return False


print(is_even(10))


# 6.define a function that takes two arguments ,and returns true
#   if the first value is greater than the second value and returns false
#   if it is less than or equal to the second.
def is_greater(x, y):
    """Take one parameter, user's name.

    Prints "My name is {userName}
    """
    if x > y:
        return True
    return False


print(is_greater(10, 0))


# 7.Define a function which takes arbitrary number of arguments and
#   returns the sum of the arguments.
def sum(*args):
    """Take an unlimited amount of parameter, interger values.

        sum all of the values and return it
    """

    total = 0
    for a in args[0:]:
        total = total + a
    return total


print(sum(2, 5, 2, 5, 6, 7, 8, 3))


# 8.Define a function which takes arbitrary number of arguments and
#   returns a list containing only the arguments that are even.
def evenOnly(*args):
    """Take an unlimited amount of parameter, interger values.

        stores all of the even numbers into a list and return the list
    """
    result = []
    for a in args[0:]:
        if a % 2 == 0:
            result.append(a)
    return result


print(evenOnly(5, 2, 6, 7, 32, 234, 63, 23))


# 9.Define a function that takes a string and
#   returns a matching string where every even letter is
#   uppercase and every odd letter is lowercase
def weridCase(x):
    result = ""
    for i in range(len(x)):
        if i % 2 == 0:
            result = result = result + x[i].upper()
        else:
            result = result = result + x[i].lower()
    return result


print(weridCase("HOWS are You Doing?"))

# 10.Write a function which gives lesser than a given number
#    if both the numbers are even, but returns greater if one or both or odd.
def bothEvenOdd(x, y):
    """Take two parameter, x = value1 y = value2.

    Determines if either x or y is the greater and lesser value
    return the lesser value if both numbers
    """
    lesser = ""
    greater = ""
    if x < y:
        lesser = x
        greater = y
    else:
        lesser = y
        greater = x

    if x % 2 == 0 and y % 2 == 0:
        return lesser
    elif x % 2 == 1 and y % 2 == 1:
        return greater


print(bothEvenOdd(2, 4))


# 11.Write a function which takes  two-strings and returns true
# if both the strings start with the same letter.
def sameStartingLetter(x, y):
    """Take two parameter, x = string1 y = string2.

    Compares the first letter of x and y
    if they are the same letter
    return true
    else return false
    """
    if x[0] == y[0]:
        return True
    return False


sameStartingLetter("Hello", "World")


# 13.A function that
# capitalizes first and fourth character of a word in a string.
def capitalize(x):
    """Take one parameter, x = string.

    returns the string with 1st and 4th character captialized
    """
    result = "testing"
    if len(x) > 4:
        result = x[0].upper() + x[1:3] + x[3].upper() + x[4:]
        return result
    return


print(capitalize("hello world!"))

# Imagine an accounting routine used in a book shop.
# It works on a list with sublists, which look like this:
# Order Number	Book Title and Author	Quantity	Price per Item
#        34587	Learning Python, Mark Lutz	4	40.95
#        98762	Programming Python, Mark Lutz	5	56.80
#        77226	Head First Python, Paul Barry	3	32.95
#        88112	Einführung in Python3, Bernd Klein	3	24.99
# Write a Python program, which returns a list with 2-tuples.
# Each tuple consists of a the order number and the product of the price per items and the quantity.
# The product should be increased by 10,- € if the value of the order is smaller than 100,00 €.
# Write a Python program using lambda and map.

OrderNumber2Price = {34587: 40.95, 98762: 56.80, 77226: 32.95, 88112: 24.99}


def OrderNumberPrice(x):
    result = x.apply(lambda x: OrderNumber2Price[x])
    return result


print(OrderNumberPrice(34587))


# The same bookshop, but this time we work on a different list.
# The sublists of our lists look like this:
# [ordernumber, (article number, quantity, price per unit), ...
# (article number, quantity, price per unit) ]
# Write a program which returns a list of two tuples with
# (order number, total amount of order).
