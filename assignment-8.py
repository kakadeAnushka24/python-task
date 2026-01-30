# Q.1 Create a dictionary with keys name, rollNo, and address and print it.
data = {"name":"Anushka","rollNo":21,"address":"Rahuri"}
print(data)

# Q.2 Write a program to access and print the value of key name from a dictionary.
data = {"name":"Anushka","rollNo":21,"address":"Rahuri"}
print(data["name"])

# Q.3 Create a dictionary and print its length using len().
data = {"name":"Anushka","rollNo":21,"address":"Rahuri"}
print(len(data))

# Q.4 Write a program to check the type of a dictionary using type().
data = {"name":"Anushka","rollNo":21,"address":"Rahuri"}
print(type(data))

# Q.5 Create a dictionary with two keys and print all its values.
data = {"a":1,"b":2,"c":3}
print(data.values())

# Q.6 Create a dictionary and access values using both [] and get() methods.
data = {"name":"Anuuu","age":22}
print(data["name"])
print(data["age"])

# Q.7 Write a program to add a new key-value pair to an existing dictionary.
data = {"a":1,"b":22,"c":23}
data["d"] = 24
print(data)

# Q.8 Create a dictionary and update one value using the update() method.
data = {"a":1,"b":2,"c":3,"d":4}
data.update({"d":5})
print(data)

# Q.9 Write a program to remove a key using the pop() method.
data = {"a":1,"b":2,"c":3,"d":4}
data.pop("c")
print(data)

# Q.10 Create a dictionary and remove the last inserted item using popitem()
data = {"a":11,"b":22,"c":33,"d":44}
data.popitem()
print(data)

# Q.11 Write a program to print all keys using the keys() method.
data = {"a":21,"b":22,"c":23,"d":24}
print(data.keys())

# Q.12 Write a program to print all values using the values() method
data = {"a":21,"b":22,"c":23,"d":24}
print(data.values())

# Q.13 Create a dictionary and print all key-value pairs using items().
data = {"a":21,"b":22,"c":23,"d":24}
print(data.items())

# Q.14 Convert a tuple of key-value pairs into a dictionary using dict()
data1 = (("a",1),("b",2))
data2 = dict(data1)
print(data2)


# Q.15 Write a program to check if a key exists in a dictionary.
data = {"a":11,"b":22,"c":33}
print("a" in data)

# Q.16 Create a dictionary with duplicate keys and print the output.
data = {"a":11,"a":12,"b":22,"c":33}
print(data)

# Q.17 Write a program to delete a specific key using the del keyword
data = {"a":100,"b":200,"c":300,"d":400}
del data["c"]
print(data)

# Q.18 Write a program to delete the entire dictionary using del.
# data = {"a":100,"b":200,"c":300,"d":400}
# del data
# print(data)

# Q.19 Create a dictionary and empty it using the clear() method.
data = {"a":100,"b":200,"c":300,"d":400}
data.clear()
print(data)

# Q.20 Copy a dictionary using the copy() method and show both dictionaries.
data1 = {"a":100,"b":200,"c":300,"d":400}
data2 = data1.copy()
print(data2)

# Q.21 Copy a dictionary using the dict() constructor and modify the original dictionary.
data1 = {"a":21,"b":22,"c":23,"d":24}
data2 = dict(data1)
data1["a"] = 25
print(data1)
print(data2)

# Q.22 Write a program to demonstrate why dict1 = dict2 is not a proper copy.
dict1 = {"a":21,"b":22,"c":23,"d":24}
dict2 = dict1
dict1["a"] = 200
print(dict1)
print(dict2)

# Q.23 Create a dictionary and add multiple items using assignments.
data = {}
data["a"] = 20
data["b"] = 30
data["c"] = 40
print(data)

# Q.24 Write a program to remove multiple keys one by one using pop()
data = {"a":21,"b":22,"c":23,"d":24}
data.pop("b")
data.pop("c")
print(data)

# Q.25 Use fromkeys() to create a dictionary with default values.
data = {"a","b","c","d"}
new=dict.fromkeys(data,21)
print(new)

# Q 26 Write a program to access a missing key using get() without error.
data = {"a":101,"b":102,"c":103,"d":104}
print(data.get("e"))

# Q.27 Create a dictionary and print key-value pairs in tuple form
data = {"a":11,"b":22,"c":33}
for item in data.items():
    print(item)

# Q.28 Write a program to update multiple values using update().
data = {"a":11,"b":22,"c":33}
data.update({"a":22,"b":42})
print(data)

# Q.29 Create a dictionary and check membership of a key using in.
data = {"a":61,"b":62}
print("a" in data)
print("b" in data)

# Q.30  Write a program that creates a dictionary from tuples and accesses values using keys.
data = (("name","Anuuu"),("age",22))
data = dict(data)
print(data["name"])
print(data["age"])

# Q31. Write a program that performs the following operations on a list:
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


# Q.31 All operators in one program
p = int(input("Enter number 1: "))
q = int(input("Enter number 2: "))

p += 2

print("Addition:", p + q)
print("Comparison:", p > q)
print("Logical AND:", p > 10 and q < 20)
print("Multiplication:", p * q)
print("Difference:", p - q)
