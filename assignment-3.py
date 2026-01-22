# Q1.Write a Python program to create a list of 5 student names and print it.

students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print(students)

# Q2 Write a program to find the length of a list using len().
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print(len(students))

# Q3 Create a list with mixed data types and print all elements one by one.
list = [10,"python",2.3,True,False,"anushka"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[5])

# Q4 Write a program to access the first and last element of a list.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print(students[0])
print(students[-1])

# Q5 Create a list and print the element using negative indexing.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print(students[-2])

# Q6 Write a program to check whether "Chetan" exists in a list.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print("Tanuja" in students)

# Q7 Write a program to change the second element of a list.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
students.insert(1,"Ishani")
print(students)

# Q8 Create an empty list and append three values to it.
list=[]
list.append("Tanuja")
list.append("Anushka")
list.append("Jayshree")
print(list)

# Q9 Write a program to remove the last element from a list.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
students.remove("Jayshree")
print(students)

# Q10 Create a list and clear all its elements using a method.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
students.clear()
print(students)

# Q11 Write a program to slice a list from index 2 to 5
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
print(students[3:5])


# Q12 Write a program to replace the first two elements of a list using range assignment.
students = ["Anushka","Tanuja","Bhakti","Rinal","Jayshree"]
students[0:2]=["Tanuja","Anushka"]
print(students)

#  Q13 Create two lists and join them using the + operator.
list1=[1,2,3]
list2=[4,5,6]
result=list1+list2
print(result)

# Q14 Write a program to insert an element at index 3 in a list.
list=[1,2,3,4,5,6,7]
list.insert(89,90)
print(list)

# Q15 Write a program to extend a list using:
# * another list
# * a tuplen
numlist=[23,45,67]
namelist=["Kunal","Dhanu","Rushi"]
numlist.extend(namelist)
print(numlist)

# * a tuplen
numtuple=(21,25)
namelist.extend(numtuple)
print(namelist)

# Q16 Write a program to remove a specific value from a list using remove().
namelist=["Vivansh","Rudra","Raya","Parth","Shivansh"]
namelist.remove("Rudra")
print(namelist)

# Q17 Write a program to sort a list of integers in ascending order.
numlist=[1,4,3,6,9,7,5,10]
numlist.sort()
print(numlist)

# Q18 Write a program to sort a list of integers in descending order.
numlist=[1,4,3,6,9,7,5,10]
numlist.sort(reverse=True)
print(numlist)

# Q19 Write a program to reverse a list using an inbuilt method.
numlist=[2,3,4,5,6,7,8,9,0]
numlist.reverse()
print(numlist)

# Q20 Write a program to copy a list using the copy() method and show that changes in the original list do not affect the copied list.
name1=["Vivansh","Rudra","Raya","Parth","Shivansh"]
name2=["Ragini","Dipti","Khushi","Vaishnavi","Dipa"]
name1=name2.copy()
print(name1)
name2.append("Samruddhi")
print(name1)

# Q21 Write a program to extend a list using a dictionary and print the result.
list=["Arti","Trisha","Tanvi"]
Dict={1:"Anushka",2:"Ishani",3:"Ishita"}
list.extend(Dict)
print(list)

# Q22 Write a program to demonstrate that list2 = list1 creates a reference, not a copy
list1=[11,12,13,14,15]
list2=list1
print(list1)
print(list2)
list1.append(44)
print(list1)
print(list2)

# Q23 Write a program to sort a list containing both uppercase and lowercase letters alphabetically.
list=["anushka","Tanuja","dipti","Ragini"]
list.sort()
print(list)

# Q24 Write a program to sort a list containing uppercase and lowercase letters together using key=str.lower.
list=["anushka","Tanuja","dipti","Ragini"]
list.sort(key=str.lower)
print(list)

#  Q25 Write a program to remove the element at index 4 using pop().
list=["Arti","Trisha","Tanvi","Anuja","Ragini"]
list.pop(4)
print(list)

# Q26 Write a program to delete the third element of a list using the del keyword.
list=[1,2,3,4,5,6,7,8,9]
del list[2]
print(list)

# Q27 Write a program to count how many times a specific value occurs in a list.
list=[1,2,3,4,5,6,7,8,9,9,8,3]
print(list.count(9))

# Q28 Write a program to find the index of a specific element in a list
list=[2,3,6,4,8,0,9,]
print(list.index(8))

# Q29 Write a program to add elements of a set to a list using extend().
list=[1,2,3,4]
set={5,6}
list.extend(set)
print(list)

# Q30. Write a program that performs the following operations on a list:
# # * append
# * insert
# * remove
# * sort
# * reverse

list=[3,7,9,0]
list.append(1)
print(list)

list=[3,7,9,0]
list.insert(12,10)
print(list)

list=[3,7,9,0]
list.remove(7)
print(list)

list=[3,7,9,0]
list.sort()
print(list)

list=[3,7,9,0]
list.reverse()
print(list)