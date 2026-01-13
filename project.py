# first_name = "Kanika"
# print(f"My name is {first_name}")
#
# #type casting
# a = int("2") # agar normally hume amjh nhi aara h ki ye value kya h to type casting ka use karte h
# b = 4
# print(a+b)
#
# gpa  = 3.2
# print(type(gpa))
#
# gpa = int(3.2)
# print(gpa) #float tha per int me print hua
# print(type(gpa))
#
# b = 67
# b += 1
# print(b)
import json
#input
# name = input("What is your name")
# age = int(input("How old are you?"))
#
# age = age + 1
# print(f"My age is {age} years old" )

# #rectangle
# length = int(input("Enter the length "))
# breadth = int(input("Enter the breadth "))
# area = length*breadth
# print(f"The area is -> {area}cm")

#shopping cart
# item = input("Enter the item name: ")
# prize =  int(input("Enter the prize of item: "))
# quantity = int(input("How many would you like : "))
# total  = prize*quantity
# print(f"You have bought {quantity} {item}/s")
# print(f"Your total prize is: ${total}")

# Madlibs game
# word game where you create a story
# by filling in blanks with random words

#arthmetics
# friends = 10
# friends = friends + 1
# friends += 1
# friends = friends - 2
# friends -= 2
# friends = friends * 3
# friends *= 3
# friends = friends /2
# friends /= 2
# friends = friends ** 2
# friends **= 2
# friends = friends % 2
# friends %= 2
# print(friends)

# # maths functions
# x = 3.141234567
# y = 4
# z = 5
# result = round(x)
# result = abs(y)
# result = pow(4,3) #pow(base, exponent)  2^3 = 8  pow--> power
# result = max(x,y,z)
# result = min(x,y,z)
# print(result)

# import math
# x = 9.1
# print(math.pi)
# print(math.e)
# result = math.sqrt(x) square root of x
# result = math.ceil(x)
# result = math.floor(x)
# print(result)

# p = "7"
# q = "2"
#print(int("7"+"2")- int("2"+"7"))
# print(int(p+q)- int(q+p)) #45

import math
import time


# radius = float(input("Enter the radius of a circle: "))
# circumference = 2* math.pi*radius
# print(f"The circumference is : {round(circumference,2)}")
#
# radius = float(input("Enter the radius of a circle: "))
# area = math.pi * pow(radius,2)
# print(f"The area of circle is:  {round(area,2)}cm^2")

#calculates the hypotenuse of a right-angled triangle using the Pythagoras theorem!
# a = float(input("Enter side A: "))
# b = float(input("Enter side B: "))
# c  = math.sqrt(pow(a,2) + pow(b,2)) #math.sqrt() → takes the square root of the sum ./a^2+b^2
# print(f"the side of c: {c}")

#condition #dicision making
# name = input("Enter your name: ")
#
# if name == "":
#     print("You did not type in your name!")
# else:
#     print(f"Hello {name}")

# marks = int(input("Enter your marks: "))
# if marks >= 90:
#     print("A")
# elif marks >=80 and marks<90:
#     print("B")
# elif marks >=70 and marks<80:
#     print("C")
# elif marks >=40 and marks<70:
#     print("D")
# else:
#     print("F")

# Calculator

# operator = input("Enter an operator (+,-,*,/,%,**)")
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
#
# if operator == "+":
#     result = num1 + num2
#     print(f"The sum is {round(result,3)}") #round for short the point number #round(number, digits)
# elif operator == "-":
#     result = num1 - num2
#     print(f"The sub is {round(result,3)}")
# elif operator == "*":
#     result = num1 * num2
#     print(f"The multiple is {round(result,3)}")
# elif operator == "/":
#     result = num1 / num2
#     print(f"The div is {round(result,3)}")
# elif operator == "%":
#     result = num1 % num2
#     print(f"The mod is {round(result,3)}")
# elif operator == "**":
#     result = num1 ** num2
#     print(f"The .... {round(result,3)}")
# else:
#     print(f"{operator} operator is not valid..")

#python weight converter

# weight = float(input("Enter your weight: "))
# unit = input("Kilograms or Pounds? (K or L): ")
# #
# if unit == "K".lower():
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your weight is: {round(weight,1)} {unit}")
# elif unit == "L".lower():
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your weight is: {round(weight,1)} {unit}")
# else:
#     print(f"{unit} was not valid")

# Celcius and Fahrenheit (C/F)
# unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
# temp = float(input("Enter the temperature: "))
#
# if unit == "C":
#     temp = round((9 * temp) / 5 + 32, 1)
#     #(9 * temp) / 5 + 32
#     print(f"The temperature in Celsius is: {temp} C")
# elif unit == "F":
#     temp == round((temp - 32) * 5 / 9, 1)
#     #(temp - 32) * 5 / 9
#     print(f"The temperature in Fahrenheit is: {temp} F")
# else:
#     print(f"{unit} is an invalid unit of measurement")

#and or not
# temp = 0
# is_sunny = False
#
# if temp >= 28 and is_sunny:
#     print("It is HOT outside.")
#     print("It is SUNNY.")
# elif temp <= 0 and is_sunny:
#     print("It is Cold outside.")
#     print("It is SUNNY.")
# elif 28 > temp >0 and is_sunny:
#     print("It is WARM outside.")
#     print("It is SUNNY")
# elif temp >= 28 and not is_sunny:
#     print("It is HOT outside.")
#     print("It is CLOUDY.")
# elif temp <= 0 and not is_sunny:
#     print("It is Cold outside.")
#     print("It is CLOUDY.")
# elif 28 > temp >0 and not is_sunny:
#     print("It is WARM outside.")
#     print("It is CLOUDY")
# else:
#     pass

#condition
# num =  4
# a = 8
# b = 7
# age = 19
# temperature = 30
# user_role = "admin"
# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"
# max_num = a if a>b else b
# min_num = a if a<b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "HOT" if temperature > 20 else "COLD"
# access_level = "FULL Access" if user_role == "admin" else "Limited Access"
# print(access_level)

# name  = input("Enter your name: ")
# ph_no  = input("Enter your phone number: ")
# result = len(name)
# result = name.find("a")
# result = name.rfind("e")
# result = name.capitalize()
# result = name.upper()
# result = name.lower()
# result = name.isdigit()
# result = name.isalpha()
# result = ph_no.count("-")
# result = ph_no.replace("-"," ")

# print(result)

# print(help(int))

#exercise
#condition
# username = input("Enter the username: ")
#
# if len(username)> 12:
#     print("Your username can't be more than 12 character...")
# elif not username.find(" ") == -1:
#     print("Your username can't contain space...")
# elif not username.isalpha():
#     print("Your username can't contain number...")
# else:
#     print(f"Welcome {username}")

# indexing = accessing elements of a sequence using [] (indexing operator) [start : end :step]

# credit_number = "1234-5678-3456"
# print(credit_number[8])
# print(credit_number[::2])

#format  Specifier = {value:flags} format a value based on what flags are inserted
# '.' (number) = round to that may decimal places (fixed point)
# ':' (number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use plus sign to indiicate positive value
# := = place sign to leftmost position
# :  = insert a space before position numbers
# :, = comma separator
# price1 = 3.14159
# price2 = -987.65
# price3 = 12.34
# print(f"Price 1 is ${price1 : +,.2f}")
# print(f"Price 2 is ${price2 : +,.2f}")
# print(f"Price 3 is ${price3 : +,.2f}")

