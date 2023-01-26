#Python Getting Started
# Python Datatypes
#1. String
""""
print("test")
print("Hello world!")
print("testing the \nnew line")

#2. Intergers and Floats
print(87423784)
print(54.4)

#3. Variables
city="Coimbatore"
print(city)
city="Bangalore"
print(city)
#a) Overriding variable value
city="Coimbatore"
city_da="Bangalore"
city=city_da
print(city)
#b) Spaces in teh printed values 
city = "Coimbatore"
cycle_shops= 10
print("City:",city,"Cycle Shops:",cycle_shops)
#c) Variable naming conventions
#variable name cannot used with space
#variable name cannot be used with number
#variable name cannot be used with soe certain words (like 'else')

"""
#Input from the user
"""""
name = input()
print(name)

name = input("Enter an name:")
print(name)

number = input("Enter a number:")
print(number)

number = input("Enter a number:")
print("The entered number",number,"is",type(number))

number1=5
#print(type(number1))
print("The number",number1,"is",type(number1))
number2=5.5
#print(type(number2))
print("The number",number2,"is",type(number2))

#Get the numbers as input from the user
#We canot directly get the number as input from the user instead do converting strings into numbers/floats
number3= input("Enter the number:")
number3=int(number3)
print("The entered number",number3,"is",type(number3))

number4=int(input("Enter the number:"))
print("The entred number",number4,"is",type(number4))

number5=float(input("Enter the number:"))
print("The entred number",number5,"is",type(number5))
"""

#Multiple lines commands (notes)
# Select the multiple lines and use cmd + / 
"""
#Multiline string
# test = '''This is a
# multiline string'''
# print(test)

#Operators

#Arithmetic operators
# Addition: +
# Subtraction: -
# Multiplication: *
# Division: /
# Floor division: //
# Remainder: %
# Exponent: **

x = 5

result = x + 10 # addition
print(result)   # 15

result = x - 10 # subtraction
print(result)   # -5

result = x * 10 # multiplication
print(result)    # 50

result = x / 10 # division
print(result)   # 0.5

result = x ** 2   # exponent
print(result)     # 25

quotient = x // 2  # floor division
remainder = x % 2  # modulus

print("Quotient is", quotient) # 2
print("Remainder is", remainder) # 1
print(result) # variable result holds the last stored value 25

# harder to understand
number = 34 * 5 - 5 / 3 # 168.33333
print(number)
# easier to understand
number = (34 * 5) - (5 / 3) # 168.33333
print(number)

#Concatenate two strings
str1 = "Vivek "
str2 = "Murugesan "
print(str1 + str2)

#Assignment operators
x,y=5,6
print(x,y)

#Compound operators => Arithmetic + Assigment operators
x = 5
y = 6
x += 10 # x = x + 10
y -= 10 # y = y - 10
print(x,y)

#Program to Compute Discount
fee = 4525
discound_percent = 10
discound_price = (fee * (discound_percent/100))
#discound_price = discound_percent/100*fee
print("Discound Price is:",discound_price)
discound_fee = fee - discound_price
print("Amount to be paid after 10 percentage discound is:",discound_fee)

# Program to convert kilometers to files
distance_km = 564.5
conversion_ratio = 0.621371
distance_miles = distance_km * conversion_ratio
print("Kilmoters to miles for",distance_km,"km is:",distance_miles,"miles") # 350.7639295

"""

"""
#Boolean Data type
result1 = True
result2 = False

print(result1) # True
print(result2) # False

number = 5
print(number < 10) # True
number = 15
print(number < 10) # False

# Comparison Operators:

# <          Less than
# >          Greater than
# ==         Equal   
# !=         Not equal
# >=         Greater than or equal to
# <=         Less than or equal to

# comparison operators in action

number = 15
print(number > 10) # True

number = 10
print(number > 10) # False

number = 10
# equal to
print(number == 10) # True

number = 10.0
# comparing float and integer
print(number == 10) # True

number = '10'
# comparing string and integer
print(number == 10) # False

number = '10'
# not equal to
print(number != 10) # True

number = 10
# less than or equal to
print(number <= 10) # True

number = 10
# greater than or equal to
print(number >= 10) # True

#Not operators
result = True
print(result) # True

result = True
print(not result) # False

language = "Python"
print("1.", language == "python")

#Programming Task
age = 18
print("2.", age >= 18)
print("3.", age > 18)

print("4.", not age >= 18 and language == "Java")

"""

