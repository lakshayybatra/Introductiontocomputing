#Program for Question 1
#Python program to count the number of occurrences of each word or character in the string entered by the user.
print("Question 1")
a=str(input("ENTER ANY STRING: "))
list=a.split()
dict={}
if list.__len__()==1:
    for i in list[0]:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    print(dict)
#End of program 1
print("\n")

#Program for Question 2
#Python script to print next date of input date
print("Question 2")
def input_date():
    global day
    global month
    global year
    day = int(input("Day(enter a value from 1 to 31)-"))
    month = int(input("Month(enter a value from 1 to 12)-"))
    year = int(input("Year(enter a value from 1800 to 2025)-"))
    if year > 2025 or year < 1800 or month < 1 or month > 12 or day < 1 or day > 31:
        print("Please Re-enter A Valid Date OR Only Enter A Year Between 1800 and 2025")
        input_date()
    if day > 28 and month == 2 and year % 4 != 0:
        print("Please Re-enter A Valid Date!!")
        input_date()
    elif day > 28 and month == 2 and year % 4 == 0 and year%100 == 0:
        print("Please Re-enter A Valid Date!!")
        input_date()
    elif ((day > 29 and month == 2) and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)):
        print("Please Re-enter A Valid Date!!")
        input_date()
    elif day > 30 and month in [4, 6, 9, 11]:
        print("Please Re-enter A Valid Date!!")
        input_date()
input_date()
if (month in [1,3,5,7,8,10] and day==31):
    day=1
    month=month+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month in [1,3,5,7,8,10] and 1<=day<=30):
    day=day+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month in [4,6,9,11] and day==30):
    day=1
    month=month+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month in [4,6,9,11] and 1<=day<=29):
    day=day+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==2 and day==28 and year%4==0 and year%100!=0):
    day=29
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==2 and day==29 and year%4==0 and year%100!=0):
    day=1
    month = month + 1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==2 and day==28 and year%100==0 and year%400==0):
    day = 29
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==2 and day==29 and year%100==0 and year%400==0):
    day = 1
    month = month + 1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month == 2 and day == 28):
    day = 1
    month = month + 1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==2 and 1<=day<=27):
    day=day+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==12 and day==31):
    day=1
    month=1
    year=year+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
elif (month==12 and 1<=day<=30):
    day=day+1
    print("Next Date is:", day, end="")
    print("/", month, end="")
    print("/", year)
#End of program 2
print("\n")

#Program for Question 3
#Python program to create a list of tuples
print("Question 3")
list=[]
num_elemets= int(input("Enter number of elements to be entered in the list:"))
for ele in range(0, num_elemets):
    element= int(input("Enter the element:"))
    list.append(element)
print(list)
list_of_tuples=[]
for i in list:
    tuple=(i,i**2)
    list_of_tuples.append(tuple)
print(list_of_tuples)
#End of program 3
print("\n")

#Program for Question 4
#Program to prompt the user for a grade between 4 and 10
print("Question 4")
grade=int(input("Enter grade points:"))
if (4<=grade<=10):
    if(grade==4):
        print("Your Grade is ‘D’ and Poor Performance.")
    elif(grade==5):
        print("Your Grade is ‘C’ and Below Average Performance.")
    elif(grade==6):
        print("Your Grade is ‘C+’ and Average Performance.")
    elif(grade==7):
        print("Your Grade is ‘B’ and Good Performance.")
    elif(grade==8):
        print("Your Grade is ‘B+’ and Very Good Performance.")
    elif(grade==9):
        print("Your Grade is ‘A’ and Excellent Performance.")
    elif(grade==10):
        print("Your Grade is ‘A+’ and Outstanding Performance.")
else:
    print("You have entered a value out of range")
#End of program 4
print("\n")

#Program for question 5
#Python program to print a particular pattern
print("Question 5")
n=6
for i in range(n):
    for j in range(i):
        print(' ', end='')
    for k in range(2*(n-i)-1):
        print(chr(65+k), end='')
    print()
#End of program 5
print("\n")

#Program for question 6
#Python script that repeatedly ask user to enter name and SID of students
print("Question 6")
sid = int(input("Enter SID: "))
name = input("Enter Name: ")
students = {sid:name}
while True:
    wish = input("Do you want to enter another student details(Y or N): ").upper()
    if wish == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif wish == 'N':
        break
    else:
     print('Invalid input!!!')

#parta
print("\nparta")
print(students)

#partb
print("\npartb")
print({k:v for k,v in sorted(students.items(), key= lambda x:x[1])})

#partc
print("\npartc")
print({k:v for k,v in sorted(students.items())})

#partd
print("\npartd")
search = int(input("Please Enter SID Of The Student You Want To Search: " ))
print("Student With The Given SID Is: ", students[search])
#End of program 6
print("\n")

#Program for question 7
#Python program to print Fibonacci sequence
print("Question 7")
def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))
terms=int(input("Enter The Number Of Terms In The Seires: "))
if (terms <= 0):
   print("Plese enter a positive integer!")
else:
   print("Resultant Fibonacci sequence: ")
   sum=0
   for i in range(terms):
       print(fibo(i))
       sum=sum+fibo(i)
avg=float(sum/terms)
print("Average Of The Resultant Fibonacci Series = ",avg)
#End of program 7
print("\n")

#Program for question 8
#Program to use set functions
print("Question 8")
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}
print("Set1=", Set1)
print("Set2=", Set2)
print("Set3=", Set3)

#parta
print("\nparta")
parta = (Set1|Set2)-(Set1&Set2)
print(parta)

#partb
print("\npartb")
partb = (Set1|Set2|Set3) - ((Set1&Set2)|(Set2&Set3)|(Set3&Set1))
print(partb)

#partc
print("\npartc")
partc= ((Set1&Set2)|(Set1&Set3)|(Set3&Set2))-(Set1&Set2&Set3)
print(partc)

#partd
print("\npartd")
partd = set()
for i in range(1, 11):
    if i not in Set1:
        partd.add(i)
print(partd)

#parte
print("\nparte")
parte = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        parte.add(i)
print(parte)
#End of program 8
