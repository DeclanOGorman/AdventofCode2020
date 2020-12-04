
import re

def isValid(passport, requiredFields):
    fields = 0
    for field in requiredFields:
        if field in passport: fields += 1
    if fields == len(requiredFields): return 1
    return 0

def isValidField(field, value):


passports = []
passport = {}
with open('./4/input_a.txt', 'r') as f:
    for line in f:
        for field in line.split():
            passport[field.split(':')[0]] = field.split(':')[1]
        if line.strip() == '': 
            passports.append(passport)
            passport = {}
passports.append(passport)

requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validationRule = {{'byr',  }}

valid = 0
for passport in passports:
   valid += isValid(passport, requiredFields) 

print(f'Part A: {valid}')