"""
#If statement => decision making
pass_mark = 50
score = int(input("Enter your score: "))
if score > pass_mark:
    print("Congrats! you have paassed the test")
elif pass_mark == score:
    print("You have passed successfully with a pass mark",pass_mark)
else:
   print('Sorry! please better luck next time')

# Can you create a program to check whether a number is positive or negative or 0?
# To create this program, create a variable named number and assign a float value to it based on the user input. 
# Then using a if statement, check if the number variable is positive or negative or 0.
#     If number is positive, print "The number is positive"
#     If number is 0, print "The number is 0"
#     If number is negative, print "The number is negative"

number = float(input("Please enter the float number:"))
if(number>0):
    print("The number",number,"is positive")
elif(number==0):
    print("The number is 0")
else:
    print("The number",number,"is negative")

"""

"""
#While loop
count = 0
while count <= 5:
    print("Inside loop:",count)
    count = count + 1

number = int(input("Enter the number: "))
count = 1
while count <= 10:
    prodcut = number * count
    print(number,"x",count,"=",prodcut)
    count = count + 1

count = 0
while count <= 5:
    print("Inside loop:",count)
    count = count + 1

number = int(input("Enter the number: "))
count = 10
while count >= 1:
    prodcut = number * count
    print(number,"x",count,"=",prodcut)
    count = count - 1
"""

"""
# For loop
# Python sequences
text = "Python"
for text in text:
    print(text)

text = "Python"
languages = ['English', 'French', 'German']
for languages in languages:
    print(languages)

for count in range (1, 6):
    print("for loop:",count)

# count = 1
# while count <6:
#     print("while loop:",count)
#     count = count +1

for count in range (1, 6):
    print(count)

total = 0

number = int(input("Enter an integer: "))

for count in range(1, 11):
    product = number * count
    print(number, "*", count, "=", product)

# looping from 1 to 100
for number in range(1, 101):
    if(total == 0):
        print("total:",total,"number:",number,"total:",total)
        
    total = total + number
    print("total:",total,"number:",number,"total:",total)  

print(total)
"""

"""
#Break
for item in range(1,6):
    print(item)
    break

for item in range(1,6):
    if(item==4):
        break
    print(item)
print(item)    

#taking the input from user repeatly 
while True:
    number =float(input("Enter the number:")) 
    if(number<0):
        print("The entered number is negative:",number)
        break
    print("The entered number is:",number)

#Continue
for i in range(2):
    number = float(input("Enter the number:"))
    print("The entered number is",number)

for i in range(3):
    number = float(input("Enter the number:"))

    if(number <0):
        continue
    print("The entered number is",number)

languages = ["Python", "Java", "Swift", "C", "C++"]
for languages in languages:
    if languages=="Swift" or languages=="C++":
        continue
    print(languages)



#Pass statement
number = 5.5

if number > 0.0:
    pass
"""

"""
#Functions
#Call the funtions after created it
def func():
    print("Hi function")

func()

#functions with arguments
def func1(name):
    print("Hi", name)

func1("Vivek")   

name = input("Enter the name:")
def func2(name):
    print("Hi", name)
    
func2(name)  

def func3(n,m):
    result = n + m
    print("The sum is:",result)

# number1 = float(input("Enter the first number:"))
# number2 = float(input("Enter the second number:"))
number1,number2 = float(input("Enter the first number:")),float(input("Enter the second number:"))
func3(number1,number2)

def func3(n,m):
    result = n + m
    return result

number1,number2 = float(input("Enter the first number:")),float(input("Enter the second number:"))
result = func3(number1,number2)
print("The sum is:",result)

marks = [55, 64, 75, 80, 65]

lenght = len(marks)
print("The length is:",lenght)

marks_sum = sum(marks)
print("The total mark is:",marks_sum)


def avg_marks(marks):
    lenght = len(marks)
    total = sum(marks)
    average_marks = total/lenght
    return average_marks

def grade(average_marks):
    if average_marks >= 80:
        grade ='A'
    elif average_marks >= 60 and average_marks < 80:
         grade ='B'
    elif average_marks >= 50 and average_marks < 60:
         grade ='C'
    else:
        grade ='F'
    return grade

marks = [55, 64, 75, 80, 65]
average_mark = avg_marks(marks)
grade_mark = grade(average_mark)

print("The average mark for your exam is:",average_mark)
print("The Grade for your marks is:",grade_mark)

def add_numbers(number1,number2):
    result = number1 + number2
    return result

def multiply_numbers(number1,number2):
    result1 = number1 * number2
    return result1

number1,number2 = float(input("Enter the first number:")),float(input("Enter the second number"))
added_numbers = add_numbers(number1,number2)
multiplied_numbers = multiply_numbers(number1,number2)

print("The sum of the given two number is",added_numbers)
print("The multiplied of the given two number is",multiplied_numbers)

"""

