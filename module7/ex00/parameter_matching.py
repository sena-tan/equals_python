#!/usr/bin/env python3
import sys

if len(sys.argv) != 2:
 print("none")
else:
 para = sys.argv[1]
 if para == input("What was the parameter? "):
  print("Good Job!")
 else:
  print("Nope, sorry...")