#********************************************************************************

#1) find if a number is positive or negative

number = int(input("Enter any number: "))

if number > 0:
    print("The number is positive")

elif number < 0:
    print("The number is negative")

else:
    print("The number is neither positive or negative, it is 0")

#*******************************************************************************

#2)Find if the number is even or odd

number = int(input("Enter any number: "))

if number % 2 == 0:
    print("The number is even")

else:
    print("The number is odd")

#********************************************************************************

#3)determine the maximum of 3 numbers.

print("Enter 3 numbers:")

a,b,c = int(input()), int(input()), int(input())

if a > b:
    if a > c:
        print("A is the maximum number")

    else:
        print("C is the maximum number")

else: 
    if b > c:
        print("B is the maximum number")

    else:
        print("C is the maximum number")
        
#***********************************************************************************

#4) determine the maximum of 4 numbers

print("Enter 4 numbers:")

a,b,c,d = int(input()), int(input()), int(input()), int(input())

if a > b and a > c:
    if a > d:
        print("A is the maximum number")

    else:
        print("d is the maximum number")

elif b > a and b > c: 
    if b > d:
        print("B is the maximum number")

    else:
        print("d is the maximum number")
        
else:
    if c > d:
             print("c is the maximum number")   

    else:
        print("d is the maximum number")

#*************************************************************************************

#5) determine the maximum of 3 numbers without using a third variable.

print("Enter 3 numbers:")

def maximum(a, b, c): 
  
    if (a >= b) and (a >= b): 
        largest = a 
  
    elif (b >= a) and (b >= a): 
        largest = b 
    else: 
        largest = c 
          
    return largest 

a,b,c = int(input()), int(input()), int(input())

print("The largest number is :", maximum(a,b,c))

#**********************************************************************************

#6)check the divisibility of a number by another number

a = int(input("Enter a number: "))
b = int(input("Enter a value to check the number is divisible by the value or not: "))

if a % b == 0:
    print("The number is divisible")

else:
    print("The number is not divisible")

#*********************************************************************************

#7) in which quadrant does the given point lie

x = int(input("Enter the 'x' co-ordinate: "))
y = int(input("Enter the 'y' co-ordinate: "))

if x == 0 and y == 0:
    print("The co-ordinates lie at the origin")

elif x >= 0 ^ y >= 0:
    print("The co-ordinates lie at the 1st quadrant")

elif x <= 0 ^ y >= 0:
    print("The co-ordinates lie at the 2nd quadrant")

elif x <= 0 ^ y<= 0:
    print("The co-ordinates lie at the 3rd quadrant")

else:
    print("The quadrant lie at the 4th quadrant")

#**********************************************************************************

#8)does the triangle exist with the given sides

print("Enter the sides of the triangle")

a = int(input("Enter the 1st side: "))
b = int(input("Enter the 2nd side: "))
c = int(input("Enter the 3rd side: "))

if a + b > c:
    print("The triangle exists")

else: 
    print("The trinagle does not exist")

#***************************************************************************************

#9)determine if the input year is a leap year or not.

year = int(input("Enter a year: "))

if (( year%400 == 0) or (( year%4 == 0 ) and ( year%100 != 0))):
    print(year , "is a Leap Year")
else:
    print(year , "is not a Leap Year")

#*************************************************************************************

#10) does the point belong to the circle with the centre at origin.




#*****************************************************************************************

#11) solve the quadratic equation

print("Enter the 3 coefficients for the quadratic equation: ")

a, b, c= eval(input()), eval(input()), eval(input())

d = (b**2) - (4 * a * c)
import math
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("The roots are real and unequal: ",x1, " and ",x2)


elif d == 0:
    x1 = x2 = (-b + math.sqrt(d)) / (2 * a)
    print("The roots are real and equal: ", x1," and ", x2)

else:
    real = -b/(2*a)
    imaginary = math.sqrt(-d)/(2*a)
    print("root1 = ",real,"+ i",imaginary,"and root2 = ",real,"+ i",imaginary)



#****************************************************************************************