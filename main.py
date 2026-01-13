'''# Task:1
# Make a calculator with python code
from itertools import count
from math import factorial
from random import choice

from numpy.ma.extras import average


def add(x,y):
    return  x+y
def sub(x,y):
    return  x-y
def multiple(x,y):
    return x*y
def divide(x,y):
    if y==0 :
        return "Cannot divide by zero!"
    return x/y

print("Select Operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiple")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number"))
num2 = float(input("Enter second number"))

if choice == "1":
    print("Result; " , add(num1,num2))
elif choice == '2':
    print("Result: ", sub(num1,num2))
elif choice == "3":
    print("Result: " , multiple(num1,num2))
elif choice == '4':
    print("Result :" , divide(num1,num2))
else:
    print("Invalid Input")

########################################################################

# Task 2:
# Make a program to calculate total marks, average and grade

#input marks for 5 subjects
print("Enter marks of 5 subjects (out of 100)")
marks = []
for i in range(1, 6):
    m = float(input(f"Subject {i} :"))
    marks.append(m)

# Calculate total and average
total = sum(marks)
average =  total / 5

# Determine grade
if average >= 90:
    grade = "A+"
elif average  >= 80:
    grade = "A"
elif average >= 70 :
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >=  50:
    grade= "D"
else:
    grade = "F"

#Display results
print("\nTotal marks : ", total)
print("Average marks : ", average)
print("Grade : ", grade)

##############################################################

# Task:3
# Make a program in multiplication table is generate

#get input from user
num = int(input("Enter a number to print its table: "))
#print table from 1 TO 10
print(f"\nMultiplication table of {num}:")
for i in range(1,11):
    print(f"{num} * {i} = {num * i}")

##############################################################

# Task:4
#Mae a program and print Fibonacci series up to n terms

#Get numbr of terms from user
n = int(input("Enter the number of terms;"))

# first two terms
a, b =0 ,1
count = 0

print("\nFibonacci Series:")
while count < n:
    print(a, end=" ")
    a, b = b , a+b
    count += 1
print("\n")

##############################################################

# Task:5
# Make a program and print a prime number

#Get input from user
num = int(input("Enter a number: "))

#Prime number check
if num <= 1:
    print(num,"is not a prime number")
else:
    for i in range(2, int(num ** 0.5) + 1 ):
        if num % i == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num , "is a prime number")


##############################################################

# Task:6
# make a program and print a factorial Calculator

#Get input from user
num = int(input("Enter a number:"))

#Check for valid input
if num < 0:
    print("Factorial does not exist for negative number")
elif num == 0:
    print("The factorial of 0 is 1.")
else:
    factorial = 1
    for i in range(1, num+1):
        factorial *= i
        print(f"The factorial of {num} is {factorial}.")


##############################################################

# Task:7
# Make a program on Check if number is positive, negative or zero

num = float(input("Enter any number"))
if num > 0:
    print("Positive")
elif num< 0 :
    print("Negative")
else:
    print('Zero')

##############################################################

# Task:8
# Make a program on to check if a year is leap year:

#Check leap year

year = int(input("Enter any number:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")

##############################################################

# Task:9
# Make a program on a temperature converter (Celsius to Fahrenheit)

celsius = float(input("Enter temperature in celsius;"))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in Fahrenheit", fahrenheit)

##############################################################

# Task:10
# Make a program on  a check if a number is even or odd
num = int(input("Enter any number"))

if num % 2 == 0:
    print("Even number")
else:
    print("odd number")


##############################################################

# Task:11
# Make a program on calculate a Simple Interest

p =  float(input("Enter principal amount"))
r = float(input("Enter rate of interest"))
t = float(input("Enter time (in years):"))

si = (p*r*t)/100
print("Simple Interest", si)

###############################################################

# Task:12
# Make a program on calculate the area of circle

radius = float(input("Enter the radius:"))
area = 3.1416 * radius * radius
print("Area of the circle", area)


################################################################

# Task:13
# Make a program on to find the square of a number
num = float(input("Enter a number"))
square =  num ** 2
print("Square is", square)

from itertools import count

################################################################

# Task:14
# Make a program on to reverse a number
num =  int(input("Enter a number"))
rev =0
while num != 0 :
    digit = num % 10
    rev = rev * 10 + digit
    num //= 10
print("Reversed  number: " , rev)

################################################################

# Task:15
# Make a program on to find the sum of digits of a number

num = int(input("Enter any number"))
sum_digits = 0

while num !=0:
    sum_digits += num % 10
    num //= 10
print("Sum of digits: ", sum_digits)

################################################################

# Task:16
# Make a program on to swap two number

a = int(input("Enter first number"))
b = int(input("Enter second number"))

#swapping
a,b = b,a
print("After swapping: a= ",a,"b= ",b)

################################################################

# Task:17
# Make a program on to count the number of digits in a number
num = int(input("Enter a number"))
count = 0
while num != 0:
    num//= 10
    count +=1
print("Total digit", count)

################################################################

# Task:18
# Make a program on find the largest of 3 number

a = int(input("Enter first number"))
b = int(input("Enter second number"))
c = int(input("Enter third number"))

if a>=b and a>=c:
    print("largest number is:",a)
elif b> a and b>=c:
    print("largest number is",b)
else:
    print("Largest number is:",c)

from unicodedata import digit

################################################################

# Task:19
# Make a program on check vowel or constant

ch = input("Enter a single alphabet: ") .lower()
if ch in ("a","e","i","o","u"):
    print(ch,"is a vowel.")
elif ch.isalpha():
    print(ch, "is a consonant.")
else:
    print("Not a valid alphabet.")

################################################################

# Task:20
# Make a program on  to check if a number is Armstrong or not
num = int(input("Enter a number: "))
sum =  0
temp = num
n = len(str(num))

while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num,"is not an Armstrong number.")

################################################################

# Task:21
# Make a program on to check if a number is palindrome(same forward and backward)

num = int(input("Enter a number:"))
original = num
rev = 0

while num>0:
    digit = num % 10
    rev = rev * 10+digit
    num//= 10

if original == rev:
    print(original,"is a palindrome.")
else:
    print(original,"is not a palindrome")


##########################################################

# Task: 22
# Create a program on to print all even number from 1 to N:

n = int(input("Enter the value of N: "))
print("Even numbers from 1 to",n, "are:")
for i in range(1,n+1):
    if i % 2 == 0:
        print(i,end=' ')

##########################################################

# Task: 23
# Create a program on to print the factorial of all numbers from 1 TO N:

n = int(input("Enter a number"))
for i in range(1, n+1):
    fact = 1
    for j in range(1,i + 1):
        fact *= j
    print(f"Factorial of {i} is {fact} :")

###########################################################

# Task: 24
# Create a program on to print a star triangle pattern:

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    print("*" * i)


###########################################################

# Task: 25
# Create a program on to print a reverse star triangle pattern:

rows = int(input("Enter number of rows: "))
for i in range(rows, 0 , -1):
    print("*" * i)

###########################################################

# Task: 25
# Create a program on to print a pyramid pattern

rows = int(input("Enter number of rows: "))
for i in range(1, rows+1):
    print(" "* (rows - i)+ "*" * (2*i-1))

############################################################

# Task:26
# Create a program on to check whether a number is prime or not:

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num ** 0.5)-1):
        if num % i == 0:
            print(num, "is a not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print("is not a prime number")

#############################################################

# Task: 27
# Create a program to find the GCD(Greatest Common Divisor) of two numbers:

# Find GCD of two numbers

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
while b != 0:
    a,b = b,a % b
    print("GCD is:", a)

#############################################################

# Task: 27
# Create a program to calculate the LCM (Lest Common Multiple) of two numbers:

a = int(input("Enter first number"))
b = int(input("Enter Second number"))
def gcd(x,y):
    while y!=0:
        x,y = y, x%y
    return x
lcm = (a*b)  // gcd(a,b)
print("Lcm is ",lcm)

###############################################################

# Task: 28
# Create a program to check whether character is uppercase, lowercase, digit , or special character

ch = input("Enter a single character:")

if ch.isupper():
    print("Uppercase letter")
elif ch.islower():
    print("Lowercase letter")
elif ch.isdigit():
    print("Digit")
else:
    print("Special character")

#####################################################################

# Task: 29
# Create a program to count words in a sentence
sentence = input("Enter a sentence")
words = sentence.split()
print("Totals words:",len(words))

from numpy.ma.extras import average

########################################################################

# Task: 30
# Create a program to find  the sum of natural number up to N

n = int(input("Enter a number; "))
sum = 0
for i in range(1, n + 1):
    sum += i
print("Sum is:",sum)

#######################################################################

# Task: 31
# Create a program to calculate the power of a number(x^y)

base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

result = base ** exponent
print(f"{base}^{exponent} = {result}")

############################################################

# Task: 32
# Create a program to find the average of N numbers:

n = int(input("How many numbers? "))
total = 0

for i in range(n):
    num = float(input(f"Enter number {i+1}: "))
    total += num

average = total/n
print("Average is:",average)

##############################################################

# Task:33
# Create a program to reverse a string

text = input("Enter a string: ")
reversed_text = text[::-1]
print("Reversed string:",reversed_text)

from numpy.ma.extras import unique

################################################################

# Task:34
# Create a program to find the smallest number in a list:

numbers = list(map(int, input("Enter number to find the smallest number in list ").split()))
smallest = min(numbers)

print("Smallest number is: ", smallest)

#########################################################################

# Task: 35
# Create a program to sort a list in ascending order

numbers = list(map(int, input("Enter numbers to sort a list in ascending order ").split()))
numbers.sort()

print("Sorted list:", numbers)

##################################################################

# Task: 36
# Create a program to find the Second largest number in a list:
numbers = list(map(int, input("Enter numbers to find the second largest number in a list. ").split()))
unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers)<2:
    print("second largest does not exist")
else:
    print("Second largest number is: ",unique_numbers[-2])

################################################################

#Task: 37
# Create a program to remove duplicates from list
numbers = list(map(int, input("Enter numbers to remove duplicate from list ").split()))
unique_numbers = list(set(numbers))

print("list after removing duplicates:", unique_numbers)

##################################################################

# Task: 38
# Create a program to count the frequency of each element in a list:
numbers = list(map(int, input("Enter numbers to count the frequency of each element in a list ").split()))

frequency = {}
for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Frequencies: ")
for key, value in frequency.items():
    print(key,":",value)

######################################################################

# Task: 39
# Create a program to check if an element exists in a list:

numbers = list(map(int, input("Enter numbers to check if an element exists in a list ").split()))
key = int(input("Enter number to search: "))
if key in numbers:
    print(key,"is present in the list.")
else:
    print(key,"is not present in the list.")

#######################################################################

# Task: 40
# Create a program to merge two lists:
list1 = list(map(int, input("Enter numbers to merge two lists ").split()))
list2 = list(map(int, input("Enter numbers to merge two lists ").split()))
merged_list = list1 + list2
print("Merged list:",merged_list)

#########################################################################

# Task: 41
# Create a program to find the sum of the element in a list:

numbers = list(map(int, input("Enter numbers to find the sum of the element in a list ").split()))
total = sum(numbers)

print("Sum of elements", total)

#########################################################################

# Task: 42
# Create a program to count even and odd number in list:

numbers = list(map(int, input("Enter numbers to count even and odd number in list").split()))
even =0
odd = 0

for num in numbers:
    if num % 2 ==0:
        even += 1
    else:
        odd += 1
print("Even numbers:", even)
print("Odd numbers:", odd)

##########################################################

# Task: 43
# Create a program to separate even and odd numbers from a list
numbers = list(map(int, input("Enter a number separated by space ").split()))
even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)
print("Even number: ",even)
print("Odd number: ", odd)

############################################################################

# Task: 44
# Create a program to print numbers divisible by a given number in a list
numbers = list(map(int, input("Enter a number to print a divisible by a given number in a list ").split()))
divisor  =  int(input("Enter the divisor: "))
print(f"Numbers divisible by {divisor} are: ")
for num in numbers:
    if num % divisor == 0:
        print(num,end=' ')

###########################################################################

# Task: 45
# Create a program to print all prime number in list;

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
        return True

numbers = list(map(int, input("Enter a number to print all prime number list ").split()))
print("Print prime numbers are:")

for num in numbers:
    if is_prime(num):
        print(num,end=' ')

#################################################################3

# Task: 46
# Create a program to find a HCF of two numbers.

a = int(input("Enter first number:"))
b = int(input("Enter second number"))

while b:
    a, b = b, a % b
    print("Sum is: ", a)


#################################################################3

# Task: 47
# Create a program to find a LCM of two numbers.

a = int(input("Enter first number:"))
b = int(input("Enter second number"))

def gcd(x,y):
    while y:
        x, y = y, x % y
    return  x

lcm = (a * b)
print("lcm is: ",lcm)


#################################################################3

# Task: 48
# Create a program (with function) check prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n** 0.5)+1):
        if n % i == 0:
            return False
    return True
num = int(input("Enter a number: "))
print("Prime " if is_prime(num) else "not Prime")

#################################################################3

# Task: 49
# Create a program (with function) find factorial
def factorial(n):
    result  = 1
    for i in range(1, n+1):
        result *= i
    return  result
num = int(input("Enter a number: "))
print("Factorial is:",factorial(num))

####################################################################

# Task: 50
# Create a program (with function) find maximum of two  numbers
def maximum(a, b):
    return a if a > b else b

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
print("Maximum is:", maximum(x , y))

#####################################################################

# Task: 51
# Create a program (with function) check palindrome
def is_palindrome(s):
    return s == s[::-1]

text = input("Enter text or number: ")
print("Palindrome" if is_palindrome(text) else "not Palindrome")

#####################################################################

# Task: 52
# Create a program (with function) fibonacci series
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end="")
        a,b = b, a+ b
terms = int(input("Enter numer of terms:"))
fibonacci(terms)

######################################################################

# Task: 53
# Create a program (with function) simple program for myself
def myself():
    a = 2
    b = 3
    if a>b:
        print("hello 'a' ")
    else:
        print("hello 'b' ")
myself()

#######################################################################

# Task: 54
# Create a program with function and with class
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

l = float(input("Enter length: "))
w = float(input("Enter width: "))
rect = Rectangle(l,w)
print("Area of rectangle is:",rect.area())

######################################################################

# Task: 55
# Create a program with function and class
class Number:
    def __init__(self , num):
        self.num  =  num
    def is_even(self):
        return self.num % 2 == 0
n = int(input("Enter a number"))
obj = Number(n)
print("Even" if obj.is_even() else "odd")

##############################################################

# Task: 56
# Next class program
class Calculator:
    def add(self,a ,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def multiple(self, a, b):
        return a*b
    def divide(self,a,b):
        return a/b if b != 0 else "Cannot divide by 0"

c = Calculator()
x = int(input("Enter first number"))
y = int(input("Enter second number"))

print("Add", c.add(x,y))
print("Subtraction", c.sub(x,y))
print("Multiplication",c.multiple(x,y))
print("Division",c.divide(x,y))

from symtable import Class

from PIL.SpiderImagePlugin import iforms
from matplotlib.pyplot import title


############################################################

# Task: 57
# LIBRARY BOOK MANAGEMENT
class Book:
    def __init__(self ,title , author):
        self.title = title
        self.author = author

    def display(self):
        print(f"Title: {self.title}, Author: {self.author}")

book1 = Book("Harry Potter","J.K. Rowling")
book2 = Book("Wings of fire","A.P.J. Abdul Kalam")

book1.display()
book2.display()

##############################################################
# Task: 58
# BANK ACCOUNT(DEPOSIT/WITHDRAW)
class BankAccount:
    def __init__(self,myname,balance=0):
        self.myname = myname
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited:",amount)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Withdraw:",amount)
    def display_balance(self):
        print(f"{self.myname}'s Balance:{self.balance}")

acc = BankAccount("Kanika")
acc.deposit(1000)
acc.withdraw(600)
acc.display_balance()

#############################################################

# Task:58
# SIMPLE CONTACT BOOK

class Contact:
    def __init__(self, myname , phone):
        self.myname = myname
        self.phone = phone
    def display(self):
        print(f"Name: {self.myname} , Phone: {self.phone}")

c1 = Contact("Mine","12345789")
c2 = Contact("Your","987654321")

c1.display()
c2.display()

##############################################################
# Task:59
# ATM Machine Simulator (Basic)
class ATM:
    def __init__(self,balance=1000):
        self.balance = balance
    def check_balance(self):
        print("Balance:",self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount
            print("Withdraw:",amount)

atm = ATM()
atm.check_balance()
atm.withdraw(500)
atm.check_balance()

##################################################################
# Task: 60
# SHOPPING CART(ADD AND VIEW ITEMS)
class Cart:
    def __init__(self):
        self.items = []
    def add_items(self,product):
        self.items.append(product)
        print(f"Added: {product}")
    def show_cart(self):
        print("Your Cart:")
        for item in self.items:
            print("-",item)

cart = Cart()
cart.add_items("Milk")
cart.add_items("Bread")
cart.show_cart()

###################################################################
# Task: 61
# MOVIE TICKET BOOKING (Basic)
class Movie:
    def __init__(self,title ,seats):
        self.title = title
        self.seats = seats

    def book_ticket(self,n):
        if n <= self.seats:
            self.seats -= n
            print(f"{n} ticket(s) booked for '{self.title}'")
        else:
            print("Not enough seats available")

m = Movie("Avengers",5)
m.book_ticket(2)
m.book_ticket(4)

###################################################################
# Task: 62
# TO DO TASK MANAGER

class Todo:
    def __init__(self):
        self.tasks = []
    def add_tasks(self,task):
        self.tasks.append(task)
    def view_taskes(self):
        print("Tasks:")
        for task in self.tasks:
            print("-",task)

t = Todo()
t.add_tasks("Complete Homework")
t.add_tasks("Go for a walk")
t.view_taskes()

###################################################################
# Task: 63
# SIMPLE VOTING SYSTEM
class Voter:
    def __init__(self,myname,age):
        self.myname = myname
        self.age = age
    def can_vote(self):
        return self.age >= 18

v = Voter("Riya",20)
print("Eligible to vote" if v.can_vote()
else "Not eligible to vote")

###################################################################
# Task: 64
# EMAIL VALIDATOR (BASIC CHECK)
class Email:
    def __init__(self, email):
        self.email = email
    def is_valid(self):
        return "@" in self.email and "." in self.email
e = Email("kanika20056@gmail.com")
print("Valid email" if e.is_valid() else "Invalid Email")

###################################################################
# Task: 65
# BILL GENERATOR FOR GROCERY SHOP

class Bill:
    def __init__(self):
        self.total = 0
    def add_items(self,price):
        self.total += price
    def show_total(self):
        print("Total Bill : $ ",self.total)
b = Bill()
b.add_items(40)
b.add_items(25)
b.show_total()

###################################################################
# Task: 65
# SIMPLE GRADE CHECKER WITH CLASS

class Result:
    def __init__(self,percent):
        self.percent = percent
    def get_grade(self):
        if self.percent >= 90:
            return "A"
        elif self.percent >= 70:
            return "B"
        elif self.percent >= 50:
            return "c"
        else:
            return "F"

r = Result(83)
print("Grade:",r.get_grade())

####################################################################
# Task: 66
# ELECTRIC BILL CALCULATOR
class ElectricBill:
    def __init__(self, units):
        self.units = units
    def calculate_bill(self):
        if self.units <=100:
            return self.units *5
        else:
            return (100 * 5) + (self.units-100)*10
e  = ElectricBill(150)
print("Bill Amount: $",e.calculate_bill())

###############################################################
# Task: 67
# ATM PIN VALIDATION
class ATM:
    def __init__(self , correct_pin):
        self.correct_pin = correct_pin
    def validate(self , pin_entered):
        return  pin_entered == self.correct_pin
atm =  ATM("1234")
entered = input("Enter PIN: ")
print("Access Granted:" if
atm.validate(entered) else "Wrong PIN")

##############################################################
# Task: 68
# BANK MANAGEMENT SYSTEM (MENU-BASED)
class BankAccount:
    def __init__(self, myname, balance=0):
        self.myname = myname
        self.balance = balance
    def deposit(self,amount):
        self.balance += amount
        print("Deposited:", amount)
    def withdraw(self,amount):
        if amount >= self.balance:
            self.balance -= amount
            print("Withdraw", amount)
        else:
            print("Insufficient Balance")
    def check_balance(self):
        print(f"Balance: ${self.balance}")

account = BankAccount("Kanika")

while True:
    print("\n1.Deposit\n2.Withdraw\n3.Check Balance\n4.Exit")
    ch = int(input("Choose option: "))

    if ch == 1:
        amt = float(input("Enter amount to deposit:"))
        account.deposit(amt)
    elif ch == 2:
        amt = float(input("Enter amount to Withdraw:"))
        account.withdraw(amt)
    elif ch == 3:
        account.check_balance()
    elif ch == 4:
        print("Thank you !")
        break
    else:
        print("Invalid choice.")

######################################################################
# Task: 69
# STUDENT MANAGEMENT SYSTEM
class Student:
    def __init__(self,roll,myname,marks):
        self.roll = roll
        self.myname = myname
        self.marks = marks

    def display(self):
        print(f"Roll: {self.roll}, Name: {self.myname}, Marks: {self.marks}")

students = []
while True:
    print("\n1.Add Student\n2.View All\n3.Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        r = int(input("Roll no."))
        n = input("Name")
        m = int(input("Marks:"))
        s = Student(r,n,m)
        students.append(s)
    elif ch == 2:
        for s in students:
            s.display()
    elif ch == 3:
        break
    else:
        print("Invalid option.")

#######################################################################################
# Task: 70
# QUIZ GAME WITH CLASSES
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer
question = [
    Question ("Capital of India?\n{A}Delhi\n{B}Mumbai\n","A"),
    Question ("Python is?\n{A}Snack\n{B}Language\n","B"),
    Question ("2+2=?\n{A}3\n{B}4\n","B")
]
score = 0
for q in question:
    ans = input(q.prompt)
    if ans == q.answer:
        score += 1
print(f"You got {score}/ {len(question)} correct.")

########################################################################################
# Task: 71                                # Is Project ke Command Run Nhi Ho Re Hai #
# ONLINE FOOD ORDERING (CLASS WITH LIST)
class FoodItem:
    def __init__(self , myname , price):
        self.myname = myname
        self.price = price
class Order:
    def __init__(self):
        self.items = []
    def add_item(self,item):
        self.items.append(item)
        print(f"{item.myname} added.")
    def show_bill(self):
        total = sum(item.price for item in self.items)
        print("Total bill: $",total)
menu= [
    FoodItem("Pizza",120),
    FoodItem("Burger",80),
    FoodItem("Price",50)
]
order = Order()

while True:
    print("\nMenu:")
    for i , item in enumerate(menu):
        print(f"{i+1}. {item.myname} - $ {item.price}")
        print("4.Show bill\n5.Exit")

        ch = int(input("Choose item number: "))
        if 1 <= ch <= 3:
            order.add_item(menu[ch-1])
        elif ch == 4:
            order.show_bill()
        elif ch == 5:
            break
        else:
            print("Invalid option.")

####################################################################################
# Task: 72
# LIBRARY MANAGEMENT SYSTEM (BASIC)
class Book:
    def __init__(self , title , author):
        self.title = title
        self.author = author
        self.available = True
    def display(self):
        status = "Available" if self.available else "Issued"
        print(f"{self.title} by {self.author} = {status}")
class Library:
    def __init__(self):
        self.books = []
    def add_book(self,book):
        self.books.append(book)
    def issue_book(self , title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book issued!")
                return
            print("Book not available")
    def show_books(self):
        for book in self.books:
            book.display()

lib =Library()
lib.add_book("Python Basics", "A.Sharma")
lib.add_book("Data Structure","M.Rao")
while True:
    print("\n1.Show Books\n2.Issue Book\n3.Exit")
    ch = int(input("Enter Choice: "))
    if ch == 1:
        lib.show_books()
    elif ch == 2:
        title = input("Enter book title: ")
        lib.issue_book(title)
    elif ch == 3:
        break
    else:
        print("Invalid option")

########################################################################
# Task: 73
import requests

class WeatherApp:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather" # Invalid API key

    def get_weather(self, city):
        params = {
            "q": city,
            "appid": self.api_key,
            "units": "metric"
        }

        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()

            if response.status_code == 200:
                print(f"\n🌤️ Weather in {city.capitalize()}:")
                print(f"Temperature: {data['main']['temp']}°C")
                print(f"Condition: {data['weather'][0]['description'].title()}")
                print(f"Humidity: {data['main']['humidity']}%")
                print(f"Wind Speed: {data['wind']['speed']} m/s")
            else:
                print("❌ City not found. Try again.")
        except Exception as e:
            print("Error occurred:", e)

# === Object Creation and Method Call ===

if __name__ == "__main__":
    print("🌦️ Welcome to the OOP-Based Weather App")
    api_key = "your_api_key_here"  # Replace with real API key
    city = input("Enter city myname: ")

    app = WeatherApp(api_key)  # ← Object bna diya
    app.get_weather(city)      # ← Method call kiya

#############################################################################

import pyttsx3
engine = pyttsx3.init()
engine.say()

engine.runAndWait()

'''
from ast import increment_lineno
from collections import abc
from dataclasses import replace
from functools import reduce
from random import randint, choice
from traceback import print_list

