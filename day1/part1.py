"""
Solution Complexity: O(n)

Solution Explanation: Iterate though list, storing results as keys of a  dictionary to allow constant time determination for 
successive list elements. As we can eliminate inputs greater than 2020 we have no problem with hash duplicity for theoretical large inputs.
"""


input_file = open('input.txt', 'r')
array = list(map(int, input_file.read().splitlines()))
input_file.close()

#Initialise dict to log unmatched entries in
attempted = {}

for i in array:
    if (2020 - i) in attempted:
        print(i * (2020 - i))
    else:
        attempted[i] = True




