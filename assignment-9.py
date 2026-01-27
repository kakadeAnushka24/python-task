# Q.1. Personal Information Collector 
# Sample Input  
# Enter full name: Raj Thakare 
# Enter age: 57 
# Enter gender: Male 
# Enter city: Mumbai 
# Enter state: Maharashtra 
# Enter country: India 
# Enter email: rajthackeray@gmail.com 
# Enter phone number: 8860300404  
# ...............................................................
name = input("Enter Full Name:")
age = input("Enter Age:")
gender = input("Enter Gender:")
city = input("Enter City:")
state = input("Enter State:")
country = input("Enter Country:")
email = input("Enter Your Email:")
phone = input("Enter Your Phone Number:")

print("\n..................PERSONAL INFORMATION CARD..................\n")
print("Full Name:",name)
print("Age",age)
print("Gender:",gender)
print("City:",city)
print("State:",state)
print("Country:",country)
print("Email",email)
print("Phone:",phone)
print("\n.............................\n")

# Q.2  Simple Billing System 
# Sample Input  
# Customer name: Rahul 
# Item 1 name: Pen 
# Item 1 price: 10 
# Item 2 name: Notebook 
# Item 2 price: 50 
# Item 3 name: Bag
# Item 3 price: 700 

customer = input("Enter customer name: ")

item1 = input("Item 1 name: ")
item1_price = float(input("Item 1 price: "))

item2 = input("Item 2 name:")
item2_price = float(input("Item 2 price: "))

item3 = input("Item 3 name: ")
item3_price = float(input("Item 3 price: "))

#  calculate Total Amount
total = item1_price + item2_price + item3_price

# Calculate GST (5%)
gst = total * 0.05

# Calculate Final Amount
final_amount = total + gst

print("\n===============================================")
print("\n--- BILL RECEIPT ---\n")
print("\n===============================================")
print("Customer Name :" , customer)
print("Item                            Price(Rs.)")
print("------------------------------------------")
print(f"{item1}                               {item1_price}")
print(f"{item2}                              {item2_price}")
print(f"{item3}                              {item3_price}")
print("-------------------------------------------")
print(f"Total Amount:                     {total}")
print(f"GST(5%):                          {gst}")
print(f"Final Amount:                     {final_amount}")
print("=================================================\n")

# Q.3 append() 
# 1. Write a program to add 10 user-entered integers into a list using append(). 
# 2. Append only even integers from 1 to 20 into a list. 
# 3. Append the square of each integer from an existing list into a new list. 
# 4. Take integer input until the user enters `0` and append each value to a list. 
# 5. Append elements of a tuple `(5, 10, 15)` one by one into a list.

# Q.1. Write a program to add 10 user-entered integers into a list using append(). 

# lst = []

# for i in range(10):
#     num = int(input("Enter Number: "))
#     lst.append(num)

# print(lst)

# Q.2. Append only even integers from 1 to 20 into a list. 
# lst = []

# for i in range(1, 21):
#     if i % 2 == 0:
#         lst.append(i)

# print(lst)

# Q.3. Append the square of each integer from an existing list into a new list. 


# old_list = [1, 2, 3, 4, 5]
# new_list = []

# for i in old_list:
#     new_list.append(i * i)

# print(new_list)



# clear() 
# 1. Write a program to clear all elements from an integer list. 
# 2. Clear a list only if it contains more than 5 integers. 
# 3. Display all elements of a list and then clear it. 
# 4. Clear a list and then add 3 new integer values to it. 
# 5. Clear a list inside a function and print the list outside the function.

# Q.1 Write a program to clear all elements from an integer list.
numlist = [10,20,30,40,50,60,70,80,90,100]
numlist.clear()
print(numlist)

# Q.2 Clear a list only if it contains more than 5 integers. 
numlist = [11,12,13,14,15]
if len(numlist)> 5:
    print(numlist)

# Q.3 Display all elements of a list and then clear it.
numlist = [9,8,7,6,5,4,3,2,1]
print("list before clear:",numlist)

numlist.clear()
print("list after clear:",numlist)

# Q.4 Clear a list and then add 3 new integer values to it.

numlist = [10,20,30,40,50,60] 
numlist.clear()
numlist.append(70)
numlist.append(80)
numlist.append(90)
print(numlist)

# Q.5 Clear a list inside a function and print the list outside the function.
def clear_list(mylist):
    mylist.clear
    list = [34,5,467,87,44,233,445,98]
    clear_list(list)
    print(list)



# copy() 
# 1. Copy all elements of one integer list into another list using copy(). 
# 2. Copy a list and add new integers to the copied list without affecting the original. 
# 3. Copy a list and remove an element from the copied list.


# Q.1 Copy all elements of one integer list into another list using copy(). 
numlist1 = [90,98,97,96,95,94,93]
numlist2 = numlist.copy()
print(numlist1)
print(numlist1)

# Q.2 Copy a list and add new integers to the copied list without affecting the original. 
numlist1 = [90,98,97,96,95,94,93]
numlist2 = numlist.copy()
numlist2.append(110)
numlist2.append(120)
print("Origanal List:",numlist1)
print("Copied List:",numlist2)


# Q.3 Copy a list and remove an element from the copied list.
numlist1 = [22,33,44,55,66,77,88,99]
numlist2 = numlist1.copy()
numlist2.remove(66)
print("Origanal List:",numlist1)
print("Copied List:",numlist2)


# count() 
# 1. Count how many times the integer 5 appears in a list. 
# 2. Count the occurrences of a user-entered integer in a list. 
# 3. Count how many times an even number appears in a list.

# Q.1 Count how many times the integer 5 appears in a list. 
numlist = [31,32,38,33,34,35,36,37,38,39,38]
print(numlist.count(38))

# Q.2 Count the occurrences of a user-entered integer in a list. 
numlist = [1,2,3,4,5,4,4,3,2,1,2,5,7,3,1,2,5]
num = int(input("Enter a number:"))
count = numlist.count(num)
print(count)

# Q.3 Count how many times an even number appears in a list.
numlist = [1,2,3,4,5,6,7,6,8,9,6,8]
count = 0
for num in numlist:
    if num % 2==0:
        count += 1
        print(count)


# extend() 
# 1. Extend a list with another integer list entered by the user. 
# 2. Extend a list using a tuple of integers. 
# 3. Extend an empty list with integers from range 1 to 5.

# Q.1 Extend a list with another integer list entered by the user.
# numlist1 = [1,2,3,4,5,6,7] 
# numlist2 = list(map(int,input("Enter Integer Sepreted by spece:".split())))
# numlist1.extend(numlist2)
# print("Extended list:",(numlist))