"""
#Local and Global Variables
#from unittest import result

def add_numbers(n1, n2):
    result = n1 + n2
    return result

output = add_numbers(2, 5)
print(output)

message="outside function"

def greet():
    message="inside function"
    print(message)

greet()
print(message)

def greet():
    global message #to handle with care since it's hard to understand the value if such global variable 
                   #used inside the function
    message="inside function"
    print(message)

greet()
print(message)

"""

"""
#Python List and Tuple
#List - sequence of itmes in order

# list of integers
#from ctypes.wintypes import PINT
#from ctypes.wintypes import LANGID
#from xmlrpc.client import boolean


numbers = [1, 5, 6, -4]
print(numbers)
print(len(numbers))

#mixed list
random_list = [2.5, "Vivek", -5, 2.7]
print(random_list)

#empty list
list1 = []
print(list1)
print(len(list1))


languages = ["Python","Java","C","C++"]
for languages in languages:
    if languages == "C":
        continue
        print("test")  
    print(languages)   

languages = ["Python","Java","C","C++"]
print(languages[-1]) # 0 for the first index value and -1 for the last index value 

languages = ["Python","Java","C","C++"]
print(languages[0:3])
print(languages[0:4])
print(languages[0:-1])

languages = ["Python", "JavaScript", "C++", "Kotlin"]
# modifying the second item
languages[3]="Java"
print(languages)
#In keyword to return true or false for decision making it will be useful
print("Python" in languages)
for languages in languages:
     print("Python" in languages)
    
#List Methods
languages = ["Python", "JavaScript", "C++", "Kotlin"]
languages[3] = "Java"
print(languages)
languages.append("Plsql")
print(languages)
languages.insert(2,"C")
print(languages)
languages.remove("C++")
print(languages)
languages1 = languages.copy()
print(languages1)
"""

"""
#Tuples
numbers = (21, -5, 6, 9)
print(numbers)
print(numbers[3])
#numbers[0]=2 => 'tuple' object does not support item assignment

for numbers in numbers:
    print(numbers)

mixed_list = ["Hello", -34, "Java", True]

print("1.", mixed_list[-1]) # 1. True

mixed_list[1] = "Hi"
print("2.", mixed_list) # 2. 'Hello', 'Hi', 'Java', True

mixed_tuple = (1, 3, 4, 5)

mixed_tuple[1] = 100
print("3.", mixed_tuple) # 'tuple' object does not support item assignment

"""

"""
#Python Strings
# single quote
text = 'Hello there'
print(text)

# double quotes
text = "Hello there"
print(text)

"""
# triple quotes for multiline strings
# text = """Hello there.
# How are you doing"""
# print(text)

"""
#text = "He said, "What's there?""
text = "He said, \"What\'s there?\""
print(text)

text = "Python"
print(text[-1])
#Slicing operator
print(text[0:])
print(text[3:])
print(text[0:5]) # last index is exclusive

#Change and Delete String Characters
# text = "Python"
# text[0] = "p"
# print(text)

#Python String Operations
text1 = "Python"
text2 = "Programming"

result = text1 + " " + text2
print(result)

text = "Python"
text_len = len(text)
print("text_len:",text_len)

new_text = text * 3
new_text_len = len(new_text)
print("new_text_len:",new_text_len)

print(new_text)

#Iterating through a String
text = "Python"
for character in text:
    print(character) 

#In keyword to check the string
text = "Python"
print("P" in text)
print("yth" in text)
print("ont" in text)

#Python String Methods
#lower() and upper() method
text = "I like Python 3"
result = text.lower()
print(result)

text = "I like Python 3"
result = text.upper()
print(result)

#find() method
text = "I like Python 3"
result = text.find("Python")
print(result)

#replace() method
text = "I like Python 3"
result = text.replace("Python 3", "Java")
print(result)

quote = "Talk is cheap. Show me the code."
print("1.", quote[3])
print("2.", quote[-3])
print("3.", quote.replace("code", "program"))

"""