from fontTools.misc.cython import returns
from numpy.ma.core import append

from pyparsing import countedArray
from win32evtlogutil import langid

# print("hella\\ guy")
#
# letter = ("kanu", 23, 45, "hello")
# print(type(letter))
# print(letter)
#
# a = ["hello",3,34,45,45,45,45,"kanu"]
# print(type(a))
# print(a)
#
# no = a.count(45)
# print(no)
# iu = a.index(34)
# print(iu)
#
# length = (0,1,2,3,4,5,6,7,8,9)
# print(length)
# print(type(length))
# print(len(length))
#
# print(max(length))
# print(min(length))
# print(7 in length)
#
# marks = []
#
# f1 = input("Enter the number ")
# marks.append(f1)
# f2 = input("Enter the number ")
# marks.append(f2)
# f3 = input("Enter the number")
# marks.append(f3)
# f4 = input("Enter the number")
# marks.append(f4)
# f5 = input("Enter the number")
# marks.append(f5)
# f6 = input("Enter the number")
# marks.append(f6)
# f7 = input("Enter the number")
# marks.append(f7)
# marks.pop()
# print(marks)
#
# text = input("Enter the sentence")
# vowels = "aeiouAEIOU"
# count = sum(1 for ch in text if ch in vowels)
# print("Vowels count:", count)
#
# word = input("Enter any word: ")
# reverse = word[::-1]
# print("Reversed the word: ",reverse)

