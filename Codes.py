#Program for Question 1
#Program for average of 3 numbers entered by user 
print("enter first number")
num1=input()
print("enter second number")
num2=input()
print("enter third number")
num3=input()
print("the average of three nummbers is", (float(num1)+float(num2)+float(num3))/3)
#End of program 1
#Program for Question 2
#Program to compute a person's income tax.
print("Enter your Gross Income to the nearest penny")
gi=input()
print("Enter the number of dependents")
dep=input()
ti=int(gi)-10000-int(dep)*3000
#ti is taxable income
print("Your income tax is", int(ti)*20/100)
#End of program 2
#Program for Question 3
#Program to store different datatypes values in a list
print("enter your sid")
sid=int(input())
print("enter your name")
name=input()
print("enter your gender (Use M for Male, F for Female, U for unknown)")
gender=input()
print("enter your course name")
cn=input()
print("enter your CGPA")
cgpa=float(input())
l=[sid,name,gender,cn,cgpa]
print("student", l)
#End of program 3
#Program for Question 4
#Program to enter marks of 5 students
print("enter marks of 1st student")
inp1=input()
print("enter marks of 2nd student")
inp2=input()
print("enter marks of 3rd student")
inp3=input()
print("enter marks of 4th student")
inp4=input()
print("enter marks of 5th student")
inp5=input()
marks=[inp1,inp2,inp3,inp4,inp5]
print("Marks of respective students", marks)
marks.sort()
print("Marks in sorted manner", marks)
#End of program 4
#Program for Question 5
#Program to print a specified list
colours=['Red','Green','White','Black','Pink','Yellow']
print("The list of colors is", colours)
colours.remove('Black')
print("Q5a) color", colours)
colours=colours[:colours.remove('Pink')]+['Purple']
print("Q5b) The final list is", colours)
#End of program 5