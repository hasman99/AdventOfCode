"""
Complexity: O(n^3)  (Running 'test_sequence' n times. This doesen't feel the best possible. There are clearly optimisations that can be made but none
I can see any that decrease the asymptotic complexity)

Explanation: Brute force
"""

def test_sequence(instructions):
    length = len(instructions)
    curr = 0
    acc = 0
    visited = []
    while (curr not in visited) and (curr < length) and (curr >= 0):
        if instructions[curr][0] == 'nop':
            visited.append(curr)
            curr += 1
        elif instructions[curr][0] == 'acc':
            acc += instructions[curr][1]
            visited.append(curr)
            curr += 1
        else:
            visited.append(curr)
            curr += instructions[curr][1]
   
    if curr == length:
        valid = True
    else:
        valid = False
    
    return (valid, acc)
    
        
with open('input.txt', 'r') as input_file:
    raw_instructions = input_file.read().splitlines()
    instructions = [[x.split()[0], int(x.split()[1])] for x in raw_instructions]

for i in range(0, len(instructions)):
    op = instructions[i][0]
    if op == 'nop':
        instructions[i][0] = 'jmp'
    elif op == 'jmp':
        instructions[i][0] = 'nop'
    
    (valid, acc) = test_sequence(instructions)

    if valid:
        print(acc)

    instructions[i][0] = op

    