# word = input("Enter the word")
# if word == word[::-1]:
#     print("the word is palindrome")
# else:
#     print("this is not palindrome")
#
# sentence = input("Enter the sentence")
# words = sentence.split()
# print("The sentence:", len(words))
#
#
# # 🌟 Python Mini String Project with Delete and Save Option
#
# def string_operations(s):
#     print("\n📚 String Proof & Operations:")
#     print("Original String:", s)
#     print("Length:", len(s))
#     print("Uppercase:", s.upper())
#     print("Lowercase:", s.lower())
#     print("First 5 chars:", s[:5])
#     print("Last 3 chars:", s[-3:])
#     print("Count of 'a':", s.count('a'))
#     print("Position of 'e':", s.find('e'))
#
# # 🔰 Step 1: Input
# text = input("Enter your string: ")
# string_operations(text)
#
# # 🗑️ Step 2: Delete Option
# choice = input("\nDo you want to delete part of the string? (yes/no): ").lower()
# if choice == "yes":
#     part = input("Enter the part to delete: ")
#     if part in text:
#         text = text.replace(part, "")
#         print("Updated string after deletion:", text)
#     else:
#         print("Text not found in string!")
#         print("Text not found in string hello")
#
# # 💾 Step 3: Save Option (simulate saving)
# save = input("\nDo you want to save the final string? (yes/no): ").lower()
# if save == "yes":
#     with open("saved_string.txt", "w") as f:
#         f.write(text)
#     print("✅ String saved to 'saved_string.txt'")
# else:
#     print("String not saved.")

