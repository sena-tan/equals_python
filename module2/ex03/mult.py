#!/usr/bin/env python

num1 = int(input("Pick a number:"))
num2 = int(input("Pick another number:"))

number = int(num1*num2)

print(number)

if number < 0:
 print("The result is negative.")
if number > 0:
 print("The result is positive.")
if number == 0:
 print("The result is positive and negative.")