"""
#Python Dictionary
person1 = {"name": "vivek", "age": "30"}
print(person1)
print(person1["age"])
print(person1.get("hobbies"))
print(person1.get("hobbies",["cycling","reading"]))

#Add and Change Dictionary Elements
person1["age"] = "31"
print(person1)
person1["hobbies"] = ["cycling","reading"]
print(person1)

#Dictionary methods
#Remove Elements From a Dictionary
print("removing age:",person1.pop("age"))
print(person1)

#Iterating Through a Dictionary
person1 = {"name": "Linus", "age": 21}
for key in person1:
    print(key)
    print(person1[key])

synonyms = {"mountain": "peak", "forest": "jungle"}
print("1.", synonyms["mountain"]) # 1. peak

synonyms["terrain"] = "land"
print("2.", synonyms) # 2. {'mountain': 'peak', 'forest': 'jungle', 'terrain': 'land'}

synonyms.pop("forest")
print("3.", synonyms) # 3. {'mountain': 'peak', 'terrain': 'land'}

"""

"""

#Python sets

animals = {"tiger","cat","tiger"}
print(animals)


#empty set
animals = set()
print(animals)

#non empty set
animals= set(["cat","tiger","horse"])
print(animals)

#Add Items to a Set
animals = {"dog", "cat", "tiger", "elephant", "dog"}
animals.add("monkey")

print(animals)

#Update items to a Set
animals = {"dog", "tiger", "elephant"}
wild_animals = ["tiger", "leopard", "horse"]

animals.update(wild_animals)
print(animals)

animals.update(wild_animals, {"dolphin"})
print(animals)

#Remove Items from a Set
animals = {"tiger", "cat", "elephant", "dog"}
#animals.remove("horse")
animals.discard("horse")
print(animals)

animals = {"tiger", "cat", "elephant", "dog"}
animals.remove("dog")
print(animals)

#Check if an item is in a Set
animals = {"tiger", "cat", "elephant", "dog"}
print("tiger" in animals)
print("ferret" in animals)

#Iterating Through a Set
animals = {"tiger", "cat", "elephant", "dog"}
for animal in animals:
    print(animal)

#Python Set Operations
#Union of Sets
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}

animals = domestic_animals.union(wild_animals)
animals1 = animals = domestic_animals | wild_animals

print(animals)
print(animals1)

#Intersection of Two Sets
# The intersection of two sets is a set of items that are common in both sets.
# To find the union of sets, we can either use the intersection() method or the ampersand symbol &.
domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}

common_animals = domestic_animals.intersection(wild_animals)
common_animals1 = domestic_animals & wild_animals

print(common_animals)
print(common_animals1)

"""

"""

#range() Function

import re


result = range(1,11)
print(result)
print(list(result))

for value in range(1,6):
    #print(value)
    print(value,"iteration")

for value in range(5):
    print(value)

#range() with step Parameter
result = list(range(1, 11, 5))
print("step args:",result)

result = list(range(5, -6, -1))
print(result)

result = range(3,31,3)
print(list(result))

for result in range(3,31,3):
    print(result)

"""

"""

#Python Object-Oriented Programming

#Python Classes and Objects

from numbers import Complex
from random import triangular


class Student:
    def chk_pass_fail(check):
        if check.marks >=40:
            #print("passed")
            return True
        else:
            #print("failed!, better luck next time")
            return False

student1 = Student()
student1.name = "Vivek"
student1.marks = 90
print(student1.name)
print(student1.marks)

pass_chk = student1.chk_pass_fail()
print(pass_chk)

student2 = Student()
student2.name = "virat"
student2.marks = 39
print(student2.name)
print(student2.marks)

pass_chk1 = student2.chk_pass_fail()
print(pass_chk1)

#init
class Student:
    def chk_pass_fail(check):
        if check.marks >=40:
            #print("passed")
            return True
        else:
            #print("failed!, better luck next time")
            return False

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

student1 = Student("Vivek", 95)
student2 = Student("Virat",36)
print(student1.name)
print(student1.marks)
print(student2.name)
print(student2.marks)

did_pass = student1.chk_pass_fail()
print("student1:",student1.name,student1.marks,did_pass)

did_pass = student2.chk_pass_fail()
print("student1:",student2.name,student2.marks,did_pass)

#Add Two Complex Numbers

class Complex:
    def __init__(self,real,image):
        self.real = real
        self.image = image

    def add(self,number):
        real = self.real + number.real
        image = self.image + number.image
        result = Complex(real,image)
        return result

n1 = Complex(5 ,6) 
n2 = Complex(-4, 2)  
result = n1.add(n2)

print("real =", result.real)
print("imag =", result.image)

class Tirangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
     
    def get_perimeter(self):
        perimeter = self.a + self.b + self.c
        return perimeter
    
t1 = Tirangle(3,4,5)
print(t1.get_perimeter())

"""

