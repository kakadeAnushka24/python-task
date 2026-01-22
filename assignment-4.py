# Consider this nested list for all questions:
# students = [ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]


#  Q1 Write the code to access the first student's name.  
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[0][0])

# Q2 Write the code to access Neha’s marks.
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[1][1])

# Q3  Write the code to access the grade of Rohit.
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[2][2])

# Q4 Write the code to print the entire second inner list.
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[1])

# Q5 Write the code to access Pooja’s name using negative indexing.
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[3][0])

# Q6 Write the code to access the last element of the first inner list.
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[0][-1])


# Q7 Write the code to print only the names of all students using indexing (without loop).
students =[ ["Amit", 85, "A"], ["Neha", 90, "A+"],  ["Rohit", 78, "B"],["Pooja", 88, "A"]]
print(students[0][0])
print(students[1][0])
print(students[2][0])
print(students[3][0])