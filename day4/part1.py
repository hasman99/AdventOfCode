"""
Complexity: O(n)

Explanation: Since field validation isn't required we can determind validity just by counting number of fields present.
"""

with open('input.txt', 'r') as intput_file:
    passports = intput_file.read().split('\n\n')

valid = 0

for passport in passports:
    fields = set(map(lambda x: x.split(':')[0], passport.split()))
    
    if len(fields) == 8 or ((len(fields) == 7) and (not 'cid' in fields)):
        valid += 1

print(valid)