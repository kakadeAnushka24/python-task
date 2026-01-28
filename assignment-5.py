# Q.1 Create a tuple with three fruits and print it.
fruits =("Apple","Banana","Mango")
print(fruits)

# Q.2 Create a tuple with one item Python  and print its type.
sub = ("python",)
print(type(sub))

# Q.3 Create a tuple of five numbers and print its length using len().
numlist = [1,2,3,4,5,6,7,8,9,0]
print(len(numlist))

# Q.4 Create a tuple and print its first element using indexing.
numlist = [1,2,3,4,5,6,7,8,9,0]
print(numlist[0])

# Q.5 Create a tuple and print its last element using negative indexing.
numlist = (20,40,5,9,10,45)
print(numlist[-1])

# Q.6 Create a tuple using the tuple() constructor with values 1 to 5 and print it.
numlist = ([1,2,3,4,5])
print(numlist)

# Q.7 Given t = (10, 20, 30, 40, 50) , print elements at index 1 and 3.
t = ([10,20,30,40,50])
print(t[1],t[3])

# Q.8 Given t = ("a","b","c","d","e") , print elements from index 1 to 4 using slicing.
t = ("a","b","c","d","e")
print(t[1:4])

# Q.9 From a tuple t = (5,10,15,20,25,30) , print elements from index 2 to end.
t = (5,10,15,20,25,30)
print(t[2:])

# Q.10 From a tuple t = (5,10,15,20,25,30) , print elements from start to index 3.
t = (5,10,15,20,25,30)
print(t[:3])

# Q.11 Create a tuple with mixed data types (int, float, string, boolean) and print it.
t = (10, 5.5, "Python", True)
print(t)

# Q.12 Check whether Python exists in a given tuple and print the result.
t = ("Java","Python","MongoDB")
print("Python" in t)

# Q.13 Convert a tuple to a list, add a new element, and print the updated list.
numlist = (1,2,3,4,5,6)
list1 = list(numlist)
list1.append(7)
print(list1)


# Q.14 Convert a list back into a tuple and print it.
numlist = (9,8,7,6,5,4,3,2,1)
list2 = tuple(numlist)
print(list2)

# Q.15 lCreate two tuples and concatenate them using += operator.
list3 = (10,20,30,40,50)
list4 = (60,70,80,90,100)
list3 += list4
print(list3)

# Q.16 Convert a tuple to list, change the second element, and convert back to tuple.
numlist = (10,20,30,14)
list11 = list(numlist)
print("Convert a tuple to list", list11)
list11[1] = 50
print("element added:",list11)
numlist11 = tuple(list1)
print("List converted into tuple is :",numlist11)

# Q.17 Create a tuple and access elements using both positive and negative indexing.
numlist = ("Sakshi","Mansi","Sanchita","Kajal")
print(numlist[0])
print(numlist[2])
print(numlist[-1])
print(numlist[-2])

# Q.18 Create a tuple of 7 elements and print its middle element.
numlist = (1,2,3,4,5,6,7)
print(numlist[3])

# # Q.19 Create a tuple and try to change one value directly (observe and write the error).
numlist = (1,2,3,4,)
t[0]=10
print(numlist)

# Q.20 Write a program that takes a tuple, converts it to list, replaces the last element, and converts back to tuple.
t = (10, 20, 30)
new_t = t[:-1] + (40,)
print(new_t)

# Q.21 Create a tuple of 10 numbers and extract the middle 5 elements using slicing.
t = (1,2,3,4,5,6,7,8,9,10)
print(t[2:7])

# Q.22 Write a program to check if a value exists in a tuple before accessing its index.
numlist = (10,34,57,98,36)
print(36 in numlist)

#Q.23 Create a tuple, convert it to list, remove one item, and convert it back to tuple.
namelist = ("Revati","Rajvi","Rama","Yaminii")
namelist = list(namelist)
namelist.remove("Rama")
namelist = tuple(namelist)
print(namelist)

# Q.24 Write a program that accepts a tuple, converts it to list, inserts a value at index 2, and converts back to tuple.
numlist = (23,24,25,26,27,28)
numlist =list(numlist)
numlist.insert(20,2)
numlist = tuple(numlist)
print(numlist)


# Q.25 Create a tuple and demonstrate slicing with positive and negative indexes in one program.
numlist = (7,6,5,4,7,8,9,3,2,9,87,5,6,67,66,5)
print(numlist[2:8])

# Q.26. Write a complete program that :-
# * creates a tuple
# * prints its length
# * accesses elements
# * slices it
# * converts to list
# * updates a value
# * converts back to tuple

numlist = (91,92,93,94,95,96,97,98,99,100)
print(len(numlist))
print(numlist[6])
print(numlist[2:4])
numlist = list(numlist)
numlist[2] = 82
numlist = tuple(numlist)
print(numlist)

# Q.27 Write a program that takes two tuples, adds them, and prints the final result.
numlist1 = (15,20,25,30,35,40)
numlist2 = (45,50,55,60,65,70)
print(numlist1 + numlist2)

# Q.28 Create a tuple, delete it using del , and then try to print it (observe the error).
numlist = (23,4,5,6,78,98,23)
del numlist
print(numlist)


# Q.29 A school stores a student’s basic details in a tuple because the data should not be changed accidentally.
#        The tuple contains: student = ("Rahul", 10, "A", 85.5)
#        Write a program to:
# 1. Print the student’s name and class using indexing.
# 2. Check whether "A" exists in the tuple.
# 3. Convert the tuple into a list, change the marks (85.5 → 90.0), and convert it back into a tuple.
# 4. Print the final updated tuple.
student = ("Rahul", 10, "A", 85.5)
print(student[0], student[1])
print("A" in student)
lst = list(student)
lst[3] = 90.0
student = tuple(lst)
print(student)

# Q.30. A customer’s selected product prices are stored in a tuple:
#       prices = (250, 500, 750, 1000, 1250)
#        Write a program to:
# 1. Print the total number of items using len().
# 2. Print the first and last price using positive and negative indexing.
# 3. Extract the middle three prices using slicing.
# 4. Convert the tuple into a list, add a new price 1500, and convert it back into a tuple.
# 5. Print the final tuple.
prices = (250, 500, 750, 1000, 1250)
print(len(prices))
print(prices[0],prices[1])
print(prices[1:4])
numlist = list(prices)
numlist.append(1500)
prices = tuple(numlist)
print(prices)