#while condition
# name = input("Enter your name: ")
# while name == "":
#     print("you did not enter your name")
#     name = input("Enter your name: ")
# print(f"hello {name}")

# age = int(input("Enter your age: "))
# while age <0:
#     print("Age can't be negative")
#     age = int(input("Enter your age: "))
# print(f"You are {age} year old..")

# food = input("Enter a food you like (q to quit): ")
#
# while not food == "q":
#     print(f"You like {food}")
#     food = input("Enter another food you like (q to quit): ")
# print("bye")
#
# num =  int(input("Enter a # between 1-10: "))
#
# while num < 1 or num > 10:
#     print(f"{num} is not valid..")
#     num =  int(input("Enter a # between 1-10: "))
# print(f"Your number is: {num}")

#Python compound interest calculator
# principle = 0
# rate = 0
# time = 0
# # interest = PxRxT/100
# while True:
#     principle = float(input("Enter the principle in year: "))
#     if principle < 0:
#         print("principle can't be les than  zero..")
#     else:
#         break
#
# while True:
#     rate = float(input("Enter the interest rate in year: "))
#     if rate < 0:
#         print("interest rate can't be les than  zero..")
#     else:
#         break
# while True:
#     time = float(input("Enter the time in year: "))
#     if time < 0:
#         print("time can't be less than  zero..")
#     else:
#         break
#
# total = principle * pow((1+ rate/100),time)
# print(f"Balance after {time} years/s: $ {total:,.2f}")

#for loop
# for i in range(1,11,3):
#     print(i)
# for i in range(1,21):
#     if i == 13:
#         #continue
#         break
#
#     else:print(i)

###########################################################
# import time
# my_time = int(input("Enter the time in seconds: "))
# for i in range(my_time,0,-1):
#     seconds = i % 60 # % returns the remainder of division
#     minutes = int(i / 60) % 60
#     hours = int(i/ 3600)
#     print(f"{hours:02}:{minutes:02}:{seconds:02}")
#     time.sleep(1)
# print("Time's up")

#nested loop

# rows = int(input("Enter the # of rows: "))
# col = int(input("Enter the # of column: "))
# symbol = input("Enter the symbol to use: ")
# for x in range(rows):
#     for y in range(col):
#         print(symbol,end=" ")
#     print()

# List[]
# set{}
#tuple()
# f = ["apple","banana","grapes","orange"]
# print(dir(f))
# print(f)
# print(34 in f)
# f[0] = "watermelon"
# print(help(f))
# print(type(f))
# f.append("pineapple")
# f.remove("grapes")
# print(f)
# print(f[::-1])
# for x in f:
#     print(x)
# f.insert(0,"lemon")
# print(f)
# f.sort()
# print(f)
# f.reverse()
# print(f)
# print(f.count("apple"))
# f.clear()
# print(f)
# f.pop()
# print(f)
# print(f.index("apple"))

#Shopping cart Program

# foods = []
# prices = []
# total = 0
#
# while True:
#     food = input("Enter a Food to buy (q to quit): ")
#     if food.lower() == "q":
#         break
#     else:
#         price = float(input(f"Enter the price of a {food}: $"))
#         foods.append(food)
#         prices.append(price)
# print("------YOUR CART--------")


#23.2D collection
# groceries = ({"apple","banana","orange","grapes"},
#              {"potato","brocalli","tomato","Peas"},
#              {"fish","chikan","turkey"})
# for collection in groceries:
#     for food in collection:
#         print(food,end=" ")
#     print()

# num_pad = ((1,2,3,)
#            ,(4,5,6),
#            (7,8,9),
#            ("*",0,"#"))
# for row in num_pad:
#     for num in row:
#         print(num,end=" ")
#     print()
#


#####################################################################
#Python Quiz Game

# questions =("How many elements are in periodic table?: ",
#             "Which animal lays the largest eggs?: ",
#             "What is the most abundant gas in Earth's atmosphere?: ",
#             "How many bones are in the human body?: ",
#             "Which planet in the solar system is the hottest?: ")
#
# options = (("A. 116","B. 117","C. 118","D. 119"),
#            ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
#            ("A. Nitrogen","B. Oxygen","C. Carbon-Dioxide","D. hydrogen"),
#            ("A. 206","B. 207","C. 208","D. 209"),
#            ("A. Mercury","B. Venus","C. Earth","D. Mars"))
#
# answers = ("C","D","A","A","B")
# guesses = []
# scores = 0
# question_num = 0
#
# for question in questions:
#     print("------------------------------------")
#     print(question)
#     for option in options[question_num]:
#         print(option)
#
#     guess = input("Enter (A,B,C,D): ").upper()
#     guesses.append(guess)
#     if guess == answers[question_num]:
#         scores += 1
#         print("CORRECT")
#     else:
#         print("INCORRECT")
#         print(f"{answers[question_num]} is the correct answer")
#
#     question_num += 1
# print("---------------------------------------------")
# print("                  RESULT                     ")
# print("---------------------------------------------")
#
# print("answers: ",end=" ")
# for answer in answers:
#     print(answer,end=" ")
# print()
#
# print("guesses: ",end=" ")
# for guess in guesses:
#     print(guess,end=" ")
# print()
#
# score = int(scores / len(questions)*100)
# print(f"Your score is: {score}%")


#Dictionary {key:value}

