#!/usr/bin/python

"""
This is a multiline comment
"""
# this is a one line comment
print("Hello dude!")

print("------Variables------")
x = 5
y = "John"
print(x)
print(y)

"""
Casting types
"""
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print("Values of x, y, and z:")
print(x, y, z)

print("Types of x, y, and z:")
print(type(x),type(y),type(z))


print("Multiple variables in one line:")
p, q, r = "Prague", "London", "Berlin"
print(p)
print(q)
print(r)

print("One variable in multiple lines:")
s = t = u = "Prague"
print(s)
print(t)
print(u)

# Unpack a list
cities = ["Sao Paulo", "New York", "Toronto"]
x, y, z = cities
print(x)
print(y)
print(z)

# Output variables: must be the same type. Otherwise they must be separated/joined by commas
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Global and local variables:
print("------Global and local variables------")
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


print("--- To change the value of a global variable inside a function, refer to the variable by using the global keyword ---")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)


print("--- Get the character at position 1 (should be 'e')---")
a = "Hello, World!"
print(a[1])

print("--- Looping ---")
for x in "banana":
  print(x)


print("--- Strip removes the spaces surrounding the string ---")
a = " Hello, World! "
print(a.strip())

print("--- Splitting ---")
a = "Hello, World!"
b = a.split(",")
print(b)
a = "This is a no-brainer"
b = a.split("-")
print(b)


print("--- Concatenating ---")
a = "Hello"
b = "World"
c = a + " " + b
print(c)

print("--- Use the format() method to insert numbers into strings ---")
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

print("--- format() receives infinite number of arguments ---")
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

print("--- Or we can use indexes, like C ---")
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

"""
Python Collections (Arrays)
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
*Set items are unchangeable, but you can remove and/or add items whenever you like.

**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.
"""