"""
Complexity: O(nlogn)

Explanation: Sort seat ids, then go through list comparing each element with successive element to find my seat.
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

ids = [get_seat_id(b_pass) for b_pass in b_passes]
ids.sort()

for i in range(0, len(ids) - 1):
    #We allow for duplicate seats
    if ids[i + 1] != ids[i] and ids[i + 1] != ids[i] + 1:
        print(ids[i] +  1)