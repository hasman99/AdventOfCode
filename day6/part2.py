"""
Complexity: O(n)  (for each group determination of count is linear in size of group)

Explanation: For each group go through every question and see if all members of the group have that question. Since there is 26
questions this takes time linear in number of people in the group.
"""

with open('input.txt', 'r') as input_file:
    groups = input_file.read().split('\n\n')

total = 0

for group in groups:
    count = 0
    for question in 'abcdefghijklmnopqrstuvwxyz':
        if all([(question in person) for person in group.split()]):
            count += 1

    total += count

print(total)
