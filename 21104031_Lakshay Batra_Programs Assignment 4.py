#Program for Question 1
#Program for Recursive python function to solve the problem of tower of Hanoi with three disks.
print("Question 1")
def Hanoi(n , fro , mid, to):
	if n == 0:
		return
	Hanoi(n-1, fro, mid, to)
	print("Move Disk ",n," from rod ",fro," to rod ",to)
	Hanoi(n-1, mid, to, fro)
#Calling Function For 3 Disks
print("For 3 disk:")
n = 3
Hanoi(n, 'A', 'C', 'B')
print("\n")

#Program for Question 2
#Python program to print the Pascal’s triangle for n number.
print("Question 2")
from math import factorial, remainder
from tracemalloc import start
n = int(input("Enter The Size Of The Pascal's Triangle: "))
# Using Recursions
print("By Recursion Method...")
def pascal_triangle(n,length = n):
    if n == 0:
        return
    pascal_triangle(n-1,length)
    print('  '*(length-n), end='')
    start = 1
    for i in range(1, n+1):
        print(start, end ='   ')
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")

# Using Iterations
print("By Iterative Method...")
for i in range(n):
	for j in range(n-i+1):
		print(end=" ")
	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
	print()
print("\n")

#Program for Question 3
#Program to input two integer values from user, calculate and print the quotient and reminder obtained from the two values.
print("Question 3")
inp1=int(input("Enter the first integer: "))
inp2=int(input("Enter the first integer: "))
#rem=Remainder
rem=inp1%inp2
#quo=Quotient
quo=inp1//inp2

#part <a>
print("\nPart A")
print("Checking if the quotient and remainder is a callable value or not.")
print(callable(quo))
print(callable(rem))

#part <b>
print("\nPart B")
if (quo == 0):
    print("The quotient is zero")
if (rem == 0):
    print("The reminder is zero")
if (quo != 0 and rem != 0):
    print("All the values are non zero")

#part <c>
print("\nPart C")
partClist = [quo + 4, rem + 4, rem + 5, quo + 5, rem + 5, quo + 6, rem + 6]
result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"Filtered out numbers that are greater than 4 are : {result}")

#part <d>
print("\nPart D")
setresult = set(result)
print("Set:", setresult)

#part <e>
print("\nPart E")
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("Immutable set:",immutableSet)

#part <f>
print("\nPart F")
print("Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")

#Program for Question 4
#Create a class named Student, use the_init_() function to assign values for name and roll number.
print("Question 4")
class Student:
    def __init__(self, student, roll_no):
        self.name = student
        self.roll_no = roll_no
    def __del__(self):
        print("Object Destroyed!")
student1 = Student("Lakshay Batra", 21104031)
print("Object Created...")
print(f"The Name Of The Student Is {student1.name} And SID Is {student1.roll_no}.")
del student1
print("\n")

#Program for Question 5
#Program to store details of three employees: name and salary using class.
print("Ouestion 5")
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)
#part <a> for updating salary
employee1.salary = 70000
print("\nPart A")
print(f"The updated salary of {employee1.name} is {employee1.salary} ")
#part <b> for deleting a record
print("\nPart B")
print("Record of Viren deleted", end='')
del employee3
print("\n")

#Program for QUestion 6
word1 = input("Enter Any Word: ")
word1 = word1.lower()
word2 = input("Enter A New Word Using The Exact Same Letters: ")
word2 = word2.lower()
def count_in_dict(word):
    count = {}
    list1 = list(word)
    n = len(list1)
    for i in range(n):
        if list1[i] in count:
            count[list1[i]] += 1
        else:
            count[list1[i]] = 1
    return count
def userinput():
    if count_in_dict(word1) != count_in_dict(word2):
        print("The Words Aren't Matching, Friendship Is Fake!")
        return
    ans = input("Does The Word Makes Any Sense?(Y Or N) ")
    if ans == 'y' or ans == 'Y':
        print("Passed The Friendship Test!!!")
    elif ans == 'n' or ans == 'N':
        print("Meaningless Word , Friendship Is Fake!")
    else:
        print("Invalid Input,Try Again! ")
        userinput()
userinput()