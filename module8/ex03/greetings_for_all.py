#!/usr/bin/env python

def greetings(name):
    if name==None:print("Hello noble stranger.")
    if type(name) == str:
     print("Hello, "+name)
    else:
     print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)


#AAAAHH