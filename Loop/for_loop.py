# For loop

# for a in range(stop)
'''
for a in range(9):
    print(a)
'''

#for b in range(start,stop):

'''
for b in range(6,12):
    print(b)
'''

#for b in range(start,stop,increment):
'''
for b in range(5,25,5):
    print(b)
'''

'''
number1 = int(input("Enter a number:"))
number2 = int(input('enter a number:'))

sum = number1 + number2
print("sum of two numbers is:", sum)
'''

# for loop excercise
a = int(input('enter start number:'))
b = int(input('enter stop number:'))
c = int(input('enter incr. number:'))

for j in range(a,b,c):
    print(j)
    if j % 2 == 0:
        print(j,"is a even number")
    else:
        print(j, "is a odd number")
