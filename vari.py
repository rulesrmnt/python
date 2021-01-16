number1=23
print (number1)
first_name = "Rahul"
second_name ="ranjan"
ag= 24
full_name = first_name+" "+second_name
print("My full name is \n"+ full_name+ " \nand age is \n" + str(ag))
print("My full name is "+ full_name+ " and age is " + str(ag))
print(f"my full name is {second_name} and age is {ag}")

# user input function
name =input("enter ur name : ")
print ("ur name is " + name)
number_one=int(input ("enter first number : "))
number_two=int(input ("enter second number : "))
sum=number_one + number_two
print ("Sum of two numbers is " + str(sum))

num1=int(input('enter 1 no : '))
num2=int(input('enter 2 no : '))
num3=int(input('enter 3 no : '))
Average=(num1 + num2 +num3)//3
print("Average of three numbers is " + str(Average))

num1, num2, num3=input('enter 3 no : ').split(",")
Average=(int(num1) + int(num2) +int(num3))//3
print("Average of three numbers is " + str(Average))

name,roll_no, clas, school=input("Enter student details : ").split(",")
print (name,roll_no,clas,school)
print(f"Student name is {name} whos roll number is {roll_no} studies in class {clas} of {school} school") 
print(f'{name}\n{roll_no}\n{clas}\n{school}')