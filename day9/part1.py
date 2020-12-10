"""
Complexity: O(n) (my solution isn't all that efficient but since we are always only looking at the last 25 numbers it is 
linear in the total length of the list)

Explanation: More or less brute force
"""

def distinct_sum_exists(nums, total):
    #Determinds if two distinct numbers exist in 'nums' that sum to 'total'
    tried = []
    for x in nums:
        if ((total - x) in tried) and total != 2*x:
            return True
        else:
            tried.append(x)

    return False


with open('input.txt', 'r') as input_file:
    array = input_file.read().splitlines()
    array = [int(x) for x in array]

for i in range(25, len(array)):
    if not distinct_sum_exists(array[i - 25: i], array[i]):
        print(array[i])
        break

    