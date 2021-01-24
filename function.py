def add_two(a,b):
    return a+b
a, b =input("enter number : ").split()
total= add_two(int(a),int(b))
print(total)

def even_odd(num):
    if num % 2 == 0:
        return('even')
    return('odd')
while True:
    num=int(input('Enter the number : '))
    print(even_odd(num))


while True:
    num = int(input('enter the number : '))
    total = 0
    for i in range (1,11):
        total=num*i
        print(f'{num} * {i} = {total}')

def is_even(num):
    if num % 2 == 0:
        return True
    return False
num=int(input('Enter the number : '))
print(is_even(num))

def is_even(num):
    return num % 2 == 0
while True :
    num=int(input('enter the number : '))
    print(is_even(num))

def greater (a,b):
    return a > b
while True:
    a, b=input('enter number : ').split()
    print(greater(int(a),int(b)))

def greater (a,b):
    if a > b:
        return "first number is greater than second number"
    return "first number is smaller than second number"
while True:
    a, b=input('enter two numbers : ').split(",")
    print(greater(int(a),int(b)))

def three_greater (a,b,c):
    if a>b and a>c:
        return 'first number is greater'
    elif b>a and b>c:
        return "second number is greater"
    return "third number is greater"
while True:
    a, b, c=input('enter three numbers : ').split(',')
   print(three_greater(int(a),int(b),int(c)))

def is_palindrome(name):
    reverse=name[::-1]
    if name==reverse:
        return("the entred word is palindrome")
    return('the enetred word is not palindrome')
while True:
    name = input('enter palindrome : ')
    print(is_palindrome(name))

def febonacci_series(num):
    a = 0
    b = 1
    if num==1:
        print(a)
    elif num==2:
        print(a,b)
    else:
        print(a,b, end=" ")
        for i in range (num-2):
            c=a+b
            a=b
            b=c
            print(b, end=" ")
while True:

    num=int(input('enter number : '))
    febonacci_series(num)

