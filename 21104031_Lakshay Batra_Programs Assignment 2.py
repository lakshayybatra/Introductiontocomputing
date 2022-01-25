#Program for Question 1
#Program to input given string “Python is a case sensitive language” and use string related functions.
print("Question 1")
input_string="Python is a case sensitive language"
print(input_string)
#1a)
print("\nPart a")
print("Length of the string is", len(input_string))
#1b)
print("\nPart b")
print("The string in reverse order is:", input_string[::-1])
#1c)
print("\nPart c")
new_string=input_string[10:27]
print(new_string)
#1d)
print("\nPart d")
part_d1=input_string.replace("a case sensitive", "object oriented")
print("After replacing in input string:", part_d1)
#or was confused that in which one string we have to replace so replacing in both
part_d2=new_string.replace("a case sensitive", "object oriented")
print("After replacing in new string created in part c:", part_d2)
#1e)
print("\nPart e")
print(input_string.index("a"))
#1f)
print("\nPart f")
print(input_string.replace(" ",""))
#End of program 1
print("\n")

#Program for Question 2
#Program to use String formatting
print("Question 2")
Name="Hey, {name} here!".format(name="Lakshay")
SID="My SID is {sid}".format(sid=21104031)
intro="I am from {dept} department and my CGPA is {cgpa}".format(dept="Electrical", cgpa=float(10))
print(Name)
print(SID)
print(intro)
#End of program 2
print("\n")

#Program for Question 3
#Program about using bitwise operators
print("Question 3")
a=56
b=10
print("a=", a)
print("b=", b)
print("\nPart a")
print("a&b:", a&b)
print("\nPart b")
print("a|b:", a|b)
print("\nPart c")
print("a^b:", a^b)
print("\nPart d")
print("Left shifting both a and b with 2 bits:", a<<2, b<<2)
print("\nPart e")
print("Right shifting a with 2 bits and b with 4 bits:", a>>2, b>>4)
#End of program 3
print("\n")

#Program for Question 4
#Program to find the greatest of three numbers entered by the user.
print("Question 4")
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if(num1>num2 and num1>num3):
    print("Number one is greatest", num1)
else:
    if (num2 > num1 and num2>num3):
        print("Number two is greatest", num2)
    else:
        print("Number three is greatest", num3)
# End of program 4
print("\n")

#Program for Question 5
#Program to check if the word “name” is present in the string entered by the user
print("Question 5")
enter_string=str(input("Enter a string:"))
if("name" in enter_string):
    print("Yes")
else:
    print("No")
#End of program 5
print("\n")

#Program for Question 6
#Program to find whether the sides will form a triangle or not
print("Question 6")
side1=input("Enter first side length:")
side2=input("Enter second side length:")
side3=input("Enter third side length:")
side1=int(side1)
side2=int(side2)
side3=int(side3)
if(side1==0 or side2==0 or side3==0):
#As none of the side of a triangle can be zero so, it will not form a trianlge
    print("No")
elif(side1+side2>side3 and side2+side3>side1 and side3+side1>side2):
#As the sum of any two sides is greater than the third side, it will form a triangle
    print("Yes")
else:
#As the sum of any two sides is not greater than the third side, it will not form a triangle
    print("No")
#End of program 6
