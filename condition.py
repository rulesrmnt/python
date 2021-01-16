age=input("enter your age : ")
if int(age)>=14:
    print("you are eligible")
else:
    print("better luck next time")

lucky_no = 7
enter_no=input("Enter your number betwwen 0-14 : ")
if int(enter_no)>=14:
    print("out of range")
elif int(enter_no)<14:
    print ('entered number is btween 0 to 14')
if int(enter_no)==int(lucky_no):
    print("u have got the lucky number")
else:
    print ('u lost')
