#!/usr/bin/env python

print("Enter a number less than 25")
n = input()
n = int(n)

if n >= 26: print("Error")
else:
 while n < 26:
  print("Inside the loop my variable is ", n)
  n += 1
