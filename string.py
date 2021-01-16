#to print defined location character
name='rahul'
print (name[2])

#character slicing
name2="raHul is gOOd boT"
print (name2[0:10])
print (name2[1:-5])
print (name2[1:9:2]) #print alternate characters
print (name2[::-1])
print (name2[::-1])
#user input and print in reverse order
name3=input("enter usename : ")
print(name3[::-1])

print (len(name2))
print (name2.upper()) #upper case 
print (name2.lower()) # lower case
print (name2.title()) #title case
print (name2.count('O'))
print (name2.count('o'))

#strip method
name4="   abhishek raj    "
dot="@@@@@"
print(name4)
print(name4.lstrip()+dot)
print(name4.rstrip()+dot)
print(name4.strip()+dot)
print(name4.replace(" ","_"))
asd=(name4.replace(" ",""))
print(asd.center(25,'*'))