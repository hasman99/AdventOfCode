"""
Complexity: O(n)

Explanation: Convert each passport into a python dict and do the necessary tests.
"""

import string

def is_valid(fields):

    #byr
    if not 'byr' in fields:
        return False
    elif not fields['byr'].isnumeric():
        return False
    elif int(fields['byr']) < 1920 or int(fields['byr']) > 2002:
        return False
    
    #iyr
    if not 'iyr' in fields:
        return False
    elif not fields['iyr'].isnumeric():
        return False
    elif int(fields['iyr']) < 2010 or int(fields['iyr']) > 2020:
        return False

    #eyr
    if not 'eyr' in fields:
        return False
    elif not fields['eyr'].isnumeric():
        return False
    elif int(fields['eyr']) < 2020 or int(fields['eyr']) > 2030:
        return False
    
    #hgt
    if not 'hgt' in fields:
        return False
    elif not fields['hgt'][:-2].isnumeric():
        return False
    elif not fields['hgt'][-2:] in ['cm', 'in']:
        return False
    elif fields['hgt'][-2:] == 'cm' and (int(fields['hgt'][:-2]) < 150 or int(fields['hgt'][:-2]) > 193):
        return False
    elif fields['hgt'][-2:] == 'in' and (int(fields['hgt'][:-2]) < 59 or int(fields['hgt'][:-2]) > 76):
        return False 
    
    #hcl
    if not 'hcl' in fields:
        return False
    elif fields['hcl'][0] != '#':
        return False
    elif len(fields['hcl']) != 7:
        return False
    elif any([(x not in string.hexdigits) for x in fields['hcl'][1:] ]):
        return False
    
    #ecl
    if not 'ecl' in fields:
        return False
    elif fields['ecl'] not in ['amb','blu','brn','gry','grn','hzl','oth']:
        return False

    #pid
    if not 'pid' in fields:
        return False
    elif len(fields['pid']) != 9:
        return False
    elif not fields['pid'].isnumeric():
        return False

    return True
    
        

with open('input.txt', 'r') as intput_file:
    passports = intput_file.read().split('\n\n')

valid = 0

for passport in passports:

    fields = { field.split(':')[0] : field.split(':')[1] for field in passport.split() }
    
    if is_valid(fields):
        valid += 1

print(valid)
    




