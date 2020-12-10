"""
Complexity: O(n^2) I don't know that this can be improved as each instruction we must check if we have been here before.
This requires checking membership in a list of length up to n. One may be tempted to use hashmaps for constant time lookup, but 
since n isn't bounded in the theoretical limit this would lead to collisions and not provide working solutions.

Explanation: Not needed.
"""

with open('input.txt', 'r') as input_file:
    raw_instructions = input_file.read().splitlines()
    instructions = [(x.split()[0], int(x.split()[1])) for x in raw_instructions]

curr = 0
acc = 0
visited = []

while curr not in visited:
    if instructions[curr][0] == 'nop':
        visited.append(curr)
        curr += 1
    elif instructions[curr][0] == 'acc':
        acc += instructions[curr][1]
        visited.append(curr)
        curr += 1
    else:
        visited.append(curr)
        #Well just assume the jmp instructions send us at least to a valid instruction
        curr += instructions[curr][1]

print(acc)