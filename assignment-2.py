# Store your name & print using f-string
name = "Anushka Prakash Kakade"                   
print(f"My Name Is {name}")

# City name using string concatenation
city = "Nashik"
print("My city is " + city)

# Print Hello & World on new lines
print("Hello \n World")

# Sentence with single quote
print('It\'s My Book')

# Tab space between words
print("python \t language")

# Boolean value of 100
print (bool(100))

# Boolean value of 0
print (bool(0))

# Compare two numbers (>)
a = 10
b = 5
print(a > b)

# Add two numbers
a = 10
b = 5
print(a + b)

# Multiply two numbers
a =  10
b = 5
print(a * b)

# Remainder
a = 25
b = 4
print(a % b)

# Use += operator
x = 20
x = 10
print(x)

# Use += operator
x -= 5
print(x)

# Compare using ==
print(a == b)


# Logical AND
num = 15
print(num > 10 and num < 20)

# User input arithmetic
n1 = int(input("Enter Your First Number: "))
n2 = int(input("Enter Your Second Number: "))
print (n1 + n2)
print (n1 - n2)
print (n1 * n2)
print (n1 / n2)

# f-string name & age
name = "Anushka"
age = 22
print(f"My Name Is {name} and Age Is {age}")

# Check number > 50
num = int(input("Enter Number: "))
print(num > 50)

# Logical OR
print(num < 10 or num > 100)

# Logical NOT
print(not(num > 50))

# Identity operator is
a = [1 , 2]
b = a
print(a is b)

# Identity operator is not
c = [1,2]
print(a is not c)

# Bitwise AND
print(5 & 3)

# Bitwise OR
print(7 | 4)

# Bitwise XOR
print(6 ^ 2)

# Operator precedence
a = 2
b = 5
c = 2
print(a + b * c - a // b ** 2)

# Greater than 10 AND even
num = int(input("Enter Number: "))
print(num > 10 and num % 2 == 0)

# List identity
list1= [10 , 20]
list2 = list1
print(list1 is list2)

# Binary + Bitwise
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Binary of x =", bin(x))
print("Binary of y =", bin(y))

print("Bitwise AND (&) Output =", x & y)
print("Bitwise OR (|) Output  =", x | y)
print("Bitwise XOR (^) Output =", x ^ y)

# All operators in one program
p = int(input("Enter number 1: "))
q = int(input("Enter number 2: "))

p += 2

print("Addition:", p + q)
print("Comparison:", p > q)
print("Logical AND:", p > 10 and q < 20)
print("Multiplication:", p * q)
print("Difference:", p - q)