###########################################################################

# 🔰 Mini String Editor Project in Python
#
# def string_proof(s):
#     print("\n📋 String Properties:")
#     print("Original:", s)
#     print("Type:", type(s))
#     print("Length:", len(s))
#     print("Upper:", s.upper())
#     print("Lower:", s.lower())
#     print("Sliced [0:4]:", s[0:4])
#     print("Reversed:", s[::-1])
#
# def delete_part(s):
#     part = input("Enter part to delete: ")
#     if part in s:
#         s = s.replace(part, "")
#         print("✔️ Updated String:", s)
#     else:
#         print("❌ Part not found.")
#     return s
#
# def save_string(s):
#     with open("final_string.txt", "w") as f:
#         f.write(s)
#     print("💾 String saved to 'final_string.txt'.")
#
# # 🔁 MAIN PROGRAM
# text = input("🔤 Enter a string: ")
#
# while True:
#     print("\n🔘 Menu:\n1. Show String Info\n2. Delete Part\n3. Save\n4. Exit")
#     choice = input("Enter choice: ")
#
#     if choice == '1':
#         string_proof(text)
#     elif choice == '2':
#         text = delete_part(text)
#     elif choice == '3':
#         save_string(text)
#     elif choice == '4':
#         print("🚪 Exiting Program.")
#         break
#     else:
#         print("❌ Invalid Choice .")
#
# ################################################################
#
# import random
#
# words = ["butterfly", "tiger", "python", "jungkook", "purple"]
# word = random.choice(words)
# display = ['_'] * len(word)
# attempts = 6
#
# print("🎯 guess the word! You have", attempts, "chances.")
#
# while attempts > 0 and '_' in display:
#     guess = input("Guess a letter: ").lower()
#     if guess in word:
#         for i in range(len(word)):
#             if word[i] == guess:
#                 display[i] = guess
#         print("✅", ' '.join(display))
#     else:
#         attempts -= 1
#         print("❌ Wrong! Attempts left:", attempts)
#
# if '_' not in display:
#     print("🎉 You guessed it:", word)
# else:
#     print("😢 Game Over! The word was:", word)

###############################################################
# print("💜 Welcome to JungCodeBot — Talk to Jungkook!")
#
# while True:
#     msg = input("You: ").lower()
#
#     if "hello" in msg or "hi" in msg:
#         print("JK: Annyeong 💜 I'm your golden maknae!")
#     elif "how are you" in msg:
#         print("JK: I'm fine... thinking about ARMY as always 😊")
#     elif "i love you" in msg:
#         print("JK: Saranghae 💜 You're my everything!")
#     elif "sad" in msg:
#         print("JK: Don’t be sad. You’re more beautiful when you smile 🌈")
#     elif "song" in msg or "sing" in msg:
#         print("JK: Singing ‘Euphoria’ just for you 🎶💫")
#     elif "quote" in msg:
#         print("JK: “Effort makes you. You will regret someday if you don’t do your best now.” 🐰")
#     elif "bye" in msg:
#         print("JK: Bye bye~ Take care, my shining star ✨")
#         break
#     else:
#         print("JK: Aigoo~ I didn’t get that... but I still purple you! 💜")

##################################################################################################
# import random
#
# questions = {
#     "You are the cause of my euphoria": "euphoria",
#     "I was lost but I found you": "begin",
#     "Monday, Tuesday, Wednesday": "seven",
#     "Every time I miss you": "still with you",
#     "I'm the one I should love in this world": "epiphany",  # bonus!
# }
#
# line = random.choice(list(questions.keys()))
# print("🎤 Guess the Jungkook/BTS song:")
# print("Line: ", line)
#
# ans = input("Your answer:").lower()
# if ans == questions[line]:
#     print("🎉 Correct! You're a true ARMY 💜")
# else:
#     print("😢 Oops! Right answer was:", questions[line])
##################################################################################################
# import random
#
# questions = {
#     "lachimolala":"jimin",
#     "Flower Flower Flower":"jungkook",
#     "I'm a good boy":"v",
#     "Raaaaaaaapp Monster..........":"jungkook",
#     "night apple is poison, but I'm ok":"jungkook",
#     "mochi baby":"suga",
#     "destroyed monster":"rm",
#     "I'm your hope, you are my hope, I'm jhope":"jhope",
#     "I'm world wide handsome":"jin",
#
#
# }
# line = random.choice(list(questions.keys()))
# print("Guess line of BTS:")
# print("Line: ",line)
#
# ans = input("Your answer:").lower()
# if ans == questions[line]:
#     print("🎉 Correct! You're a true ARMY 💜")
# else:
#     print(" 😢 Oops! Right answer was:", questions[line])
##################################################################################

# #Fortune Teller
#
# import random
#
# myname = input("Enter your myname: ")
#
# fortunes = [
#     "You will have a wonderful day!",
#     "Something unexpected is coming your way 🌈",
#     "Today is a perfect day to try something new.",
#     "A small act of kindness will bring big joy 😊",
#     "Your smile is your luck today!"
# ]
# print(f"{myname}, your fortune:{random.choice(fortunes)}")
#
# #####################################################################################
# d = {}
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# myname = input("Enter the your myname:")
# lang =  input(open())
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# myname = input("Enter the your myname:")
# lang = input("Enter the your language:")
# d.update({myname:lang})
#
# print(d)

# b = int(input("Enter the number"))
# if(b>=18):
#     print("yes")
# else:
#     print("no")
#
# a = 1
# while(a<51):
#     print(a)
#     a+=1
#
# c = 1
# while(c<50):
#     print(c)
#     c+=1
# d = 1
# while(d<11):
#     print(d)
#     d+=1
# e = 11
# if(e>=12):
#     print(e)
# else:
#     print("n")
# s=1
# while(s<90):
#     print(s)
#     s+=1
#
# p1 = "Make a lot of money"
# p2 = "Buy Now"
# p3 = "subscribe this"
# p4 = "check this"
#
# msg = input("Enter any comment:")
#
# if ((p1 in msg)or(p2 in msg)or(p3 in msg)or(p4 in msg)):
#     print("this comment is spam")
# else:
#     print("this comment is not spam")
#
# marks = int(input("Enter any marks:"))
#
# if (marks<=100 and marks>=90):
#     grade = "A+"
# elif (marks<=90 and marks>=80):
#     grade = "A"
# elif (marks<=80 and marks>=70):
#     grade = "B"
# elif (marks<=70 and marks>=60):
#     grade = "C"
# elif (marks<=50 and marks>=40):
#     grade = "D"
# else:
#     grade = "F"
# print("your Grade is: ",grade)

