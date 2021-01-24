num=[2,3,8,9]
print(num)

num1=[7,8,6,2]
print(num1[0])

num2=[5,6,2,9]
for i in num2:
    print(i)

fruits=['apple','orange','kiwi','banana','pear','grape']
length=len(fruits)
print(f'length of given list is : {length}')
fruits.append('apple')
fruits.insert(1,'aloo')
print(fruits.pop(5))
print(fruits.index('kiwi'))
length=len(fruits)
print(f'length of given list is : {length}')
print(fruits)
print(fruits[1])
for i in fruits:
    print(i)

fruits=['apple','orange','kiwi','banana','pear','grape']
print(fruits.count('orange'))
fruits.sort()
print(fruits)


def sqaure_num(l):
    square=[]
    for i in l:
        square.append(i**2)
    return square
num=[2,5,6,9,8]
print(sqaure_num(num))


        
fruits=['apple','orange','kiwi','banana','pear','grape']
num=[1,2,3,5]
def rev_num2(l):
    l.reverse()
    return l
def rev_num(l):
    rev=[]
    for i in l:
        rev.append(i[::-1])
    return rev 

print(rev_num(fruits))
print(rev_num2(num))
print(rev_num2(fruits))
   