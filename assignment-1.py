# store name in a variable and print it
name = "Anushka Kakade"
print(name)

# program to print the length of the string "Python"
text = "Python"
print(len(text))

# program to access and print the first character of the string "Karan".
name = "Karan"
print(name[0])

# program to convert the string "Maharashtra" into uppercase.
state = "Maharashtra"
print(state.upper())

#  program to convert the string "Maharashtra" into lowercase.
state = "Maharashtra"
print(state.lower())

# program to remove extra spaces from the string " Hello Python ".
text = " Hello Python "
print(text.strip())

#  program to check whether "rashtr" is present in "Maharashtra"
text = "Maharashtra"
print("rashtr" in text)

#  a program to concatenate two strings "Hello" and "World"
a = "Hello"
b = "World"
print(a + " " + b)

#  program to print each character of the string "India" using indexing.
text = "India"
print (text[0])
print (text[1])
print (text[2])
print (text[3])
print (text[4])

#  program to print a multiline string using triple quotes
text = """Hello
Welcome to
Python"""
print(text)

# program to print the last character of the string "Python"
text = "Python"
print(text[-1])

# program to slice and print the first 4 characters of "Maharashtra"
text = "Mharashtra"
print(text[0:4])

# program to print the string "Maharashtra" starting from index 3 till the end
text = "Maharashtra"
print (text[3:])

#  a program to print characters of "Maharashtra" by skipping every second character.
text = "Maharashtra"
print (text[::2])

#  program to check whether "text" is not present in "Maharashtra"
text = "Maharashtra"
print("text" not in text)

#  program to replace all occurrences of "a" with "A" in "Hello Maharashtra".
text = "Hello Maharashtra"
print(text.replace("a","A"))

# program to split the string "Hello Maharashtra proud to be your son" into a list.
text = "Hello Maharashtra Proud to be your son"
print (text.split())

#  program to reverse the string "Karan" using slicing.
name = "karan"
print (name[::-1])

# program to print the middle character of the string "Python".
text= "Python"
print(text[3:4])


# program to print the length of a string after removing extra spaces from both ends.
text = "Hello Python"
clean = text.strip()
print (len(clean))

# program to reverse a string without using any inbuilt method (use slicing only).
text = "python"
print (text[::-1])

# Count "a" in "Maharashtra"
text = "Maharashtra"
print (text.count("a"))

# Extract "rashtr" from "Maharashtra"
text = "Maharashtra"
print (text[3:9])

# Reverse "Maharashtra" using step -1
text = "Maharashtra"
print(text[::-1])

# Print alternate characters from "Programming"
text = "Programming"
print(text[::2])

# Remove starting and ending spaces
text = "      Hello Maharashtra         "
print(text.strip())

# Print characters from index -5 to -1
text = "Maharashtra"
print(text[-5:-1])

# Print each word on new line
print("Python\n is \n very \n easy")