# financial =  input("Enter your condition:")
# if (financial=="high"):
#     print("your financial condition is perfect")
# elif(financial=="medium"):
#     print("your financial condition is normal")
# else:
#     print("your financial condition is bad")
# print("Concentrate on your work/career.")

# i=1
# while(i<11):
#     print(i)
#     i+=3
#for variable in sequence
# for i in range(1,11):
#     print(i)
#
# for char in "bye":
#     print(char)
#
# fruits = ["apple","banana","grapes","mango"]
# for fruit in fruits:
#     print(fruit)
#
# for i in  range(1,3):
#     print("loop",i)
# else:
#     print("loop finished")
#
# for i in range(1,3):
#     for j in range(2,4):
#         print(f"i={i},j={j}")
#
# for i in range(1,6):
#     if i == 3:
#         continue
#     if i == 5:
#         break
#     print(i)
#
# i =1
# while i<=10:
#     if i==6:
#         break
#     print(i)
#     i+=1
#
# for letter in "python":
#     if letter=="o":
#         break
#     print(letter)
#
# i = 0
# while i<5:
#     i+=1
#     if i == 4:
#         continue
#     print(i)
#
# while True:
#     user_input = input("Enter something (type 'exit' to quit): ")
#     if user_input == "exit":
#         print("You exited.")
#         break
#     print("you typed:",user_input)

# num = int(input("Enter a number: "))
#
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a prime number")
#             break
#     else:
#         print(num, "is a prime number")
# else:
#     print(num, "is not a prime number")

# n = int(input("Enter the number"))
# for i in range(1,n+1):
#     print(" "*(n-i), end="")
#     print("*"*(2*i-1), end="")
#     print(" ")
#
# n = int(input("Enter the number"))
# for i in range (1,11):
#     print(f"{n} X {i} = {n*i}")
#
# n = int(input("Enter the number"))
# for i in range(1,11):
#     print(f"{n} X {11-i} = {n*(11-i)}")
#
# a= int(input("Enter the number"))
# b= int(input("Enter the number"))
# c= int(input("Enter the number"))
# avg = (a+b+c)/3
# print(avg)

# def average():
#     a = int(input("Enter the number"))
#     b = int(input("Enter the number"))
#     c = int(input("Enter the number"))
#     avg = (a + b + c) / 3
#     print(avg)
#
# average()
# average()

# def add_number(a,b):
#     return a+b
#
# print("Sum:",add_number(2,3))
#
# def is_prime(n):
#     if n <=1:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n % i == 0:
#             return False
#         return True
#
# print("is 7 prime?",is_prime(7)) # odd number(1,3,5,7) is true and even number(2,4,6,8) is false
#
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)
# print("Factorial number is: ",factorial(4))
#
# def reverse_string(s):
#     return s[::-1]
# print(reverse_string("hello"))
#
# def palindrome(s):
#     return s == s[::-1]
# print("Is madam a palindrome?",palindrome("madam"))
#
# def find_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# print("the maximum value is:",find_max(10,20))
#
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for char in text:
#         if char in vowels:
#             count +=1
#     return count
# print(count_vowels("hello"))
#
# def check_number(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# print("the check number is:",check_number(4))
#
# def simple_interest(p,r,t):
#     return (p+r+t)/100
# print(simple_interest(2,3,4))

# def check_char(ch):
#     if ch.lower() in "aeiou":
#         return "vowels"
#     else:
#         return "constant"
# print(check_char("a"))
#
# def countdown(n):
#     if n==0:
#         print("Done!")
#     else:
#         print(n)
#         countdown(n-1)
# countdown(5)
#
# def add(a,b):
#     return a+b
# print(add(2,3))
#
# def sub(a,b):
#     return a-b
# print(sub(5,6))
#
# def multiple(a,b):
#     return a*b
# print(multiple(3,5))
#
# def division(a,b):
#     return a/b
# print(division(4,2))

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(0) = 5 x 4 x 3 x 2 x 1

factorial(n) = n * factorial(n-1)

