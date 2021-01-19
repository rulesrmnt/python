# for i in range (10):
#     print(f'hello world : {i}')

# for i in range (1,6):
#     print (f'hello world {i}')

# total = 0
# for i in range (1,11):
#     total += i
# print (total)

# num= int(input('enter number'))
# total = 0
# for i in range (1,num+1):
#     total += i
# print (total)

num=input('enter the number : ')
length=len(num)
total=0
for i in range(length):
    total +=int(num[i])
    print(total)

# name = input ('enter your full name : ')
# lenght= len(name)
# temp=""
# for i in range(lenght):
#     if name[i] not in temp:
#         print(f'{name[i]} : {name.count(name[i])}')
#         temp+=name[i]