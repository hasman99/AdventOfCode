"""
Complexity: O(n)

Explanation: For each group create a dictionary keyed by questions they answered yes. This allows us to determind if a given question
has allready occured in constant time. (although tbf as there is only 26 questions would also be constant time if we just compare with 
each question already answered.)
"""

with open('input.txt', 'r') as input_file:
    groups = input_file.read().split('\n\n')

total = 0

for group in groups:
    questions = {}
    for person in group.split():
        for question in person:
            questions[question] = True
    
    total += len(questions.keys())

print(total)
