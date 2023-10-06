#3.1.1.4
n = int(input())
print(n>=100)

#3.1.1.10
print("Hello")
lily = str(input())
if lily == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best")
elif lily == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not", lily)

#3.2.1.5
for i in range(2, 8, 3):
    print("The value of i is currently", i)

#3.2.1.7
print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")


# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")

#3.2.1.15
c0 = int(input())
i = 0
if c0 > 0:
    while c0 != 1:
        while c0 % 2 != 0:
            c0 = 3*c0+1
            i = i+1
            print('%d'  %c0)
        while c0 % 2 ==0:
            c0=c0/2
            i = i+1
            print('%d'  %c0)
    print("step = %d" %i)

s = "hello"
def myfun():
    pass
"""
myfun.method()
myfun.__call__()
myfun()
"""

def max(a,b):
    return a if a > b else b

def fib(n):
    fn1, fn2 = 1, 0
    for i in range(n):
        print(fn1)
        fn1, fn2 = fn1+fn2, fn1
    else:
        print(fn1)
fib(200)

def fib(n):
    fn1, fn2 = 1, 0
    while fn1 <= n:
        print(fn1)
        fn1, fn2 = fn1+fn2, fn1
fib(200)
fib2 = fib
del fib
print(fib2)

def f(x,y,z=12):
    print(x,y,z)
def sum(a, b, c=0, d=0, e=0,):
    return a+b+c+d+e
f(1,2)
print(sum(1,2))
print(sum(2,3,4,5))

i = None
if i == None: print("yes")

#4.3.1.6
def is_year_leap(year):
    return year % 4 == 0 and (year % 100 !=0 or year % 400 == 0)
test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
	yr = test_data[i]
	print(yr,"->",end="")
	result = is_year_leap(yr)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#4.3.1.7
def days_in_month(year, month):
    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = months[month-1]
    if month == 2:
        if is_year_leap(year): days += 1
    return days
test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Failed")

#4.3.1.8
def day_of_year(year, month, day):
    total = 0
    for i in range(1,month):
        total += days_in_month(year, i)
    return total+day
print(day_of_year(2000, 12, 31))


#4.3.1.9
import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num)+1)):
        if (num % i) == 0: break
    else:
        return False
for i in range(1,20):
    if is_prime(i+1) == False:
        print(i+1, end="　")

#4.4.1.5
a = 1
def fun():
    global a
    a = 2
    print(a)
fun()
a = 3
print(a)

#4.5.1.6
def factorial(n):
    f = 1
    i = 1
    for i in range(i, n+1): 
        f *= i 
    return f
def factorial_2(n):
    if n <= 2: return 1
    else: return n*factorial_2(n-1)
print(factorial(5))
print(factorial_2(5))











import mod1
import mod2, mod3, mod4

import my_module
result = my_module.my_function(my_module.my_data)

from module import my_function, my_data
result = my_function(my_data)

from my_module import *
result = my_function(my_data)

from module import my_function as fun, my_data as dat
result = fun(dat)


import os
dir(os)

math
random
platform


import math
import sys
#same
import math, sys
from typing import _Alias  

print(math.sin(math.pi/2)) #1.0

def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None

pi = 3.14

print(sin(pi/2)) #0.999999 #not pi in math
print(math.sin(math.pi/2)) #1.0

from math import pi

print(math.e)

from math import sin, pi

print(sin(pi/2)) #1.0

pi = 3.14

def sin(x):
    if 2 * x == pi:
        return 0.999999
    else:
        return None
    
print(sin(pi / 2)) #0.999999



import math as m

print(m.sin(m.pi/2))

# from module import n as a, m as b, o as c
from math import pi as PI, sin as sine
print(sine(PI/2))



import math
for name in dir(math):
    print(name, end="\t")

import math
dir(math)

import math
# * 
print(math.pi, math.sin(math.pi / 4))

def sin(x):
    for i in range(10):
        (-1) ** i * x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return sin

print(sin(math.pi/4))
 
dir(math)

import random
for i in range(6):
    print(floor(random.random() * 49 + 1))


from random import randrange, randint

print(randrange(2), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 3))

from platform import processor

print(processor())

from platform import system

print(system())

from platform import version

print(version())

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)

#2.2.1.1
word = "py"
print(len(word))
#result:2
empty = "" 
print(len(empty))
#result:0
empty2 = " "
print(len(empty2))
#result:1
i_am = "I\"m"
print(len(i_am))
#result:3
#\不算

