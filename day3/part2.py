"""
Complexity: O(n)

Explnation: None needed
"""

def collision_count(trees, horizontal_delta, vertical_delta):

    width = len(trees[0])
    horizontal_pos = 0
    vertical_pos = 0
    collisions = 0

    while vertical_pos < len(trees):
        if trees[vertical_pos][horizontal_pos % width] == '#':
            collisions += 1

        horizontal_pos += horizontal_delta
        vertical_pos += vertical_delta

    return collisions
        
with open('input.txt', 'r') as input_file:
    trees = input_file.read().splitlines() 

print(collision_count(trees, 1, 1) * collision_count(trees, 3, 1) * collision_count(trees, 5, 1) * collision_count(trees, 7, 1) * collision_count(trees, 1, 2))
