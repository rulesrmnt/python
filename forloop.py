# print hello world 10 times
for i in range (10):
    print(f'hello world : {i}')

#print hello world in defined range
for i in range (1,6):
    print (f'hello world {i}')

# sum first 10 numbers
total = 0
for i in range (1,11):
    total += i
print (total)

# sum n numbers
num= int(input('enter number'))
total = 0
for i in range (1,num+1):
    total += i
print (total)

# sum each digits entered by the users
num=input('enter the number : ')
length=len(num)
total=0
for i in range(length):
    total +=int(num[i])
    print(total)

#count chracters present in input
name = input ('enter your full name : ')
lenght= len(name)
temp=""
for i in range(lenght):
    if name[i] not in temp:
        print(f'{name[i]} : {name.count(name[i])}')
        temp+=name[i]

num=int(input('enter number : '))
for i in range(1,num):
    if i==15:
        break  
    print(i)

num=int(input('enter number : '))
for i in range(1,num):
    if i==15:
        continue   
    print(i)


lucky_number=59
Enter_num=int(input('please enter ur lucky number : '))
times=1
game_over= False
while not game_over:
    if Enter_num==lucky_number:
        print(f"you won, you guessed this number in {times} times")
        game_over=True
    else:
        if Enter_num > lucky_number:
            print('too high')
        else:
            print('too low')
        times +=1
        Enter_num=int(input('Re-enter number : '))


num=input('enter the number : ')
length=len(num)
total=0
for i in num:
    total +=int(i)
    print(total)
