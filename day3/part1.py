"""
Complexity: O(n)

Explnation: None needed
"""

with open('input.txt', 'r') as input_file:
    trees = input_file.read().splitlines() 

width = len(trees[0])

horizontal_pos = 0

collisions = 0

for i in trees:
    if i[horizontal_pos % width] == '#':
        collisions += 1
    
    horizontal_pos += 3

print(collisions)