#2.2.1.2
multiline = '''Line #1
Line #2'''
print(len(multiline))
#result:15
#\n要算進去

#2.2.1.3
str1 = 'a'
str2 = 'b'
print(str1 + str2)
print(str2 + str1)
print(5 * 'a')
print('b' * 4)

#2.2.1.4
# Demonstrating the ord() function.
char_1 = 'a'
char_2 = ' '  # space
print(ord(char_1))
print(ord(char_2))

#2.2.1.5
# Demonstrating the chr() function.
print(chr(97))
print(chr(945))

#2.2.1.6
# Indexing strings.
the_string = 'silly walks'
for ix in range(len(the_string)):
    print(the_string[ix], end=' ')
print()
# Iterating through a string.
the_string = 'silly walks'
for character in the_string:
    print(character, end=' ')
print()

#2.2.1.7
# Slices
alpha = "abdefg"
print(alpha[1:3])
print(alpha[3:])
print(alpha[:3])
print(alpha[3:-2])
print(alpha[-3:4])
print(alpha[::2])
print(alpha[1::2])

#2.2.1.8
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" in alphabet)
print("F" in alphabet)
print("1" in alphabet)
print("ghi" in alphabet)
print("Xyz" in alphabet)
alphabet = "abcdefghijklmnopqrstuvwxyz"
print("f" not in alphabet)
print("F" not in alphabet)
print("1" not in alphabet)
print("ghi" not in alphabet)
print("Xyz" not in alphabet)

#2.2.1.9
alphabet = "abcdefghijklmnopqrstuvwxyz"
#del alphabet[0]
#won't work
alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet.append("A")
#won't work
alphabet = "abcdefghijklmnopqrstuvwxyz"
#alphabet.insert(0, "A")
#won't work
#string, 數字都是immutable

#2.2.1.10
alphabet = "bcdefghijklmnopqrstuvwxy"
alphabet = "a" + alphabet
alphabet = alphabet + "z"
print(alphabet)


#2.2.1.11
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))
# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')
t = [0, 1, 2]
print(min(t))
# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))

#2.2.1.12
# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')
t = [0, 1, 2]
print(max(t))

#2.2.1.13
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

#2.2.1.14
# Demonstrating the list() function:
print(list("abcabc"))
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

#capitalize() – changes all string letters to capitals;
#center() – centers the string inside the field of a known length;
#count() – counts the occurrences of a given character;
#join() – joins all items of a tuple/list into one string;
#lower() – converts all the string's letters into lower-case letters;
#lstrip() – removes the white characters from the beginning of the string;
#replace() – replaces a given substring with another;
#rfind() – finds a substring starting from the end of the string;
#rstrip() – removes the trailing white spaces from the end of the string;
#split() – splits the string into a substring using a given delimiter;
#strip() – removes the leading and trailing white spaces;
#swapcase() – swaps the letters' cases (lower to upper and vice versa)
#title() – makes the first letter in each word upper-case;
#upper() – converts all the string's letter into upper-case letters.
#endswith() – does the string end with a given substring?
#isalnum() – does the string consist only of letters and digits?
#isalpha() – does the string consist only of letters?
#islower() – does the string consists only of lower-case letters?
#isspace() – does the string consists only of white spaces?
#isupper() – does the string consists only of upper-case letters?
#startswith() – does the string begin with a given substring?

#2.3.1.1
# Demonstrating the capitalize() method:
print('aBcD'.capitalize())
print("Alpha".capitalize())
print('ALPHA'.capitalize())
print(' Alpha'.capitalize())
print('123'.capitalize())
print("αβγδ".capitalize())

#2.3.1.2
# Demonstrating the center() method:
print('[' + 'alpha'.center(10) + ']')
print('[' + 'Beta'.center(2) + ']')
print('[' + 'Beta'.center(4) + ']')
print('[' + 'Beta'.center(6) + ']')
print('[' + 'gamma'.center(20, '*') + ']')

#2.3.1.3
# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

#2.3.1.4
#index找不到會error
#find找不到會-1 
# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
print('kappa'.find('a', 2))
the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

#2.3.1.5
# Demonstrating the isalnum() method:
#checks if the string contains only digits or alphabetical characters (letters)
print('lambda30'.isalnum())
print('lambda'.isalnum())
print('30'.isalnum())
print('@'.isalnum())
print('lambda_30'.isalnum())
print(''.isalnum())