"""

#Everything in Python is an Object
#type() function
numbers = [1, 4, 7]
print(type(numbers))

numbers = (1, 4, 7)
print(type(numbers))

numbers = {1, 4, 7}
print(type(numbers))

n1 = 5
print(type(n1))

def function():
    pass

print(type(function))

#dir() function
numbers_list = [1, 2]
print(type(numbers_list))
print(dir(numbers_list))

result = numbers_list.__add__([3,4])
print(result)
result = numbers_list + [3,4]
print(result)

number1,number2 = 5,7
print(id(number1))
print(id(number2))
number3 = number2
print(id(number3))


a = [1,2,3]
#b = a
b = a.copy()

a.append(4)

print("a=",a)
print("b=",b)

print(id(a))
print(id(b))

"""

"""

#Inheritance in Python

class Animal:
    def eat(self):
        print("can eat")

class Dog(Animal):
    def bark(self):
        print("can bark")

class Cat(Animal):
    def get_grumpy(self):
        print("getting grumpy.")

dog1 = Dog()
dog1.eat()
dog1.bark()

cat1 = Cat()
cat1.eat()


class Polygon:
    def __init__(self,sides):
        self.sides = sides
    
    def display_info(self):
        print("A polygon is a two dimensional shape with straight lines")

    def get_perimeter(self):
        perimeter = sum(self.sides)
        return perimeter

class Triangle(Polygon):
    def display_info(self):
        print("A triangle is a polygon with 3 edges")
        #Polygon.display_info(self)
        return super().display_info()


class Quadrilateral(Polygon):        
    def display_info(self):
        print("A quadrilateral is a polygon with 4 edges")

t1 = Triangle([5,6,7])
perimeter = t1.get_perimeter() 
print("The perimeter is",perimeter)

#method overriding
t1.display_info()

"""

"""

#Python Modules

#import math 
import imp
import math as m
import math

number = 25
#print(dir(number))
print(dir(math))
result = m.sqrt(number)
print(result)
print(m.pi)


#from math import sqrt
from math import pi, sin, sqrt 
#from math import*

num = sqrt(64)
print(num)

value = sin(pi/2)
print(value)

#import custom modules
#Let's a module named calculator that will contain functions to perform arithmetic operation
#First, create a file named calculator.py in the same directory (refer calculator.py)
import calculator

result = calculator.add(2,3)
print(result)

result1 = calculator.multiply(2,3)
print(result1)

"""

"""

#pip - standard package manager
import pandas as pd
print(pd)

"""

"""
#Exceptions
# numerator = 10
# denominator = 0
# print(numerator/denominator)

from textwrap import indent


try:
    numerator = int(input("Enter the numerator:"))
    denominator = int(input("Enter the denominator:"))
    print(numerator/denominator)

    my_list = [1, 2, 3]
    i=int(input("Enter index:"))
    print(my_list[i])

except ZeroDivisionError:
    print("Denominator cannot be 0 , Please try again")

except IndexError:
    print("Index cannaot be greater than size of list") 

print("Program ends")

#Finally
try:
    print(10/0)

except:
    print("wrong denominator")

finally:
    print("finally")


"""

"""
#Python os module
import os

current_dir = os.getcwd() #current working directory
print(current_dir)
  
os.chdir("E:\Python\Python_Handwritten_Notes")
print(os.getcwd())


with open("testing.txt","w") as f:
    f.write("testing for creating/writing a file in the changed directory")

#list the directory 
print("cwd files:",os.listdir())
print(os.listdir("E:\Python"))

with open("testings.txt","w") as f:
    f.write("testing for creating/writing a file in the changed directory")

#os.mkdir("tests/tt")
#os.rename("tests","test-new")
os.remove("testings.txt") # remove a file

"""

"""
#remove a directory and clear all the files inside the directory at first 
import os

print("cwd:",os.getcwd())

os.chdir("E:\Python\Python_Handwritten_Notes")
#print("cwd:",os.getcwd())
#print("cwd_files:",os.listdir())

cwd = os.getcwd()
print("cwd:",os.getcwd())

files_in_dir = os.listdir(cwd)
print("files_in_dir:",files_in_dir)

for files in files_in_dir:
     os.remove(f'{cwd}/{files}')

print("files after removal:",os.listdir(cwd))
#os.rmdir("E:\Python\Python_Handwritten_Notes")

"""


