"""
Complexity: O(n) (conversion to id is constant and determine max of list is linear)

Explanation: The boarding pass is essentially two binary numbers with B's instead of 1 etc. The function bellow just converts this to a 
decimal number.

"""

def get_seat_id(b_pass):
    row = 0
    for i in range(0, 7):
        row += (2**(6-i) if b_pass[i] == 'B' else 0)

    col = 0
    for i in range(0, 3):
        col += (2**(2-i) if b_pass[7 + i] == 'R' else 0)

    return 8 * row + col

with open('input.txt', 'r') as input_file:
    b_passes = input_file.read().splitlines()

print(max([get_seat_id(b_pass) for b_pass in b_passes]))