# Q.1 Create a set with 5 integer values and print it.
s = {1,2,3,4,5}
print(s)

# Q.2 Create a set using the set() constructor from a list.
numset = [4,5,6,7,8,9]
s = set(numset)
print(s)

# Q.3 Create a set with duplicate values and print the result.
numset = {1,2,2,3,3,4,4,5,6,7,7,8,9}
print(numset)

# Q.4 Create a set containing True and 1. Print the set.
numset = {True , 1}
print(numset)

# Q.5 Write a program to find the length of a set using len().
numset = {12,34,5,4,67,8,89,00,87,6,6}
print(len(numset))

# Q.6 Create a set with mixed data types and print it.
numset = {1, "Hello",9.8,True}
print(numset)


# Q.7 Write a program to access set elements using a for loop.
numset = {23,56,998,76,5,54,45,67,90}
for i in numset:
 print(numset)

#  Q.8 Create an empty set and add three elements using add().
numset = set()
numset.add(10)
numset.add(20)
numset.add(30)
print(numset)

# Q.9 Write a program to remove an element from a set using discard().
numset = {21,22,23,24,25}
numset.discard(22)
print(numset)

# Q.10 Write a program to remove an element from a set using remove().
numset = {12,23,4,45,6,7,89,76,00}
numset.remove(00)
print(numset)

# Q.11 Write a program that removes a non-existing element using discard()
numset = {23,45,67,89,98,76,54}
numset.discard(44)
print(numset)

# Q.12 Write a program that removes a non-existing element using remove() and observe the error.
# numset = {2,3,4,5,6,7,8,9,1}
# numset.remove(10)
# print(numset)

# Q.13 Write a program to remove a random element from a set using pop().
numset = {12,23,45,43,54,23,46,77,89}
numset.pop()
print(numset)

# Q.14 Write a program to clear all elements from a set using clear().
numset = {10,20,30,40,50}
numset.clear()
print(numset)

# Q.15 Write a program to delete a set completely using del.
numset = {98,87,76,65,54,32,12}
del numset
# print(numset)

# Q.16 Write a program to combine two sets using union().
numset1 = {1,2,3,4,5}
numset2 = {6,7,8,9,0}
print(numset1.union(numset2))

# Q.17 Write a program to combine two sets using the | operator.
numset1 = {81,82,83,84,85}
numset2 = {86,87,88,89,90}
print(numset1 | numset2)

# Q.18 Write a program to update one set using another set with update()
numset1 = {2,3,4,5,6}
numset2 = {0,9,8,7,3}
numset1.update(numset2)
print(numset1)

# Q.19 Write a program to join a set with a list using union()
numset1 = {1,3,5,7,9}
s = {2,4,6,8,10}
print(numset1.union(s))

# Q.20 Write a program to join three sets using union().
numset1 = {1,2,3,4}
numset2 = {5,6,7,8}
numset3 = {9,10,11,12}
print(numset1.union(numset2,numset3))

# Q.21 Write a program to find common elements between two sets using intersection().
numset1 = {23.34,35,674,43,22,23,54}
numset2 = {23,45,768,935,85,22,14,89}
print(numset1.intersection(numset2))

# Q.22 Write a program to find common elements between two sets using the & operator.
numset1 = {23.45,35,674,43,22,23,54}
numset2 = {23,45,768,54,85,22,14,89}
print(numset1 & numset2 )

# Q.23 Write a program to find intersection between a set and a list using intersection().
numset1 = {22,23,34,56,78,76}
numset2 = {98,34,76,89,88,65}
print(numset1.intersection(numset2))

# Q.24 Write a program to update a set using intersection_update().
numset1 = {100,200,300,400,500,700}
numset2 = {600,700,800,900,1000,500}
numset1.intersection_update(numset2)
print(numset1)

# Q.25 Write a program to find elements present in first set but not in second using difference().
numset1 = {0,9,8,7,6,5,4}
numset2 = {5,4,3,2,1,6,9}
print(numset1.difference(numset2))

# Q.26 Write a program to find difference between two sets using the - operator.
numset1 = {0,9,8,7,6,5,4,70,100,20}
numset2 = {5,4,3,2,1,6,9,100,20,6,9}
print(numset1 - numset2)

# Q.27 Write a program to update a set using difference_update()
numset1 = {0,9,8,7,6,5,4,70,100,20}
numset2 = {5,4,3,2,1,6,9,100,20,6,9}
numset1.difference_update(numset2)
print(numset2)

# Q.28 Write a program to find symmetric difference using symmetric_difference().
numset1 = {7,6,5,4,70,100,20}
numset2 = {2,1,6,9,100,20,6,9}
numset1.symmetric_difference(numset2)
print(numset2)

# Q.29 Write a program to find symmetric difference using the ^ operator.
numset1 = {7,6,5,4,70,100,20}
numset2 = {2,1,6,9,100,20,6,9}
numset1^(numset2)
print(numset2)

# Q.30 Write a program to perform union, intersection, difference, and symmetric difference on two sets and print all results.
numset1 = {91,92,93,94,95,96,97,98,99,100}
numset2 = {100,101,102,103,104,97,105,106,107}
print("union:",numset1 | numset2)
print("Intersection:",numset1 & numset2)
print("Difference:",numset1 - numset2)
print("Symmetric difference:",numset1 ^ numset2)