"""
#Iterators
from unittest import result
from xml.dom.minidom import Element
from numpy import number


numbers = [1, 2, 3]
print(dir(numbers))

value = numbers.__iter__()
print(value)

item1 = value.__next__()
print(item1)

item2 = value.__next__()
print(item2)

item3 = value.__next__()
print(item3)

# iter instead of __iter__ & next instead of __next__
value = iter(numbers)
print(value)

item1 = next(value)
print(item1)

item2 = next(value)
print(item2)

item3 = next(value)
print(item3)

# item4 = next(value)
# print(item4)

num_list = [1, 4, 9]
iter_obj = iter(num_list)

while True:
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break


numbers = [1,4,6]

for element in numbers:
    print(element)

#Creating Custom Iterators

class Even():
    def __init__(self,max):
        self.n = 2
        self.max = max
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.n <= self.max:
            result = self.n
            self.n += 2
            return result
        else:
            raise StopIteration

numbers = Even(10) 
print(next(numbers))   
print(next(numbers))   
print(next(numbers))   
print(next(numbers))   
print(next(numbers))  
#print(next(numbers))   


"""


"""
#Generators
from tkinter import N


def even_generator():
    n = 0
    n += 2
    yield n

    n +=2
    yield n

    n +=2
    yield n

    pass


numbers = even_generator() 
print(next(numbers))   
print(next(numbers))   
print(next(numbers))  
#print(next(numbers)) 

def even_generators(max):
    n = 0

    while n <= max:
        yield n
        n += 2

numbers = even_generators(10)

print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
        
def generator_fibonacci():
    n1 = 0
    yield n1

    n2 = 1
    yield n2

    while True:
        n1 , n2 = n2, n1 + n2
        yield n2

seq = generator_fibonacci()
for seq in seq:
    if seq >= 100:
        break
    print("seq:",seq)
    

def odd_generators():
    n = 1

    while True:
        yield n
        n += 2

number = odd_generators()

for i in range (10):
    print(next(number))

"""


"""
#Python datetime module

import datetime as dt

current_date = dt.date.today()
print(current_date)

date1 = dt.date(2022, 5, 25)
print(date1)

print(date1.year,"\n",date1.month,"\n",date1.day)

time1 = dt.time(10, 47, 20, 234566)
print(time1)

print("Hour:", time1.hour)
print("Minute:", time1.minute)
print("Second:", time1.second)
print("Microsecond:", time1.microsecond)

import datetime as dt
datetime_obj = dt.datetime(2021, 11, 28, 23, 55, 59)

print(datetime_obj)

print(datetime_obj.date())
print(datetime_obj.time())

date_now = dt.datetime.now()
print(date_now)

current_time1 = dt.datetime.now()
nxt_new_yr = dt.datetime(2023,1,1)

print(abs(current_time1 - nxt_new_yr))
print(type(current_time1 - nxt_new_yr))


current_datetime = dt.datetime.now()
print(current_datetime)

str_date = current_datetime.strftime("%A,%B,%d,%Y")
print(str_date)

#Python strptime() method
#The strptime() method converts strings to datetime objects.

date_str = "25 May 2022"
date_obj = dt.datetime.strptime(date_str, "%d %B %Y")
print(date_obj)

"""

#"""
#Python Decorators

from unittest import result


def inc(x):
    return x + 1

#print(inc(3))    

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 5))


def print_msg(msg):
    greeting = "Hello"

    def printer():
        print(greeting,msg)

    #printer()
    return printer

#print_msg("Python is awesome")
func = print_msg("Python is awesome")
func()


# def printer1():
#     print("Hello World!")

def display_info(func):
    def inner():
        print("Executing", func.__name__,"function")
        func() #printer1
        print("Fininshed execution")

    return inner

#printer1()

#display_info1 = display_info(printer1)
#display_info1()
@display_info
def printer1():
    print("Hello World!")
printer1()

def smart_divide(func):
    def inner(a, b):
        print("Dividing", a, "by", b)
        if b == 0:
            print("Cannot divide by 0!")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a/b

value1 = divide(15, 3)
print(value1)

value2 = divide(5, 0)
print(value2)


def stars(func):
    def inner(arg):
        print("*" * 30)
        func(arg)
        print("*" * 30)
    return inner

def percent(func):
    def inner(args):
        print("%" * 30)   
        func(args) 
        print("%" * 30)
    return inner

@stars
@percent
def printer2(msg):
    print(msg)

printer2("Decorators are wonderful")


print(30*6)
#"""