age = int(input("please enetr your age for ticket charge : "))
if age>=0 and age<=3:
    print("ticket is free")
elif 4<=age<=10:
    print('price of ticket is : 150')
elif age>=11 and age<=60:
    print('price of ticket is : 250')
else:
    print('price of ticket is : 200')

num=input('enter any number : ')
length= len(num)
# num1=int(num)
i=0
total=0
while i<length:
    total=total + int(num[i])
    i +=1
    print(total)

name= input(' Enter your name : ')
length = len(name)
i=0
while i<length:
    print(f"{name[i]} : {name.count(name[i])}")
    i = i+1