"""
Complexity: O(n)

Explanation: Since we are interested in a contiguous range, we start with the range 0:0 and then depending on the total
sum of the numbers in hour range expand and shrink our range as required, forcing expanding in the case our range is of lenght 1.
It takes a little convincing that the below approach will catch any valid range.
"""

with open('input.txt', 'r') as input_file:
    array = input_file.read().splitlines()
    array = [int(x) for x in array]


lb = 0  #lower bound of range
ub = 0  #upper bound of range
target = 14144619 
total = array[0] #Total sum in range

while (lb < len(array)) and (ub < len(array)):
    if lb == ub:
        #We can't allow ranges of length 1
        ub += 1
        if ub < len(array):
            total += array[ub]
    elif total < target:
        ub += 1
        if ub < len(array):
            total += array[ub]
    elif total > target:
        total -= array[lb]
        lb += 1
    else:
        break

print(max(array[lb:ub + 1]) + min(array[lb:ub + 1]))
