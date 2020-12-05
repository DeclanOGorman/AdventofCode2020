import re

def isValid(passport, requiredFields, checkField = False):
    fields = 0
    for field in requiredFields:
        if field in passport: 
            if checkField:
                if len(re.findall(requiredFields[field],passport[field])) > 0: fields += 1
            else: 
                fields += 1
    if fields == len(requiredFields): return 1
    return 0

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

requiredFields = {
    'byr': '^(200[0-2]|19[2-9][0-9])$',
    'iyr': '^(2020|201[0-9])$',
    'eyr': '^(2030|202[0-9])$',
    'hgt': '^(19[0-3]cm|1[5-8][0-9]cm|7[0-6]in|59in|6[0-9]in)$',
    'hcl': '^(#[0-9a-f]{6})$',
    'ecl': '^(amb|blu|brn|gry|grn|hzl|oth)$',
    'pid': '^([0-9]{9})$',
}

validA = 0
validB = 0
for passport in passports:
   validA += isValid(passport, requiredFields)
   validB += isValid(passport, requiredFields, True)

print(f'Part A: {validA} passports with correct fields')
print(f'Part B: {validB} passports with correct and valid fields')