capitals = {"USA":"Washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}
# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("India"))

# if capitals.get("Russia"):
#     print("the country is exist.")
# else:
#     print("the country is doesn't exist.")

# capitals.update({"Germany":"Berlin"})
# capitals.pop("Russia")
# capitals.popitem()
# print(capitals)

# keys = capitals.keys()
# print(keys)
# print(capitals.values())
#
# for key in capitals.keys():
#     print(key,end=" ")
# print()
# items = capitals.items()
# print(items)


#concession stand program

# menu = {
#     "pizza": 3.00,
#     "nachos":4.50,
#     "popcorn":6.00,
#     "fries":2.50,
#     "chips":1.00,
#     "pretzel":3.50,
#     "soda":3.00,
#     "lemonade":4.25
# }
#
# cart = []
# total = 0
#
# print("------Menu-------")
# for key,value in menu.items():
#     print(f"{key:10}: ${value:.2f}")
# print("-----------------")
#
# while True:
#     food = input("Select an item (q to quit): ").lower()
#     if food == 'q':
#         break
#     elif menu.get(food) is not None:
#         cart.append(food) #add karna
#
# print("------Your Order--------")
# for food in cart:
#     total +=  menu.get(food)
#     print(food,end=" ")
# print()
# print(f"Total is: ${total: .2f}")


# import  random
#
# low = 1
# high = 100
#
# options = ("Rock","Paper","Scissor")
# cards = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
#
# # number = random.randint(low,high)
# # number = random.random()
# # option = random.choice(options)
# random.shuffle(cards)
# print(cards)

#Python number guessing game

# import random
# lowest_num = 1
# highest_num = 100
# answer = random.randint(lowest_num,highest_num)
# guesses = 0
# is_running = True
#
# print("Python Number Guessinng Game")
# print(f"Select a number between {lowest_num} and {highest_num}")
#
# while is_running:  # True
#     guess = input("Enter your guess: ")
#     if guess.isdigit():
#         guess = int(guess)
#         guesses += 1
#
#         if guess < lowest_num or guess >highest_num :
#             print("The number is out of range..")
#             print(f"Please Select a number between {lowest_num} and {highest_num}")
#         elif guess < answer :
#             print("too low! Try again")
#         elif guess > answer :
#             print("too high! Try again")
#         else:
#             print(f"CORRECT! The answer was {answer}")
#             print(f"Number of guesses: {guesses}")
#             is_running = False
#
#     else:
#         print("Invalid Guess..")
#         print(f"plz Select a number between {lowest_num} and {highest_num}")


#rock paper scissor
# import random
#
# options = ("rock","paper","scissor")
# running = True
#
# while running:
#
#     player = None
#     computer = random.choice(options)
#
#     while player not in options:
#         player = input("Enter a choice (rock, paper, scissor): ")
#
#     print(f"Player: {player}")
#     print(f"Computer: {computer}")
#
#     if player == computer:
#         print("it's tie.")
#     elif player == "scissor" and computer == "paper":
#         print("You win!")
#     elif player == "rock" and computer == "scissor":
#         print("You win!")
#     elif player == "paper" and computer == "rock":
#         print("You win!")
#     else:
#         print("You lose!")
#
#     if not input("Play again? (y/n): ").lower() == "y":
#         running = False
#
# print("Thanks for Playing!")


# import random
#
# # print("\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518") # ● ┌ ─ ┐ │ └ ┘
#
# # ● ┌ ─ ┐ │ └ ┘
#
# "┌───────────────┐"
# "│               │"
# "│               │"
# "│               │"
# "│               │"
# "│               │"
# "└───────────────┘"
#
# dice_art = {
#     1: ("┌───────────────┐",
#         "│               │",
#         "│               │",
#         "│       ●       │",
#         "│               │",
#         "│               │",
#         "└───────────────┘"),
#     2: ("┌───────────────┐",
#         "│               │",
#         "│   ●           │",
#         "│               │",
#         "│           ●   │",
#         "│               │",
#         "└───────────────┘"),
#     3: ("┌───────────────┐",
#         "│ ●             │",
#         "│               │",
#         "│       ●       │",
#         "│               │",
#         "│             ● │",
#         "└───────────────┘"),
#     4: ("┌───────────────┐",
#         "│  ●         ●  │",
#         "│               │",
#         "│               │",
#         "│               │",
#         "│  ●         ●  │",
#         "└───────────────┘"),
#     5: ("┌───────────────┐",
#         "│  ●         ●  │",
#         "│               │",
#         "│       ●       │",
#         "│               │",
#         "│  ●         ●  │",
#         "└───────────────┘"),
#     6: ("┌───────────────┐",
#         "│  ●         ●  │",
#         "│               │",
#         "│  ●         ●  │",
#         "│               │",
#         "│  ●         ●  │",
#         "└───────────────┘")
# }
#
# dice = []
# total = 0
# num_of_dict = int(input("How many dice?: "))
#
# for die in range(num_of_dict):
#     dice.append(random.randint(1,6))
#
# # for die in range(num_of_dict):
# #     for line in dice_art.get(dice[die]):
# #         print(line)
#
# for line in range(7):
#     for die in dice:
#         print(dice_art.get(die)[line],end="")
#     print()
# for die in dice:
#     total += die
# print(f"total: {total}")


#functions

#return  = statement used to send a function and
#               send a result back to the caller

# def create_name(first,last):
#     first = first.capitalize()
#     last = last.capitalize() #capitalize is for word first character is capital "K" = kanika = Kanika
#     return first + " " + last
# full_name = create_name("kanika","sharma")
# print(full_name)

#default arguments = A default value parameters
# default is used when the argument is omitted make your
# function more flexible , reduce # for arguments
# 1. positional , 2. Default , 3. keyword, 4.arbitrary

#positional
# def net_price(list_price,discount=0,tax=0.05):
#     return list_price* (1-discount) * (1+tax)
# print(net_price(500))
# print(net_price(500,0.1))
# print(net_price(500,0.1,50))

#default
# import time
#
# def count(start,end): #agar yaha per me "start=0" likh du
#     # start ki jagah per or fuction call me start hata du
#     # to error through ksrega or agar start=0 ko end se swipe
#     # kr du to nhi karega
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done")
#
# count(0,10)

#
# import time
#
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("Done")
#
# count(30,20)

#KEYWARD Arguments

# def hello(greeting,title,first,last):
#     print(f"{greeting} {title} {first} {last}")
# hello("Hi!","Kanika","Sharma","Miss")
# hello(greeting="Hi!",first="Kanika",last="Sharma",title="Miss")
#
# print("1","2","3",sep="-")

#*args  = allows you to pass multiple non-key argments
#**kwargs = allowa you to pass multiple keyword- arguments
#           * unpacking operator
#           # 1. positional , 2. Default , 3. keyword, 4.arbitrary

# def add(*args):
#     total = 0
#     for arg in args:
#         total += arg
#     return total
# print(add(1,2,3,4))
#
# def dis_name(*args):
#     for arg in args:
#         print(arg,end=" ")
#
# dis_name("k","a","n","i","k","a")

def print_address(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
print_address(street="123 Fake Sr.",
              apartmentno="12345",
              city = "indore",
              state = "MP",
              zip = "1234")

# def shipping_label(*args,**kwargs):
#     for arg in args :
#         print(arg,end=" ")
#     print()
#     # for value in kwargs.values():
#     #     print(value,end=" ")
#     #     print()
#     print(f"{kwargs.get('street')} ,{kwargs.get('city')}")
#
# shipping_label("Miss","Kanika","Sharma",
#                street="123 Fake Sr.",
#                apartmentno="12345",
#                city="indore",
#                state="MP",
#                zip="1234")

#Iterables = object/collection that can return its elements
#             one at atime,allowing it to be iterated in a loop

# number = [1,2,3,4,5]
# number = (1,2,3,4,5)
# for num in reversed(number):
#     print(num,end=" - ")

# name = "Bro Code"
#
# for character in name:
#     print(character,end=" ")
# print()
#
# my_dict = {"A":1,"B":2,"C":3}
# for key,value in my_dict.items():
#     print(f"{key} = {value}")

#Membership operators = used to test whether a value or variable is found in a sequence
#                        (string,list,tuple,set,or dictionry)
#                        1. in
#                        2. not in
# word = "APPLE".lower()
# letter = input("Guess a letter in the secret word: ").upper()
# if letter in word:
#     print(f"There is {letter}")
# else:
#     print(f"{letter} is not found.")

# students = {"Kanika","Kabu","kuku"}
# student = input("Enter the name of a student: ")
#
# if student not in students:
#     print(f"{student} was not found")
# else:
#     print(f"{student} is a student")

# items = {"Kanika":"C",
#           "Ayushi":"B",
#           "Aditi":"A",
#           "Vedika":"D"}
# keys = input("Enter the name of student: ")
# if keys in items:
#     print(f"{keys}'s grade is {items[keys]}")
# else:
#     print(f"{keys} was not found.")

# email = "kanika200522@gmail.com"
# if "@"  in email and "." in email:
#     print("Valid email")
# else:
#     print("invalid email")

#list comprehension = A concise way to create lists in Python
# Compact and easier to read traditional loops
# [expression for value in iterable if condition]

# for i in range(2,22,2):
#     print(i)

# n =2
# for i in range(1,11):
#     print(f"{n}x{i}={n*i}")

# double = []
# for i in range(1,11):
#     double.append(i*2)
# print(double)

# double = [x*2 for x in range(1,11)] # 2 ka table
# triple = [x*3 for x in range(1,11)] # 3 ka table
# square = [z*z for z in range(1,11)] # side*side
# print(double)
# print(triple)
# print(square)
#
# fruits = [fruit.upper() for fruit in ["apple","banana","orange","grapes"]]
# print(fruits)

# number = [1,-2,3,-4,5,6,8,9,10]
# positive_num = [num for num in number if num >= 0]
# negative_num = [num for num in number if num < 0]
# even_num = [num for num in number if num % 2 == 0]
# odd_num = [num for num in number if num % 2 == 1]
#
# print(odd_num)
#
# grades = [98,40,84,38,65,45]
# passing_grade = [grade for  grade in grades if grade >= 60 ]
# print(passing_grade)


## Match case statement : (Switch) : An alternative to using many 'elif' statement
##                                  Execute some code if a value matches a 'case' .
##                                  "Benefits: cleaner syntax is more readable
# def day_of_week(day):
#     if day == 1:
#         return "Its Sunday".upper()
#     elif day == 2:
#         return "Its Monday".upper()
#     elif day == 3:
#         return "Its Tuesday".upper()
#     elif day == 4:
#         return "Its Wednesday".upper()
#     elif day == 5:
#         return "Its Thursday".upper()
#     elif day == 6:
#         return "Its Friday".upper()
#     elif day == 7:
#         return "its Saturday".upper()
#     else:
#         return "Its not Valid..".upper()
#
# day = int(input("Enter day (1-7): "))
# print(f"Today day:  {day_of_week(day)}")
#
# #Now use match case
# def day_of_week(day):
#     match day:
#         case 1:
#             return "sunday".upper()
#         case 2:
#             return "monday".upper()
#         case 3:
#             return "tuesday".upper()
#         case 4:
#             return "wednesday".upper()
#         case 5:
#             return "thursday".upper()
#         case 6:
#             return "friday".upper()
#         case 7:
#             return "staturday".upper()
#         case _:
#             return "not valid".upper()
#
# day = int(input("Enter day (1-7):"))
# print(f"Today day: {day_of_week(day)}")


# def Food(eat):
#     match eat:
#         case "fruits" | "vegetables":
#             return "you eat healthy food."
#         case "Samosa" | "Pizza":
#             return "you eat junk food."
#         case "Fish" | "Chicken":
#             return "you eat non veg."
#         case _:
#             return "not valid"
#
#
# eat = input("What you eat today? ")
# print(f"Today : {Food(eat)}")


#module: a file containing code you want to include in your program
# use 'import' to include a module (built-in or your own) useful to
# break up a large program reusable separate files

# print(help("math"))

# import math
# import math as m
# from math import pi
# from math import e
# a,b,c,d,e = 1,2,3,4,5
# print(math.e**a)
# print(math.e**b)
# print(math.e**c)
# print(math.e**d)
# print(math.e**e)
# print(f"{math.pi}")

## import boto3
##
## s3 = boto3.client('s3')
## for bucket in s3.list_buckets()['Buckets']:
##     print(bucket['Name'])

# import example
# result = example.pi
# x = 5
# radius = 5
# result1 = example.square(x)
# result2 = example.cube(x)
# result3 = example.area(radius)
# result4 = example.circumference(radius)
# print(result1)
# print(result2)
# print(result3)
# print(result4)

#-----------main.py-------------
#module = a file containing code your want to include to your program use
# 'import' to include a module (built-in your own) useful to break up a
# large program reusable separate files

# print(help("modules"))

###############################################################
#variable scope = where a variable is visible and accesible
#scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in
###############################################################
# Variable Scope in Programming (Simple Explanation)
#
# Scope means where a variable can be accessed or used in a program.
#
# ✅ Types of Variable Scope
# 1. Local Scope
#
# Variable declared inside a function/block
# Can be used only inside that function/block
# Not accessible outside
# Example (Python):
# def fun():
#     x = 10   # local variable
#     print(x)
#
# fun()
# print(x)  # error: x not defined

# Global Scope
# Variable declared outside any function
# Can be used anywhere in the file
# Example:
# x = 50   # global variable
#
# def fun():
#     print(x)
#
# fun()
# print(x)

# 3. Block Scope (mainly in C, C++, Java)
# Variables declared inside if, for, while block
# Only available inside that block
# Example:
## if (true) {
##     int x = 10;
##     System.out.println(x);
## }
##System.out.println(x);  // error

# 4. Function Scope
# Variables declared inside a function
#Exist only while the function runs

# 5. Class/Object Scope (OOP Languages like Java/C++)
# Variables inside a class
# Accessible using object or class name
# Example:
# class A :
#     x = 10 # class variable

###########################################################
# def func1():
#     a = 1
#     print(a)
# def func2():
#     b=2
#     print(b)
# func2()
# func1()

# from example import *
# print(dir())
# print(__name__)
# def favourite_food(food):
#     print(f"Your favorite food is {food}")
# def main():
#     print("This is script")
#     favourite_food("Noodles")
#     print("Goodbye!!")
# if __name__ == '__main__': #dandar
#     main()

#Python Banking Program
#
# def show_balance(balance):
#     print("***************************")
#     print(f"Your balance is ${balance:.2f}")
#     print("***************************")
#
# def deposit():
#     print("***************************")
#     amount = float(input("Enter an amount deposited: "))
#     print("***************************")
#     if amount < 0:
#         print("This amount is not valid")
#         return 0
#     else:
#         return amount
#
# def withdraw(balance):
#     print("***************************")
#     amount = float(input("Enter an amount withdraw: "))
#     print("***************************")
#     if amount>balance:
#         print("***************************")
#         print("This is amount is not valid.")
#         print("***************************")
#     elif amount < 0:
#         print("***************************")
#         print("Amount must be greater than 0")
#         print("***************************")
#         return 0
#     else:
#         return amount
#
# def main():
#     balance = 0
#     is_running = True
#
#     while is_running:
#         print("***************************")
#         print("      Banking Program      ")
#         print("***************************")
#         print("Show Balance")
#         print("Deposit")
#         print("WithDraw")
#         print("Exit")
#         print("***************************")
#         choice = input("Enter Your Choice (1-4) : ")
#
#         if choice == '1':
#             show_balance(balance)
#         elif choice == '2':
#             balance += deposit()
#         elif choice == '3':
#             balance -=withdraw(balance)
#         elif choice == '4':
#             is_running = False
#         else:
#             print("***************************")
#             print("This choice is not valid..")
#             print("***************************")
#
#     print("***************************")
#     print("Thank you ! have a nice day.")
#     print("***************************")
# if __name__ == '__main__':
#     main()

##Python Slot Machine
#
# def spin_row():
#     Symbols= ['🍒' ,'🍉', '🍋', '🔔','⭐']
#     # result = []
#     # for symbol in range(3):
#     #     result.append(random.choice(Symbols))
#     # return result
#     return [random.choice(Symbols) for _ in range(3)]
# def print_row(row):
#     print("***************")
#     print(" | ".join(row))
#     print("***************")
# def get_payout(row,bet):
#     if row[0] == row[1] == row[2]:
#         if row[0] == '🍒':
#             return bet*3
#         elif row[0] == '🍉':
#             return bet*4
#         elif row[0] == '🍋':
#             return bet*5
#         elif row[0] == '🔔':
#             return bet*10
#         elif row[0] == '⭐':
#             return bet*20
#     return 0
#
# def main():
#     balance = 100
#
#     print("************"
#           "************************")
#     print("       Welcome to Python Slot       ")
#     print("Symbol: 🍒 🍉 🍋 🔔 ⭐")
#     print("************************************")
#
#     while balance > 0:
#         print(f"Current Balance : {balance}")
#
#         bet = input("Place your bet amount: ")
#         if not bet.isdigit():
#             print("Please Enter a Valid Number.")
#             continue
#         bet = int(bet)
#
#         if bet>balance:
#             print("Insufficient Amount")
#             continue
#         if bet <= 0:
#             print("Bet must be greater than 0.")
#             continue
#
#         balance -= bet
#
#         row = spin_row()
#         print(row)
#         print("Spinning....\n")
#         print_row(row)
#
#         payout= get_payout(row,bet)
#         if payout > 0:
#             print(f"You won ${payout}")
#         else:
#             print("You lost this Game.")
#         balance += payout
#
#         play_again = input("Do you want to spin again? (Y/N): ")
#
#         if play_again != "Y".lower():
#             break
#     print("********************************************")
#     print(f"Game Over! YOur final balance is ${balance}")
#     print("********************************************")
#
#
# if __name__ == '__main__':
#     main()


#encrytion program
# import random
# import string
#
# chars = " "+string.punctuation + string.digits + string.ascii_letters
# chars = list(chars)
# key = chars.copy()
#
# random.shuffle(key)
# # print(f"chars: {chars}")
# # print(f"key  : {key}")
#
# #encrypt
# plain_text = input("Enter a message to encrypt: ")
# cipher_text = ""
#
# for letter in plain_text:
#     index = chars.index(letter)
#     cipher_text += key[index]
#
# print(f"Original Message: {plain_text}")
# print(f"Encrypted Message: {cipher_text}")
#
# #Decryption
# cipher_text = input("Enter a message to ecrytion: ")
# plain_text = ""
# for letter in cipher_text:
#     index = key.index(letter)
#     plain_text += chars[index]
#
# print(f"Encrypted Message: {cipher_text}")
# print(f"Original Message: {plain_text}")


#HANGMAN IN PYTHON
# import random
# from example import word
#
# # word = ("apple","orange","grapes","watermelon","strawberry")
# # iski jagah per example.py me 100 words h
# #dictionary of key():
# hangman_art = {0:("   ",
#                   "   ",
#                   "   "),
#                1:(" o ",
#                   "   ",
#                   "   "),
#                2:(" o ",
#                   " | ",
#                   "   "),
#                3:(" o ",
#                   "/| ",
#                   "   "),
#                4:(" o ",
#                   "/|\\",
#                   "   "),
#                5:(" o ",
#                   "/|\\",
#                   "/  "),
#                6:(" o ",
#                   "/|\\",
#                   "/ \\")}
#
# def display_man(wrong_guesses):
#     print("******************")
#     for line in hangman_art[wrong_guesses]:
#         print(line)
#     print("******************")
# def display_hint(hint):
#     print(" ".join(hint))
# def display_answer(answer):
#     print(" ".join(answer))
# def main():
#     answer = random.choice(word)
#     hint = ["_"]*len(answer)
#     wrong_guesses = 0
#     guessed_letters = set()
#     is_running = True
#
#     while is_running:
#         display_man(wrong_guesses)
#         display_hint(hint)
#         guess = input("Enter a letter: ").lower()
#
#         if len(guess) != 1 or not guess.isalpha():
#             print("Invalid Input.")
#             continue
#
#         if guess in guessed_letters:
#             print(f"{guess} is already guessed.")
#             continue
#
#         guessed_letters.add(guess)
#
#         if guess in answer:
#             for i in range(len(answer)):
#                 if answer[i] == guess:
#                     hint[i] = guess
#         else:
#             wrong_guesses += 1
#
#         if "_" not in hint:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You win!")
#             is_running = False
#         elif wrong_guesses >= len(hangman_art)-1:
#             display_man(wrong_guesses)
#             display_answer(answer)
#             print("You lose!")
#             is_running = False
#
#
# if __name__ == '__main__':
#     main()

#object and class
#python object oriented Programming language

#object = A "bundle" of related attributes (variables) and methods (functions)
#         Ex. phone, cup,book
#         You need a "class" to create many objects

#class = (blueprint) used to design the structure and layout of the objects
#
# class Car:
#     def __init__(self,model,year,color,for_sale):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
# car1 = Car("BMW",2025,"Blue",False)
# print(car1.model)
# print(car1.color)
# print(car1.for_sale)


#class variable
# class Student:
#     class_year = 2028
#     num_student = 0
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.num_student += 1
#
# student1 = Student("Kanika",20)
# student2 = Student("Kartik",14)
#
# print(f"My graduation class of {Student.class_year} has {Student.num_student} students")
# print(student1.name)
# print(student1.age)

# Inheritance = Allows a class to inherit attributes and methods from  another class
# Helps with code reusability and extensibility
# class Child(Parent)
#
# class Animal:
#     def __init__(self,name):
#         self.name = name
#         self.is_alive = True
#     def eat(self):
#         print(f"{self.name} is eating...")
#     def sleep(self):
#         print(f"{self.name} is sleepin...")
# class Dog(Animal):
#     def speak(self):
#         print("Woof..")
# class Cat(Animal):
#     def speak(self):
#         print("Meow..")
# class Mouse(Animal):
#     def speak(self):
#         print("Squeek..")
#
# dog = Dog("Scooby")
# cat = Cat("Tom")
# mouse = Mouse("Jerry")
#
# print(cat.name)
# print(cat.is_alive)
# cat.eat()
# cat.sleep()
# cat.speak()


# class Employee:
#     def __init__(self,salary):
#         self.salary = salary
#         self.balance = 0
#     def show_salary(self):
#         print(f" My Salary is: {self.salary}")
#     def deposit(self,amount):
#         self.balance += amount
#         print(f"{amount} deposited.Current Balance {self.balance}")
#     def withdraw(self,amount):
#         if amount > self.balance:
#             print("Insufficient Amount.")
#         else:
#             self.balance -= amount
#             print(f"{amount} withdraw.Current Balance {self.balance}")
#
# salary = int(input("Enter the your salary: "))
# emp = Employee(salary)
#
# emp.show_salary()
#
# dep = int(input("Enter the deposited amount: "))
# emp.deposit(dep)
#
# wd = int(input("Enter the withdraw amount: "))
# emp.withdraw(wd)


#Multiple and Multilevel Inheritance
# class Animal:
#     def __init__(self,name):
#         self.name = name
#
#     def eat(self):
#         print(f"{self.name} is eating")
#
#     def sleep(self):
#         print(f"{self.name} is sleeping")
#
# class Prey(Animal):
#     def flee(self):
#         print(f"{self.name} is hunting")
#
# class Predator(Animal):
#     def hunt(self):
#         print(f"{self.name} is hunting")
#
# class Rabbit(Prey):
#     pass
# class Hawk(Predator):
#     pass
# class Fish(Prey,Predator):
#     pass
# rabbit = Rabbit("Bugs")
# hawk = Hawk("Tony")
# fish = Fish("Nemo")
# rabbit.eat()
# rabbit.sleep()

#super() class
# import math
# class Shape:
#     def __init__(self,color,is_filled):
#         self.color = color
#         self.is_filled = is_filled
#
#     def describe(self):
#         print(f"This is {self.color} and {'filled' if self.is_filled else 'not found'}")
#
# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius = radius
#
#     def describe(self):
#         print(f"It is a circle with an area of {3.14 * self.radius * self.radius}")
#         super().describe()
#
# class Square(Shape):
#     def __init__(self,color,is_filled,width):
#         super().__init__(color,is_filled)
#         self.width = width
#
#     def describe(self):
#         print(f"It is a square with an area of {self.width * self.width}")
#         super().describe()
#
# class Triangle(Shape):
#     def __init__(self,color,is_filled,width,height):
#         super().__init__(color,is_filled)
#         self.width = width
#         self.height = height
#
#     def describe(self):
#         print(f"It is a circle with an area of {self.width * self.height / 2}")
#         super().describe()
#
#
# circle = Circle("Red",True,2)
# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)
# circle.describe()
#
# square = Square("Blue",False,5)
# print(square.color)
# print(square.is_filled)
# print(square.width)
# square.describe()
#
# triangle = Triangle("Pink",True,2,4)
# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)
# triangle.describe()


#Polymorphism
#Poly = Many
#Morphe = Form
#Two way to achieve polymorphism
#1. Inheritance = An object could be treated of the same type as a parent class
#2. Duck Typing = Object must have necessary attributes/ methods

#1. Inheritance
# from  abc import ABC ,abstractmethod
# class Shape(ABC):
#
#     @abstractmethod # #Ye Rule banata hai ki child class me ye method jarur banana padega
# # # Agar parent class me abstract method hai,
# # # to usko inherit karne wali har child class ko us method ka apna version banana hi padega.
#     def area(self):
#         pass
#
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius = radius
#
#     def area(self):
#         return self.radius ** 2
#
# class Rectangle(Shape):
#     def __init__(self, length, breadth):
#         self.length = length
#         self.breadth = breadth
#
#     def area(self):
#         return self.length * self.breadth
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def area(self):
#         return self.side * self.side
#
# class Pizza(Circle):
#     def __init__(self, topping,radius):
#         super().__init__(radius)
#         self.topping = topping
#
# shapes = [Circle(4), Rectangle(3,4), Square(3),Pizza("Paneer",4)]
# for shape in shapes:
#     print(shape.area())


#2. Duck Typing = Another way to achieve polymorphism besides inheritance
#                 Object must have the minimum necessary attributes/methods
#                 "If it looks like a duck and quacks like a duck, it must be a duck"

# Duck method me sirf methods or properties se mtlb
# hota hai use baaki object se koi mtlb nhi or class
# se bhi koi mtb nhi h

# class Animal:
#     alive  = True
# class Dog(Animal):
#     def speak(self):
#         print("Woof!")
# class Cat(Animal):
#     def speak(self):
#         print("Meow!")
# class Car:
#     def speak(self):
#         print("Honk!")
#     alive = False
#
# animals = [Dog(),Cat(),Car()]
# for animal in animals:
#     animal.speak()
#     print(animal.alive)


#Static method that belongs to class rather than object
# from the class (instances) usually used for general utility functions

#Instance methods(object) = Best for operations on instances of the clas (objects)
# Static methods(self nhi hota h) = Best for utility functions that do not need access to class data
# class Employee:
#     def __init__(self,name,position):
#         self.name = name
#         self.position = position
#
#     def get_info(self):
#         return f"{self.name} = {self.position}"
#
#     @staticmethod #No self use
#     def is_valid_position(position):
#         valid_positions = ["Manager","Cashier","janitor","Cook"]
#         return position in valid_positions
#
# employee1  = Employee("Eugune","Manager")
# employee2 = Employee("Squidward","Cashier")
# employee3 = Employee("Spongbob","Cook")
# print(Employee.is_valid_position("Manager"))
# print(employee1.get_info())
# print(employee2.get_info())
# print(employee3.get_info())


# Instance method → object ka data chahiye → self
# Class method → class ka data chahiye → cls
# Static method → Dono ka data nahi chahiye → simple helper function

#Class Method = Allows operation related to the class itself
#              Take (cls) as the first parameter, which represents the class itself.

# class Student:
#     count = 0
#     total_gpa = 0
#
#     def __init__(self,name,gpa):
#         self.name = name
#         self.gpa = gpa
#
#         Student.count += 1
#         Student.total_gpa += gpa
#
#     #Instance Method
#     def get_info(self):
#         return f"{self.name} {self.gpa}"
#
#     @classmethod
#     def get_count(cls):
#         return f"Total # of Students: {cls.count}"
#
#     @classmethod
#     def get_average_gpa(cls):
#         if cls.count == 0:
#             return 0
#         else:
#             return f"{cls.total_gpa / cls.count:.2f}"
#
# student1  = Student("Spongbob",3.2)
# student2  = Student("Patrick",2.0)
# student3  = Student("Zig",4.0)
#
# print(Student.get_count())
# print(Student.get_average_gpa())


#Magic methods (jinhe dunder methods bhi kaha jata hai)
# Python ke special methods hote hain जिनके नाम double
# underscore se start aur end hote हैं:

# Example:
# __init__, __str__, __len__, __add__, etc

#They are automatically called by many of Python's built-in operations they alow de

# class Book:
#     def __init__(self,title,author,num_page):
#         self.title = title
#         self.author = author
#         self.num_page = num_page
#     def __str__(self): #string
#         return f"'{self.title}' by {self.author}"
#
#     def __eq__(self, other): # equal
#         return self.title == other.title and self.author == other.author
#
#     def __lt__(self, other): #less than
#         return self.num_page < other.num_page
#
#     def __gt__(self, other): #greater than
#         return self.num_page > other.num_page
#
#     def __add__(self, other): #addition
#         return f"{self.num_page + other.num_page} pages.."
#
#     def __contains__(self, keywords):
#         return keywords in self.title or keywords in self.author
#
#     def __getitem__(self, key):
#         if key == 'title':
#             return self.title
#         elif key == 'author':
#             return self.author
#         elif key == 'num_page':
#             return self.num_page
#         else:
#             return f"key {key} was not found"
#
# book1 = Book("The Habbit","J.R.R Tolkien",310)
# book2 = Book("The Habbit","J.R.R Tolkien",310)
# book3 = Book("My Love Pakhi","Arnav Singh Rawat",216)
#
#
# print(book1)
# print(book1 == book2)
# print(book1 < book3)
# print(book1 > book3)
# print(book1 + book3)
# print("Arnav Singh Rawat" in book3)
# print(book1['title'])
# print(book1['author'])
# print(book1['num_page'])
# print(book2['parrot'])


#@property = Decorator used to define as a property (it can be accessed like an attributes )
#            Benefits: Add additional logic when read , write , or delete attributes
#            Gives you getter, setter and deleter method

# class Rectangle:
#     def __init__(self,width,height):
#         self._width = width
#         self._height = height
#
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
#
#     @property
#     def height(self):
#         return f"{self._height:.1f}cm"
#
#     @width.setter
#     def width(self,new_width):
#         if new_width > 0:
#             self._width = new_width
#         else:
#             print("Width must be greater than 0")
#
#     @height.setter
#     def height(self, new_height):
#         if new_height > 0:
#             self._height = new_height
#         else:
#             print("Height must be greater than 0")
#
#     @width.deleter
#     def width(self):
#         del self._width
#         print("Width has been deleted..")
#
#     @height.deleter
#     def height(self):
#         del self._height
#         print("Height has been deleted..")
#
# rectangle1 = Rectangle(2,3)
#
# rectangle1.width = 5
# rectangle1.height = 6
#
# del rectangle1.width
# del rectangle1.height
#
# # print(rectangle1.width)
# # print(rectangle1.height)

#Decorator A function that extends the behavior of another function w/o modifying the base function
#Pass the base function as an argument to the decorator.
#@add_sprinkles
#get_ice_cream("vanilla")

######******* Window+; *******######

# def add_sprinkles(func):
#     def wrapper(*args,**kwargs):
#         print("You add sprinkles🎊")
#         func(*args,**kwargs)
#     return wrapper
# def add_fudge(func):
#     def wrapper(*args,**kwargs):
#         print("You add fudge 🍟")
#         func(*args,**kwargs)
#     return wrapper
# def add_food(func):
#     def wrapper(*args,**kwargs):
#         print("You add food 🍔")
#         func(*args,**kwargs)
#     return wrapper
#
# @add_sprinkles
# @add_fudge
# @add_food
# def get_ice_cream(flavor):
#     print(f"Here is {flavor} of your ice cream 🍦")
#
# get_ice_cream("vanilla")

# exception = An event that interrupts the flow of program
#             (ZeroDivisionError, TypeError, ValueError)
#             1.try, 2. except 3.finally

#type casting
# 1 + int('1')

# try:
#     #try some code
# except Exception:
#     #Handle an Exception
# finally:
#     # Do some clean up
# try:
#     number = int(input("Enter a number: "))
#     print(1/number)
# except ZeroDivisionError:
#     print("You can't divide by zero IDIOT.")
# except ValueError:
#     print("Enter only numbers please.")
# except Exception:
#     print("Something went wrong!")
# finally:
#     print("Do some cleanup here 😋")
#

# #python file detection
# import os
# file_path = "C:/Users/dell/OneDrive/Desktop/kaniika"
# # file_path = "C:/Users/dell/OneDrive/Desktop/kanika.txt"
#
# if os.path.exists(file_path):
#     print(f"The location '{file_path}' exists.")
#     if os.path.isfile(file_path):
#         print("This is a file")
#     elif os.path.isdir(file_path):
#         print("This is a directory")
# else:
#     print("That location doesn't exist..")


# # Python writing files (.txt, .json, .csv)
#
# # txt file
# txt_data = "I like pizza!"
#
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.txt"
# try:
#     with open(file_path,"a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That file is already exist.")


# employees = ["BTS","Stray Kids","BlackPink","TXT","Enyphen"]
#
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.txt"
# try:
#     with open(file_path,"w") as file:
#         for employee in employees:
#             file.write(employee + " ")
#         print(f"txt file '{file_path} was created")
# except FileExistsError:
#     print("That file is already exist.")

# #json file
# import json
# employee= {
#     "Name": "Kanika Sharma",
#     "Age" : 20,
#     "Status" : "Student"
# }
#
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.json"
# try:
#     with open(file_path,"w") as file:
#         json.dump(employee,file,indent=4)
#         print(f"json file '{file_path} was created")
# except FileExistsError:
#     print("That file is already exist.")

# import csv
#
# employee = [["Name","Age","Status"],
#             ["Kanika",20,"Student"],
#             ["Aditi",19,"Student"],
#             ["Ayushi",20,"Student"]]
#
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.csv"
# try:
#     with open(file_path,"w",newline="") as file:
#         writer = csv.writer(file)
#         for row in employee:
#             writer.writerow(row)
#         print(f"csv file '{file_path} was created")
# except FileExistsError:
#     print("That file is already exist.")


# Python reading files (.txt, .json, .csv )

#txt file
# file_path = "C:/Users/dell/OneDrive/Desktop/kaniika"
# try:
#     with open(file_path, "r") as file :
#         content = file.read()
#         print(content)
# except FileExistsError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that files")


# import json
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.json"
# try:
#     with open(file_path, "r") as file :
#         content = json.load(file)
#         print(content)
#         print(content["Name"])
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that files")

#
# import csv
# file_path = "C:/Users/dell/OneDrive/Desktop/sample1.csv"
# try:
#     with open(file_path, "r") as file :
#         content = csv.reader(file)
#         for line in content:
#             print(line)
#             # print(line[0])
#
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to read that files")
#

# import datetime
#
# date = datetime.date(2025,1,2)
# # print(date)
# today = datetime.date.today()
# print(today)
#
# time = datetime.time(12,30,0)
# print(time)
# now = datetime.datetime.now()
# print(now)
# now = now.strftime("%H:%M:%S [%m-%d-%Y]")
# print(now)
#
# target_datetime = datetime.datetime(2030,1,2,12,30,1)
# current_datetime= datetime.datetime.now()
#
# if target_datetime < current_datetime:
#     print("Target data has passed")
# else:
#     print("Target data has not passed")

#Python Alarm Clock
# import time
# import datetime
# import pygame
#
# def set_alarm(alarm_time):
#     print(f"Alarm set for {alarm_time}")
#     sound_file = "C:/Users/dell/Downloads/wake_up.mp3"
#     is_running = True
#
#     while is_running:
#         current_time  = datetime.datetime.now().strftime("%H:%M:%S")
#         print(current_time)
#         if current_time == alarm_time:
#             print("Wake up! ..")
#
#             pygame.mixer.init()
#             pygame.mixer.music.load(sound_file)
#             pygame.mixer.music.play()
#
#             while pygame.mixer.music.get_busy():
#                 time.sleep(1)
#
#             is_running = False
#
#         time.sleep(1)
# if __name__ == '__main__':
#     alarm_time = input("Enter the alarm time (HH:MM:SS): ")
#     set_alarm(alarm_time)


#multithreading :=> Used to perform tasks concurrently (multitasking)
#Good for I/O bound tasks like reading files or fetching data from APIs
#threading .Thread (target=my_function)

# import threading
# import time
#
# def dog_walk(firstname,lastname):
#     time.sleep(6)
#     print(f"You finish walking {firstname} {lastname}")
# def take_out_trash():
#     time.sleep(2)
#     print("You take out the trash..")
# def get_mail():
#     time.sleep(4)
#     print("You get the mail..")
#
# chore1 = threading.Thread(target=dog_walk, args=("Scooby","Doo"))
# chore1.start()
# chore2 = threading.Thread(target=take_out_trash)
# chore2.start()
# chore3 = threading.Thread(target=get_mail)
# chore3.start()
#
# chore1.join()
# chore2.join()
# chore3.join()
#
# print("All chores are complete!")

###########  How to connect to an API using Python  #################
# import requests
#
# base_url = "https://pokeapi.co/api/v2/"
#
# def get_pokemon_info(name):
#     url= f"{base_url}/pokemon/{name}"
#     response = requests.get(url)
#     print(response)
#
#     if response.status_code == 200:
#         pokemon_data = response.json()
#         return pokemon_data
#     else:
#         print(f"Failed to retrieve data {response.status_code}")
#
#
# pokemon_name = "pikachu"
# pokemon_info = get_pokemon_info(pokemon_name)
#
# if pokemon_info:
#     print(f"Name: {pokemon_info["name"].capitalize()}")
#     print(f"Id: {pokemon_info["id"]}")
#     print(f"Height: {pokemon_info["height"]}")
#     print(f"Weight: {pokemon_info["weight"]}")

# PyQt5 Introduction
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
# from PyQt5.QtGui import QIcon
# from PyQt5.QtGui import QFont
# from PyQt5.QtCore import Qt
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("My First GUI")
#         self.setGeometry(550,250,300,300)
#         self.setWindowIcon(QIcon("C:/Users/dell/Downloads/cat.png"))
#
#         label = QLabel("Hello Kitty!",self)
#         label.setFont(QFont("Arial",30))
#         label.setGeometry(0,0,500,100)
#         label.setStyleSheet("color:#bd4abb;"
#                             "background-color: #4abab8;"
#                             "font-weight : bold;"
#                             "font-style: italic;"
#                             "font-decoration: underline;")
#         # label.setAlignment(Qt.AlignTop) #Vertical Top
#         # label.setAlignment(Qt.AlignBottom) #Vertical Bottom
#         # label.setAlignment(Qt.AlignVCenter) #Vertical Center
#         #
#         # label.setAlignment(Qt.AlignRight) # Horizontal Right
#         # label.setAlignment(Qt.AlignHCenter) # Horizontal Center
#         # label.setAlignment(Qt.AlignLeft) # Horizontal Left
#         #
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # Center & Top
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # Center & Bottom
#         # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # Center & Center
#
#         # label.setAlignment(Qt.AlignCenter) # Center & Center
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
# if __name__ == "__main__":
#     main()


# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow , QLabel
# from PyQt5.QtGui import QPixmap
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700,300,500,500)
#
#         label = QLabel(self)
#         label.setGeometry(0,0,250,250)
#
#         pixmap = QPixmap("C:/Users/dell/Downloads/cloud.png")
#         label.setPixmap(pixmap)
#         label.setScaledContents(True)
#         label.setGeometry((self.width()-label.width()) // 2,
#                           self.height()-label.height() // 2,
#                           label.width(),
#                           label.height())
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
# if __name__ == "__main__":
#     main()


# PyQt5 layouts
# import sys
# from PyQt5.QtWidgets import (QApplication, QMainWindow, QLabel,
#                              QWidget, QVBoxLayout, QVBoxLayout, QGridLayout, QHBoxLayout)
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700,300,500,500)
#         self.initUI()
#
#     def initUI(self):
#         central_widget = QWidget()
#         self.setCentralWidget(central_widget)
#
#         label1 = QLabel("#1", self)
#         label2 = QLabel("#2", self)
#         label3 = QLabel("#3", self)
#         label4 = QLabel("#4", self)
#         label5 = QLabel("#5", self)
#
#         label1.setStyleSheet("background-color: red;")
#         label2.setStyleSheet("background-color: yellow;")
#         label3.setStyleSheet("background-color: green;")
#         label4.setStyleSheet("background-color: purple;")
#         label5.setStyleSheet("background-color: blue;")
#
#         # vbox = QVBoxLayout()
#         #
#         # vbox.addWidget(label1)
#         # vbox.addWidget(label2)
#         # vbox.addWidget(label3)
#         # vbox.addWidget(label4)
#         # vbox.addWidget(label5)
#         #
#         # central_widget.setLayout(vbox)
#         # hbox = QHBoxLayout()
#         #
#         # hbox.addWidget(label1)
#         # hbox.addWidget(label2)
#         # hbox.addWidget(label3)
#         # hbox.addWidget(label4)
#         # hbox.addWidget(label5)
#         #
#         # central_widget.setLayout(hbox)
#
#         grid = QGridLayout()
#
#         grid.addWidget(label1,0,0)
#         grid.addWidget(label2,0,1)
#         grid.addWidget(label3,1,0)
#         grid.addWidget(label4,1,1)
#         grid.addWidget(label5,2,2)
#
#         central_widget.setLayout(grid)
#
#
# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())
# if __name__ == "__main__":
#     main()

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QCheckBox

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700,300,500,500)
#         self.button = QPushButton("Click Me!",self)
#         self.label= QLabel("Hello",self)
#         self.initUI()
#
#     def initUI(self):
#         self.button.setGeometry(150,200,200,100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)
#
#
#     def on_click(self):
#         print("Button clicked!")
#         self.button.setText("Clicked!")
#         self.button.setDisabled(True)
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700, 300, 500, 500)
#         self.button = QPushButton("Click Me!", self)
#         self.label = QLabel("Hello", self)
#         self.initUI()
#
#     def initUI(self):
#         self.button.setGeometry(150, 200, 200, 100)
#         self.button.setStyleSheet("font-size: 30px;")
#         self.button.clicked.connect(self.on_click)
#
#         self.label.setGeometry(150,300,200,100)
#         self.label.setStyleSheet("font-size: 50px")
#
#     def on_click(self):
#         self.label.setText("Goodbye")
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

