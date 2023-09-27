import datetime
import os
import csv

with open("/workspaces/python-beginner-projects/projects/expense_tracker/ausgaben.csv", 'r') as file:
    lines = file.readlines()
    konto = ''.join([char for char in lines[0] if char.isdigit()]) # extract number out of String
print(konto)