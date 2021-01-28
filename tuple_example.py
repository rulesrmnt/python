num = (1,2,3,4)
print (num)
print (type(num))
print (num[0:2]) #slicing in tuple
print (num[1:4:2])
#  looping in tuple
for i in num:
    print(i)
# tuple with one element
num1 = (0,)
print(type(num1))
# tuple without paranthesis
num2 = 1,2,3,5,'rahul'
print (num2)
print(type(num2))
# tuple unpacking
n1,n2,n3,n4,n5=num2
print(n5)
print(n3)
# list inside tuple 
fruits = ('mango',['orange','kiwi'])
print(fruits[1])
fruits[1].append('banana')
print(fruits)
fruits[1].pop(0)
print(fruits)
fruits[1].insert(0,'grapes')
print(fruits)
# function used in tuple min max sum
print(min(num))
print(max(num))
print(sum(num))
#range in tuple
num_range = list(range(1,11))
print(num_range)
print(type(num_range))
num_range1 = tuple(range(1,11))
print(num_range1)
print(type(num_range1))
#tuple can be converted to list and string
# num3 = list((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
# print(num3)
num3 = str(((1, 2, 3, 4, 5, 6, 7, 8, 9, 10)))
print(type(num3))