'''

# def factorial(n):
#     if (n==1 or n==0):
#         return 1
#     return  n * factorial(n-1)
# print(factorial(5))
#
# def rem (l , word):
#     n = []
#     for items in l:
#         if not (items == word):
#             n.append(items.strip(word))
#     return n
# l = ["Harry", "Rahul", "Vedika", "Nonsense"]
# print(rem(l,"ae"))
#
# import random
#
# computer = random.choice([1,0,-1])
# youstr = input("Enter your choice:")
# youDict = {"s":1, "w":-1 , "g":0}
# reverseDict = {1:"Snake" , -1:"Water" , 0:"Gun"}
#
# you = youDict[youstr]
#
# print(f"you chose {reverseDict[you]}\nComputer choice:{reverseDict[computer]}")
# if(computer == you):
#     print("Its a draw!")
# else:
#     if(computer == -1 and you == 1):
#         print("You Win!")
#     elif (computer == -1 and you == 0):
#         print("You Lose!")
#     elif (computer == 1 and you == -1):
#         print("You Win!")
#     elif (computer == -1 and you == 0):
#         print("You lose!")
#     elif (computer == 0 and you == 1):
#         print("You Win!")
#     else:
#         print("Something went wrong")
#
# f = open("file.txt","r")
# data = f.read()
# print(data)
# f.close()
#
# st = "This is a beginner of python "
# f = open("hiscore.txt","w")
# f.write(st)
# f.close()

# f = open("Myfile.txt")
# lines = f.readlines()
# print(lines , type(lines))
# line1 = f.readline()
# print(line1, type(line1))
#
# line2 = f.readline()
# print(line2, type(line2))
#
# line3 = f.readline()
# print(line3, type(line3))
#
# line4 = f.readline()
# print(line4,type(line4) )
#
# f.close()
# f = "this is the beginners of python"
# line = f.readline()
# while(line != ""):
#     print(line)
#     line = f.readline()
# f.close()

# import random
# def game():
#     print("Yu are playing a game.")
#     score = random.randint(1,62)
#     #fetch the hiscore
#     with open("hiscore.txt") as f:
#         hiscore = f.read()
#         if (hiscore!= ""):
#             hiscore = int(hiscore)
#         else:
#             hiscore= 0
#     print(f"your score is: {score}")
#     if score>hiscore:
#         # write this high sore of file
#         with open("hiscore.txt","w") as f:
#             f.write (str(score))
#     return score
# game()

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#     with open (f"table/table_{n}.txt", "w") as f :
#         f.write(table)
#
# for i in range(2,21):
#     generateTable(i)

# # Note: folder banana hai us folder k
# # a name table rakhna h fir us me
# # ala-alag file me table likhe aaenge
# # 2 to 20 --->( def generateTable )

# class Employee():
#     name= "Kanika"
#     salary = 1200000
#     language = "python"
#
# my = Employee()
# my.name = "Kanika"
# print(my.name,my.language,my.salary)
#
# your = Employee()
# your.name = "yourName"
# print(your.name,your.language,your.salary)

# class Employee:
#     name = "Kanika"
#     language = "python" #this is class
#     salary = 12000000
#
#     def __init__(self):        # dunder (__init__) is automatically called class of object is created
#         print("Hello guys!")
#
#     def getInfo(self):
#         print(f"this isa language {self.language}. this is a salary {self.salary}.")
#
#     @staticmethod
#     def greet(self):
#         print("Good morning")
#
# mine = Employee()
# mine.language = "Java" #this is a instances
# print(mine.language,mine.salary)
#
# # Employee.getInfo() #error
#
# class Programmer:
#     company = "Microsoft"
#     yourCompany = "Google"
#     def __init__(self,salary,name,pin):
#         self.salary= salary
#         self.name = name
#         self.pin = pin
#
# p= Programmer(12000000,"Kanika",1234)
# print(p.company,p.pin,p.salary,p.name)
# r= Programmer(15000000,"Your",125634)
# print(r.yourCompany,r.pin,r.salary,r.name)

# class Calculator:
#     def __init__(self, n):
#         self.n = n
#     def square(self):
#         print(f"The square is {self.n * self.n}")
#     def cube(self):
#         print(f"The cube is {self.n * self.n * self.n}")
#     def squareRoot(self):
#         print(f"The squareRoot is {self.n*1/2}")
# a = Calculator(5)
# a.square()
# a.cube()
# a.squareRoot()
#
#
# class Demo:
#     a = 4
#
# o = Demo()
# print(o.a) # print the class attribute because instance attribute is not present
# o.a = 0  # instance attribute is set
# print(o.a) # print the instance attribute because instance attribute is present
# print(Demo.a) #print with class attribute
#
#
# from  random import randint
# class Train :
#     def __init__(self,TrainNo):
#         self.TrainNo = TrainNo
#
#     def  book(self,fro,to):
#         print(f"Ticket is booked in train no.{self.TrainNo} from {fro} to {to}")
#
#     def getStatus(self):
#         print(f"train is {self.TrainNo} running on time")
#
#     def getFare(self,fro,to):
#         print(f"Ticket fare is train no. {self.TrainNo} from {fro} to {to} is {randint(222 ,5555)}")
# t = Train(12345)
# t.book("Delhi","Indore")
# t.getStatus()
# t.getFare("kashmir","kerala")
#
# class Employee:
#     a= 1
#     @classmethod
#     def  show(cls):
#         print(f"The class attribute of a is {cls.a}")
#
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]  # split means one word like "Kanika"
#         self.lname = value.split(" ")[1]
#
#
# e = Employee()
# e.a = 45
# e.name = "Kanika Sharma"
# print(e.fname)
#
# e.show()
#
# class Number:
#     def __init__(self,n):
#         self.n = n
#     def __add__(self, name):
#         return self.n + name.n
#
# n = Number(1)
# m = Number(2)
#
# print(n+m)
#
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j")
#
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
#
# a = TwoDVector(1,2)
# a.show()
# b = ThreeDVector(1,2,3)
# b.show()
#
# class Animals:
#     pass
# class Pets(Animals):
#     pass
# class Dog(Pets):
#     @staticmethod
#     def bark():
#         print("Bow Bow!")
#
# d = Dog()
# d.bark()
#
#
# class Employee:
#     def __init__(self):
#         print("The Employee is constructor.")
#     a = 1
# class Programmer(Employee):
#     def __init__(self):
#         print("The Programmer is constructor.")
#     b =2
# class Manager(Programmer):
#     def __init__(self):
#         super(). __init__()
#         print("The Manager is Constructor")
#     c =3
# o = Employee()
# print(o.a)
# o1 = Programmer()
#
# class Employee:
#     a = 1
#     @classmethod
#     def show(cls):
#         print(f"The class attribute of a is {cls.a}")
#
#     @property
#     def name(self):
#         return f"{self.fname} {self.lname}"
#
#     @name.setter
#     def name(self,value):
#         self.fname = value.split(" ")[0]
#         self.lname = value.split(" ")[1]
#
#
# e = Employee()
# e.name = "Kanika Sharma"
# print(e.fname, e.lname)
# e.a =23
# e.show()
#
# class Number:
#     def __init__(self , n):
#         self.n = n
#
#     def __add__(self, num):
#         return self.n + num.n
# n = Number(1)
# m = Number(2)
#
# print(n+m)
#
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self. j = j
#     def show(self):
#         return f"The vector is {self.i}i + {self.j}j"
#
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         return f"The vector is {self.i}i + {self.j}j + {self.k}k"
#
# T = TwoDVector(1,2)
# print(T.show())
# Th = ThreeDVector(1,2,3)
# print(Th.show())
#
# class Employee:
#     salary = 234
#     increment = 20
#     @property
#     def salaryAfterIncrement(self):
#         return self.salary + self.salary* (self.increment/100)
#
#     @salaryAfterIncrement.setter
#     def salaryAfterIncrement(self,salary):
#         self.increment = ((salary / self.salary) -1)*100
#
# e = Employee()
# print(e.salaryAfterIncrement)
# e.salaryAfterIncrement = 280.8
# print(e.increment)
#
# class Complex:
#     def __init__(self, r, i):
#         self. r = r
#         self.i = i
#     def __add__(self, c2):
#         return Complex(self.r + c2.r , self.i + c2.i)
#
#     def __mul__(self, c2):
#         real_part = self.r * c2.r - self.i * c2.i
#         imag_part = self.r * c2.i +  self.i * c2.r
#         return Complex(real_part,imag_part)
#
#     def __str__(self):
#         return f"{self.r} , {self.i}i"
#
# c1 = Complex(1,2)
# c2 = Complex(3,4)
# print(c1+c2)
# print(c1*c2)
#
# class Vector:
#     def __init__(self,l):
#         self.l = l
#     def __len__(self):
#         return len(self.l)
#
# v = Vector([1,2,3])
# print(len(v))


#************************************************************************************#
#Guess the Number#
#
# import random
# n = random.randint(1,100)
# a = -1
# guesses = 1
# while(a != n):
#     a = int(input("Guess any number:"))
#     if(a>n):
#         print("Lower number please.")
#         guesses +=1
#     elif(a<n):
#         print("Higher number please. ")
#         guesses+=1
# print(f"You have the guesses number {n} correctly in {guesses} attempts.")

# #Using walrus operator
# if (n := len([1,2,3,4,5])) > 3:
#     print(f"List is too long ({n} elements excepted <=3)")
#     #Output: List is too long (5 elements excepted <=3)
#
# # Without walrus
# data = input("Data: ")
# while data != "stop":
#     print(f"You typed: {data}")
#     data = input("Data: ")
#
# # With w
# # Without walrus
# data = input("Data: ")
# while data != "stop":
#     print(f"You typed: {data}")
#     data = input("Data: ")
#
# # With walrus
# while (data := input("Data: ")) != "stop":
#     print(f"You typed: {data}")

# # Type defination of python
# num:int = 12
# decimal:float = 12.4
# name:str = "Kanika"
# boolean : bool = True
# my_list : list = [1,2,3]
# my_tuple : tuple = (1,2,3)
# my_set : set = {1,2,3}
# # my_dict : dict[int,str] = ["name": "Kanika" ,"age": 20]
# print(num)
#
# from typing import List,Dict,Tuple,Union,Set
# numbers : List[int] = [1,2,3]
#
# person : Tuple[int,str,int] = (1,"kanika",2)
#
# person2 : Set[Union[int,str]] = {1,"kanika"}
#
# scores: Dict[str, int] = {
#     "math": 90,
#     "science": 85
# }
#
# n : int = 5
# name1 : str = "kanika"
#
# def sum(a:int,b:int) -> int:
#     return a+b
#
#
# # Match case (Similar to switch cse)
# command = "Start"
#
# def show(status):
#     match status:
#         case 200:
#             return "OK"
#         case 404:
#             return "Not found"
#         case 567:
#             return "Internal Server Error"
#         case _:
#             return "Unknown status"
# print(show(200))
#
# command = "start"
# match command:
#     case "start":
#         print("Starting...")
#     case "stop":
#         print("Stoping...")
#     case "pause":
#         print("Pausing...")
#     case _:
#         print("Unknown command")
#
# # try exception
# try:
#     n = int(input("Enter any number:"))
#     print(n)
# except ValueError as v:
#     print("Hello")
#     print(v)
# except Exception as e:
#     print(e)
#
# print("Thank you")
#
# try:
#     num = int(input("Enter any number:"))
#     result = 10/num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("you can't divide by zero.")
# except ValueError:
#     print("Please enter a valid number.")
#
# a = int(input("Enter first number"))
# b = int(input("Enter second number"))
#
# if(b==0):
#     raise ZeroDivisionError ("Hey our program is not meant to divide numbers by zero.")
# else:
#     print(f"The division of a/b {a/b}")

# def main():
#     try:
#         num = int(input("Enter any number:"))
#         print(num)
#     except Exception as e:
#         print(e)
#         return # jesa ki mene niche bataya ki  return k baad k kuchh bhi code run nhi hote h
#
#     # else:
#     #     print("Iam inside else.")
#     finally:
#         print("I am inside finally")
#
# main()
#
# # finally command chahe kuchh bhi ho chalega hi chale ga jabki return k baad ka kuchh print nhi hota h function ho ya kuchh bhi
#
# global variable use
# a=34
# def func():
#     #global a
#     a = 1
#     print(a)
#
# func()
# print(a)

# #if __name__ == '__main__':
# def greet():
#     print("Hello")
#     if __name__ == '__main__':
#         print("Running directly!")
# greet()

#Now if you do this in another file:

# import example
#
# ➡️ Output:
#
# (Only): Hello from greet() -- if called manually
#
# (The print("Running directly!") won't run because it's inside the if __name__ == '__main__' block.)

#l = {1,2,34,4}

# index = 0
# for item in l:
#     print(f"The items is {index} is {item}")
#     index +=1

# This is same output with enumerate

# for index , items in enumerate(l):
#     print(f"The item is {index} is {items}")

# list Comprehension
# myList = [1,2,3,4,5]
# squaredList = []
# for items in myList:
#     squaredList.append(items*items) # append use in
# print(myList)
# print(items)
# print(squaredList)
#
# squaredList = [i*i for i in myList]
# print(squaredList)

# Practice set
# try:
#     with open("1.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("2.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)
# try:
#     with open("3.txt", "r") as f:
#         print(f.read())
# except Exception as e:
#     print(e)

# a = [1,2,3,4,5,6,7]
# for i,items in enumerate(a):
#     if i==2 or i==4 or i==6 : # put the position of items in list
#         print(items)
#
# n = int(input("Enter any number:"))
# table = [n*i for i in range(1,11)]
# print(table)
#
# try:
#     a = int(input("Enter any number"))
#     b = int(input("Enter any other number"))
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinite")

# n = int(input("Enter any number:"))
# table = [n*i for i in range(1,11)]
# with open("table.txt","w") as f:
#     f.write(f"Table of {n}: {str(table)}\n ")

# print(True+True+False)
#

# # Declare second integer, double, and String variables.
# i = 4
# d = 4.0
# s = 'HackerRank '
# # Read and save an integer, double, and String to your variables.
# n = int(input())
# o = float(input())
# p = input()
# # Print the sum of both integer variables on a new line.
# print(n+i)
# # Print the sum of the double variables on a new line.
# print(o+d)
# # Concatenate and print the String variables on a new line
# print(s+p)

# Lambda method
# def square(n):
#     return n*n
# square = lambda x : x*x
# print(square(5))
#
# sum1 = lambda a,b,c: a+b+c
# print(sum1(1,2,3))

# Join method
# a = ['Harry','Kanika','Sharma','Aditi']
#
# final = "::".join(a)
# print(final)

#Format Method (Strings)

# Strip command
# text = "   Hello    "
# print(text.strip())

# format command
# a = "{1} is a good {0}".format("Kanika", "girl")
# print(a)

# if __name__ == '__main__':
#     n = int(input().strip())
#     if n % 2 !=0:
#         print("Weird")
#     elif n % 2 == 0 and 2 <= n <= 5:
#         print("Not Weird")
#     elif n % 2 == 0 and 6 <= n <= 20:
#         print("Weird")
#     elif n % 2 == 0 and n > 20:
#         print("Not Weird")

# n = int(input("Enter any number:"))
# if n % 2 !=0:
#     print("odd")
# elif n % 2 == 0:
#     print("even")

# Map, Filter, Reduce

# Map Example
# l = [1,2,3,4,5,6]
# square = lambda x: x*x
# spList = map (square,l)
# print(list(spList))

#Filter Example
# def even(n):
#     if n%2 == 0:
#         return True
#     return False
# print(even(4))
# onlyEven = filter(even, l)
# print(list(onlyEven))

# Reduce Example
# def sum(a,b):
#     return a+b
# mul = lambda x,y:x*y
#
# print(reduce(sum,l))
# print(reduce(mul,l))


# practice set
# name = input("Enter your name:")
# marks = int(input("Enter your marks:"))
# phone = int(input("Enter your phone number:"))
#
# s = "The name of the student is {} , his marks are {} and his phone number is {}.".format(name,marks,phone)
# print(s)
#
# table = [str(7*i) for i in range (1,11)]
# print(table)
# s1 = "\n" .join(table)
# print(s1)
#
# def divisible5(n):
#     if(n%5 == 0):
#         return True
#     return False
#
# a = [1,2,3,4,5,468,4356,756]
# f = list(filter(divisible5,a))
# print(f)
#
#
# from functools import reduce
# a1 = [111,34,56,65,78,98]
#
# def greater(a,b):
#     if(a>b):
#         return a
#     return b
# print(reduce(greater,a1))


# from flask import Flask
#
# app = Flask(__name__)
#
# @app.route("/")
# def hello_world():
#     return "<p> Hello World </p>"
#
# app.run()


# *****************~~~~MEGA PROJECT ONE~~~~~***********************
# ************~~~~JARVIS VIRTUAL ASSISTANT~~~~~********************

#
# n = int(input("Enter the number:").strip())
# arr = []
# for i in range(n):
#     val = int(input(f"Enter element {i + 1}: "))
#     arr.append(val)
# print("Your array is:", arr)

#Haan, agar tum print(*arr) use karte ho to Python list ke elements ko space-separated print karega.
#Agar * nahi lagate, to pura list square brackets ke saath print hota hai, jaise:

#Without *
# arr = [2, 3, 4, 1]
# print(arr[::-1])
#
# # Output:
# # [1, 4, 3, 2]
#
# #With *
#
# arr = [2, 3, 4, 1]
# print(*arr[::-1])

# Output:
# 1 4 3 2




# if __name__ == '__main__':
#     n = int(input("Enter first line").strip())
#
#     arr = list(map(int, input("Enter second line:").rstrip().split()))
#     print(*arr[::-1])

# Output :
# Enter first line4
# Enter second line:1 2 34 4
# 4 34 2 1

# Dictionaries and map
# Keys and value

# Dictionary storing student marks
my_dict = {"name":"Kanika", "age": 20}

# Access value
print(my_dict["age"])
# Output: 20

# Add a new key-value
my_dict["city"] = "Indore"
print(my_dict)

# Update value
my_dict["age"] = 21
print(my_dict)

# Delete a key-value
del my_dict["name"]
print(my_dict)

# Check if a key exists
my_dict = "city" in my_dict
print(my_dict)


my_dict = {"name": "Kanika", "age": 20}

print(my_dict.keys())    # dict_keys(['name', 'age'])
print(my_dict.values())  # dict_values(['Kanika', 20])
print(my_dict.items())   # dict_items([('name', 'Kanika'), ('age', 20)])


# Get with default value
print(my_dict.get("city","not found"))

# Remove and return value
print(my_dict.pop("age"))

# Dictionaries in map
phone_book = {
    "Amit": "9876543210",
    "Riya": "9123456780"
}
# Lookup
print(phone_book["Riya"])  # Output: 9123456780



#Iterating Over a Dictionary
students_marks = {"Kanika": 89, "Aditi": 93, "Vedika": 67}

# Loop through keys
for name in students_marks:
    print(name, students_marks[name])

# Loop through key-value pairs
for name,marks in students_marks.items():
    print(f"{name} scored {marks}")

# Task :
# Input:
# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
#
# n = int(input().strip())  # number of phone book entries
# phone_book = {}
#
# # Read n lines of name and phone number
# for _ in range(n):
#     name, number = input().strip().split()
#     phone_book[name] = number
#
# # Read queries until no more input
# while True:
#     try:
#         query = input().strip()
#         if query in phone_book:
#             print(f"{query}={phone_book[query]}")
#         else:
#             print("Not found")
#     except EOFError:
#         break


# Key parts of a recursive function
# Base Case → The condition where recursion stops (prevents infinite loop).
# Recursive Case → The part where the function calls itself.

# Eg.

# def factorial(n):
#     if n==0 or n==1: # Base Case
#         return 1
#     else:
#         return n * factorial(n-1)  # Recursive Case
# print(factorial(4))
#
# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return factorial(n-1) + fibonacci(n-2)
# for i in range(4):
#     print(fibonacci(i),end=" ")

# Important Notes:
# Base case is necessary to avoid infinite recursion.
# Recursive solutions can be slower and use more memory than loops.
# Python has a recursion depth limit (~1000 calls). You can check with:

# import sys
# print(sys.getrecursionlimit())

# def reverse_string(s):
#     if len(s) == 0:
#         return s
#     else:
#         return reverse_string(s[1:]) + s[0]
# print(reverse_string("hello"))

#############################################################################
#Decimal to Binary Conversion in Python
# def decimal_to_binary(n):
#     return bin(n).replace("0b","")
# num = int(input("Enter the decimal number"))
# print(decimal_to_binary(num))

#Binary to Decimal Conversion in python
# def binary_to_decimal(b):
#     return int(b,2)
# num1 = input("Enter the binary number")
# print(binary_to_decimal(num1))


##############################################################################
#Menu-driven (Both in One Program)
# def decimal_to_binary(n):
#     return bin(n).replace("0b","")
# def binary_to_decimal(b):
#     return int(b,2)
#
# while True:
#     print("\n 1. Enter Decimal number")
#     print("2. Enter Binary number")
#     print("3.Exit \n")
#
#     choice = int(input("Enter your choice:"))
#
#     if choice ==  1:
#         decimal = int(input("Enter the decimal number "))
#         print(decimal_to_binary(decimal))
#     elif choice == 2:
#         b = input("Enter the binary number ")
#         print(binary_to_decimal(b))
#     elif choice == 3:
#         print("Exiting...")
#         break
#     else:
#         print("Invalid choice try again...")



# Matrices 2D Array
# Eg, 3X3 matrix  :
arr = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(arr)


# Here:
# arr[0] → [1, 2, 3] (first row)
# arr[1][2] → 6 (row 1, column 2)

# 2D matrix
matrix1 =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for row in matrix1:
    print(row)

# Loop matrix
rows,cols = 3,3
matrix = [[0]* cols for i  in range(rows)]
print(matrix)


# Taking Input for 2D Array
# Example for a 3x3 matrix:
# matrix2 = []
# for i in range(3):
#     row = list(map(int,input().split()))
#     matrix2.append(row)
# print(matrix2)

matrix3 =  [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
for i  in range(len(matrix3)):
    for j in range(len(matrix3[0])):
        print(matrix3[i][j], end="  ")
    print()

# So, in Python:
# 2D Array = list of lists
# Can be created with loops or input
# Access using arr[row][col]


# 6 X 6  matrix
# matrix4 = []
# for i in range(6):
#     row = list(map(int, input().split()))
#     matrix4.append(row)
# print(matrix4)

# 6 X 6  matrix
# matrix5  = [[1, 2, 3, 4, 5, 6],
#             [1, 2, 3, 4, 5, 6],
#             [1, 2, 3, 4, 5, 6],
#             [1, 2, 3, 4, 5, 6],
#             [1, 2, 3, 4, 5, 6],
#             [1, 2, 3, 4, 4, 5]
#             ]
# for i in range(len(matrix5)):
#     for j in range(len(matrix5[0])):
#         print(matrix5[i][j],end="  ")
#     print()

# "for loop" se perfect one by one row me likhata hai

# alphabet1 = [
#     ['A','B','C'],
#     ['D','E','F'],
#     ['G','H','I']
# ]
#
# print(alphabet1)
# for i in alphabet1:
#     print(i)
#
# #Example 2: Input from User (alphabets instead of numbers)
#
# matrix = []
# rows, cols = 3,3
# print("Enter 3x3 matrix of alphabets:")
# for i in range(rows):
#     rows = input().split()
#    # print(rows)
#     matrix.append(rows)
# #print(matrix)
# print("\nYour Matrix:")
# for row in matrix:
#     print(" ". join(row))

#Example 3: Automatically Fill Alphabets
# matrix = []
# rows, cols = 3, 3
# ch = 65   # ASCII of 'A'
#
# for i in range(rows):
#     row = []
#     for j in range(cols):
#         row.append(chr(ch))
#         ch += 1
#     matrix.append(row)
#
# for r in matrix:
#     print(" ".join(r))

import numpy as np

# Normal Python
list1 = [1,2,3,4]
list2 = [5,6,7,8]
result = [list1[i]+list2[i] for i in range(len(list1))]
print(result)

# NumPy
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
print(arr1+arr2)


# Difference Summary
# Python → constructor hamesha __init__() hota hai.
# C++ / Java → constructor ka naam class ke naam jaisa hota hai.

# Or inherit ke liye super.__init__()
# lagate hai

#super().__init__(title, author)   # self nahi dena

# 🔹 In Object-Oriented Programming (OOP):
# Abstraction is achieved using:
# Abstract Classes – classes that cannot be instantiated directly and
# may have abstract methods (methods without implementation).
# Interfaces – they only declare methods, and classes that implement
# them must provide the method definitions.

####################################################################
# Abstraction method example

# from abc import ABCMeta, abstractmethod
# class Vehicle(object, metaclass=ABCMeta):
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     @abstractmethod
#     def display(self):
#         pass
# class Car(Vehicle):
#     def __init__(self,a,b,c):
#         super().__init__(a,b)
#         self.c = c
#     def display(self):
#         print("Hello , I am car")
#         print(f"{self.a}")
#         print(f"{self.b}")
#         print(f"{self.c}")
# a = input()
# b = input()
# c = input()
# d  = Car(a,b,c)
# d.display()

##### HACKER RANK Ka code hai #####

# from abc import ABCMeta, abstractmethod
# class Book(object, metaclass=ABCMeta):
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author
#     @abstractmethod
#     def display(): pass
#
# #Write MyBook class
# class MyBook(Book):
#     def __init__(self,title,author,price):
#         super().__init__(title,author)
#         self.price = price
#     def display(self):
#         print(f"Title: {self.title}")
#         print(f"Author: {self.author}")
#         print(f"Price: {self.price}")
#
#
# title=input()
# author=input()
# price=int(input())
# new_novel=MyBook(title,author,price)
# new_novel.display()


#  SCOPE  #
#Scope tells us where a variable exists and where we can use it in the code.
#Types of Scope in Python (LEGB Rule)

# Local (L):

# Variables defined inside a function.
# Accessible only within that function.

def func():
    x = 10
    print(x)
func()

# 2,Enclosing (E):

# Variables in the enclosing (outer) function when a function is nested.
# Inner function can access outer function variables.

def outer():
    y=20
    def inner():
        print(y)
    inner()
outer()

# Global (G):

# Variables defined at the top level of a script or declared as global inside a function.
# Accessible throughout the module.

z = 30

def show():
    print(z)
show()
print(z)

# Built-in (B):
# Names that Python has reserved already (like print, len, range).
# Available everywhere.

print(len([1,2,3]))


# HACKER RANK Code  (Scope)
# class Difference:
#     def __init__(self, a):
#         self.__elements = a
#         self.maximumDifference = 0
#
#     def computeDifference(self):
#         self.maximumDifference = max(self.__elements) - min(self.__elements)
#
# # End of Difference class
#
# _ = input()
# a = [int(e) for e in input().split(' ')]
#
# d = Difference(a)
# d.computeDifference()
#
# print(d.maximumDifference)

# 🔹 Exception kya hota hai?
# Exception = error situation jo program ke normal flow ko tod deti hai.
# Example:
# 10 / 0 → ZeroDivisionError
# int("abc") → ValueError
# Normally ye errors program ko crash kar dete hain.
# 🔹 raise Exception kya karta hai?
# 👉 Jab tum raise Exception("message") likhte ho, to tum apna khud ka error generate (throw) kar rahe ho intentionally.
# Ye error baaki ke errors ki tarah behave karta hai, aur agar try-except block me ho to catch ho sakta hai

# def check_number(x):
#     if x < 0:
#         raise Exception("Negative number not allowed")  # yaha error uthaya
#     return x * 2
#
# print(check_number(5))   # 10
# print(check_number(-3))  # yaha Exception hoga ( jo intentionally ho ra h)

#####################################################################################

# Linked list
# Stack and Queue
#
# import array
# # Binary Search (array sorted hona chahiye)
# def binary_search(arr,target):
#     left,right = 0, len(arr)-1
#     while left <= right :
#         mid = (left+right)//2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid+1
#         else:
#             left = mid-1
#     return -1
#
# sorted_arr = array.array('i', [10, 20, 30, 40, 50, 60])
# print("Binary Search 40:", binary_search(sorted_arr, 40))


# f = open("demo.txt","rt")
# data = f.read()
# print(data)
#
# line1 = f.readline() #first readline ke baad ek line ka space hota h \n ki vajah se
# print(line1)
#
# # print(type(data))
# f.close()
#
# f = open("demo.txt","a") #append k pehle ''write'' likha tha
# f.write("\nI want to learn Python advance")
# f.close()
#
# f = open("sample.txt","w")
# f.close()

# f = open("demo.txt","r+") # overwrite karne ka kaam karta h vo bhi suru se
# f.write("abc")
# print(f.read())
# f.close()


# f = open("demo.txt","w+") #data khali ho jaega
# # f.write("abc")
# print(f.read())
# f.write("abc")
# f.close()

# 'r'
# 'w'
# 'a'
# 'rt'
# 'wt'
# 'rb'
# 'wb'
# 'r+'
# 'w+'
# 'a+'

# ''with'' syntax
# with open("demo.txt","r") as f: # 'as' is a alias
#     data = f.read()
#     print(data)
#
# with open("demo.txt","w") as f:
#     f.write("new data")
#
#Deleting a file
#using the os module
# import os
# os.remove("sample.txt")

#Practice
# with open("practice.txt","r") as f:
#     data = f.read()
# new_data = data.replace("Java","python")
# print(new_data)
#
# with open("practice.txt","w") as f:
#       f.write(new_data)

# def check():
#     word = "learning"
#     with open("practice.txt","r") as f:
#         data = f.read()
#         if data.find(word) != -1 :  #''if word in data:''
#             print("found")
#         else:
#             print("Not found")
# check()

# def check_line():
#     word = "python"
#     data = True
#     line_no = 1
#     with open("practice.txt","r") as f:
#         while data:
#             data = f.readline()
#             if word in data:
#                 print(line_no)
#             line_no += 1
#     return -1
#
# check_line()


# with open("practice.txt","r") as f:
#     data = f.read()
#     print(data)
#
#     num = ""
#     for i in range(len(data)):
#         if data[i] == ",":
#             print(int(num))
#             num= ""
#         else:
#             num += data[i]

#ek or tarika h isi ka
# count = 0
# with open("practice.txt","r") as f:
#      data = f.read()
#
#      nums = data.split(",")
#      for val in nums:
#          if(int(val) % 2 == 0):
#              count += 1
# print(count)

