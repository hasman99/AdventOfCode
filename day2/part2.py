"""
Solution Complexity: O(n)

Solution Explanation: None needed

"""

input_file = open('input.txt', 'r')
array = input_file.read().splitlines()
input_file.close()

valid = 0

for i in array:
    initial_index = int(i.split()[0].split('-')[0])
    final_index = int(i.split()[0].split('-')[1])

    char = i.split()[1][0]

    password = i.split()[2]

    if (password[initial_index - 1] == char) ^ (password[final_index - 1] == char):
        valid += 1

print(valid)