# # PyQt5 CheckBoxes
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QCheckBox
# from PyQt5.QtCore import Qt

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700,300,500,500)
#         self.checkbox = QCheckBox("Do you like food?",self)
#         self.initUI()
#
#     def initUI(self):
#         self.checkbox.setGeometry(10,0,500,100)
#         self.checkbox.setStyleSheet("font-size: 30px;"
#                                     "font-family: Arial;")
#         self.checkbox.setChecked(False)
#         self.checkbox.stateChanged.connect(self.checkbox_changed)
#
#
#     def checkbox_changed(self,state):
#         if state == Qt.Checked:
#            print("You like food! ")
#         else:
#             print("You don't like food")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

#
# # PyQt5 Radio Buttons
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton , QButtonGroup
# from PyQt5.QtCore import Qt
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(700,300,500,500)
#         self.radio1 = QRadioButton("Visa",self)
#         self.radio2 = QRadioButton("Mastercard",self)
#         self.radio3 = QRadioButton("Gift Card",self)
#         self.radio4 = QRadioButton("In-Store", self)
#         self.radio5 = QRadioButton("Online",self)
#         self.button_group1 = QButtonGroup(self)
#         self.button_group2 = QButtonGroup(self)
#
#         self.initUI()
#
#     def initUI(self):
#         self.radio1.setGeometry(0,0,300,50)
#         self.radio2.setGeometry(0,50,300,50)
#         self.radio3.setGeometry(0,100,300,50)
#         self.radio4.setGeometry(0, 150, 300, 50)
#         self.radio5.setGeometry(0, 200, 300, 50)
#
#         self.setStyleSheet("QRadioButton{"
#                            "font-size: 40px;"
#                            "font-family: Arial;"
#                            "padding: 10px;"
#                            "}")
#
#         self.button_group1.addButton(self.radio1)
#         self.button_group1.addButton(self.radio2)
#         self.button_group1.addButton(self.radio3)
#         self.button_group2.addButton(self.radio4)
#         self.button_group2.addButton(self.radio5)
#
#         self.radio1.toggled.connect(self.radio_button_changed)
#         self.radio2.toggled.connect(self.radio_button_changed)
#         self.radio3.toggled.connect(self.radio_button_changed)
#         self.radio4.toggled.connect(self.radio_button_changed)
#         self.radio5.toggled.connect(self.radio_button_changed)
#
#     def radio_button_changed(self):
#         radio_button = self.sender()
#         if radio_button.isChecked():
#             print(f"{radio_button.text()} is selected")
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())

