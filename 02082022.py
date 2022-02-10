import re

print("Coding Exercise 3: \n")
print("1. " + "Hello World"[8])
print("2. " + "thinker"[2:5])
s = "hello"
print("3. " + s[1])
s = "Sammy"
print("4. " + s[2:])
print("5. " + "".join(set("Mississippi")) + "\n")


def isPalindrome(s):
    p = re.sub("[!@#$, ]", "", s[::-1]).upper()
    q = re.sub("[!@#$, ]", "", s).upper()
    if q == p:
        print("Y", end=" ")
    else:
        print("N", end=" ")


a = "stars"
b = "O, a kak Uwakov lil vo kawu kakao!"
c = "Some men interpret nine memos"

print("input data : ", "3", a, b, c, "answer: ", sep="\n")
isPalindrome(a)
isPalindrome(b)
isPalindrome(c)


print("\n \n  Coding Exercise 4: \n")

a = [1, "hello world!", 2.5]
print("1. ", a)
b = [[1, 1, [1, 2]]]
print("2. ", b[0][2][1])
lst = ["a", "b", "c"]
print("3. ", lst[1:])
weekdays = {"monday": 1, "tuesday": 2, "wednesday": 3, "thursday": 4, "friday": 5}
print("4. {}".format(weekdays))
D = {"k1": [1, 2, 3]}

print("\n \n  Coding Exercise 6: \n")


def crowd_test(s):
    if len(s) >= 3:
        print("The room is crowded")
    else:
        pass


s = ["Amber", "Alan", "Mark", "Sammy"]
crowd_test(s)
s.pop()
s.pop()
crowd_test(s)
