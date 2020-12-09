"""
Solution Complexity: O(n^2)

Solution Explanation: Iterate through list, compute pairwise sums and store as keys in a dictionary. Again as we can eleminate inputs
greater than 2020 we have no problem with hash collisions.

"""

input_file = open('input.txt', 'r')
array = list(map(int, input_file.read().splitlines()))
input_file.close()

# Initialise dictionary to store pairwise sums in format 'pairwise_sum':'pairwise_product'
attempted = {}

for idx, val in enumerate(array):
    if (2020 - val) in attempted:
        print(val * attempted[2020 - val])
    else:
        for j in array[:idx]:
            # Since we assume there is a unique triple summing to 2020 the issue here caused by non-uniquness of
            # pairwise sums is a non issue.
            attempted[j + val] = j * val