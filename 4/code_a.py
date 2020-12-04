passports = []
passport = {}
with open('./4/input_a.txt', 'r') as f:
    for line in f:
        for field in line.split():
            passport[field.split(':')[0]] = field.split[1]
        if line == '': 
            passports.append(passport)
            passport = {}
passports.append(passport)

requiredFields = ['byr','iyr','eyr','hgt','hcl','ecl','pid']

for passport in passports:
    