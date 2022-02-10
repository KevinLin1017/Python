print("Coding Exercise 2: \n")
print("1. 50 + 50 = " + str(50 + 50))
print("2. 100 - 10 = " + str(100 - 10))
# print(30+*6)
print("3. " + str(6 ^ 6))  # ^ is an XOR operator
print("4. " + str(6**6))  # ** is an exponent operator
print("5. " + str(6 + 6 + 6 + 6 + 6 + 6))
print("6. Hello World")
print("7. Hello World : 10 \n")


# Mortgage algorithm
P = 800000  # Loan size
R = 6 / 100 / 12  # Interest Rate = Rate / 100 percent / 12 months
L = 103  # Duration of the Loan in Months

M = P * ((R * ((1 + R) ** L)) / ((1 + R) ** L - 1))

print("input data:")
print(str(P) + " " + str(int(R * 1200)) + " " + str(L) + "\n")
print("answer: ")
print(str(round(M)))