#2.3.1.7
# Example 1: Demonstrating the islower() method:
print("Moooo".islower())
print('moooo'.islower())
# Example 2: Demonstrating the isspace() method:
print(' \n '.isspace())
print(" ".isspace())
print("mooo mooo mooo".isspace())
# Example 3: Demonstrating the isupper() method:
print("Moooo".isupper())
print('moooo'.isupper())
print('MOOOO'.isupper())

#2.3.1.8
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

#2.3.1.9
# Demonstrating the lower() method:
print("SiGmA=60".lower())

#2.3.1.10
# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")
print("pythoninstitute.org".lstrip(".org"))
print("www.cisco.com".lstrip("w."))

#2.3.1.11
# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

#2.3.1.12
# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))
print("tau tau tau".rfind("ta", 9))
print("tau tau tau".rfind("ta", 3, 9))

#2.3.1.13
# Demonstrating the rstrip() method:
print("[" + " upsilon ".rstrip() + "]")
print("cisco.com".rstrip(".com"))

#2.3.1.14
# Demonstrating the split() method:
print("phi       chi\npsi".split())

#2.3.1.15
# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
print()
# Demonstrating the strip() method:
print("[" + "   aleph   ".strip() + "]")

#2.3.1.16
# Demonstrating the swapcase() method:
print("I know that I know nothing.".swapcase())
print()
# Demonstrating the title() method:
print("I know that I know nothing. Part 1.".title())
print()
# Demonstrating the upper() method:
print("I know that I know nothing. Part 2.".upper())

#capitalize() – changes all string letters to capitals;
#center() – centers the string inside the field of a known length;
#count() – counts the occurrences of a given character;
#join() – joins all items of a tuple/list into one string;
#lower() – converts all the string's letters into lower-case letters;
#lstrip() – removes the white characters from the beginning of the string;
#replace() – replaces a given substring with another;
#rfind() – finds a substring starting from the end of the string;
#rstrip() – removes the trailing white spaces from the end of the string;
#split() – splits the string into a substring using a given delimiter;
#strip() – removes the leading and trailing white spaces;
#swapcase() – swaps the letters' cases (lower to upper and vice versa)
#title() – makes the first letter in each word upper-case;
#upper() – converts all the string's letter into upper-case letters.

#endswith() – does the string end with a given substring?
#isalnum() – does the string consist only of letters and digits?
#isalpha() – does the string consist only of letters?
#islower() – does the string consists only of lower-case letters?
#isspace() – does the string consists only of white spaces?
#isupper() – does the string consists only of upper-case letters?
#startswith() – does the string begin with a given substring?


#2.3.1.18.lab
def mysplit(strng):
    str = strng.split()
    return str

print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))

#2.4.1.1
'alpha' == 'alpha'
'alpha' != 'Alpha'
'alpha' < 'alphabet'
'beta' > 'Beta'

#2.4.1.3
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)
print(first_greek)
print(first_greek_2)
print()
# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)
second_greek.sort()
print(second_greek)






class ExampleClass:
    def __init__(self, val = 1):
        self.__first = val
    
example_object_1 = ExampleClass()
example_object_2 = ExampleClass(2)

example_object_2.set_second(3)

example_object_3 = ExampleClass(4)
example_object_3.third = 5

example_object_1.__first += 10

print(example_object_1.__dict__)
print(example_object_2.__dict__)
print(example_object_3.__dict__)

# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

str()
int()
float()

string == number is always False;
string != number is always True;
string >= number always raises an exception.

# Caesar cipher.
text = input("Enter your message: ")
cipher = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)

# Caesar cipher - decrypting a message.
cipher = input('Enter your cryptogram: ')
text = ''
for char in cipher:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)

# Numbers Processor.

line = input("Enter a line of numbers - separate them with spaces: ")
strings = line.split()
total = 0
try:
    for substr in strings:
        total += float(substr)
    print("The total is:", total)
except:
    print(substr, "is not a number.")

# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 15:
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
    iban = int(iban2)
    if iban % 97 == 1:
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

try:
    print(first_number / second_number)
except:
    print("This operation cannot be done.")

print("THE END.")


try:
    print("1")
    x = 1 / 0
    print("2")
except:
    print("Oh dear, something went wrong...")

print("3")

try:
    x = int(input("Enter a number: "))
    y = 1 / x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry.")
except ValueError:
    print("You must enter an integer value.")
except:
    print("Oh dear, something went wrong...")

print("THE END.")


def bad_fun(n):
    try:
        return n / 0
    except:
        print("I did it again!")
        raise


try:
    bad_fun(0)
except ArithmeticError:
    print("I see!")

print("THE END.")
