"""
Solution Complexity: O(n)

Solution Explanation: None needed

"""

input_file = open('input.txt', 'r')
array = input_file.read().splitlines()
input_file.close()

valid = 0

for i in array:
    lower_bound = int(i.split()[0].split('-')[0])
    upper_bound = int(i.split()[0].split('-')[1])

    char = i.split()[1][0]

    password = i.split()[2]

    if password.count(char) >= lower_bound and password.count(char) <= upper_bound:
        valid += 1

print(valid)


