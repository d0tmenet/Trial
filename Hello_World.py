import calendar
from datetime import datetime

now = datetime.now()
mm = str(now.month)
dd = str(now.day)
yyyy = str(now.year)
hour = str(now.hour)
mi = str(now.minute)
ss = str(now.second)
print('Current course in the Universe: ' + mm + "/" + dd + "/" + yyyy + " " + hour + ":" + mi + ":" + ss)

print('Hello Boss')
print('What is your name')
yourName = input()
print('It is good to meet you, ' + yourName)
print('What is your Age, ' + yourName)
yourAge = input()

# yy = 2014
# mm = 11

# To ask month and year from the user
yy = now.year
mm = now.month
# yy = int(input("Enter year: "))
# mm = int(input("Enter month: "))

# display the calendar
print(calendar.month(yy, mm))

# Python program to convert decimal number into binary, octal and hexadecimal number system

# Change this line for a different result
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

dec = 34

def converttobinary(n):
    # Function to print binary number for the input decimal using recursion
    if n > 1:
        converttobinary(n//2)
        print(n % 2, end = '')

converttobinary(dec)

