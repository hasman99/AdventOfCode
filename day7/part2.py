"""
Complexity: This depends on a number of factors:
a) If there is a constant bound on the number of types of bag in a given bag
b) How python evaluates line 50. If it attempts to work through the recursion stack of each function in parrallel there is potential
to introduce unwanted higher order complexity.

Explanation: ASSUME BAG TREE IS ACYCLIC. ASSUME AT MOST 1 RULE PER BAG. We recursivly calculate how many bags are in the shiny gold bag.
We usememoization to ensure the recursion happens quickly and we dont calculate any results twice. 
"""
def format_rule(rule):

    def format_item(item):
        if item[-1] == 's':
            return (int(item[0]), item[2:-5])
        else:
            return (int(item[0]), item[2:-4])

    #Remove full stop
    rule = rule[:-1]

    [bag, raw_contents] = rule.split(' bags contain ')

    if raw_contents == 'no other bags':
        contents = []
    else:
        contents = raw_contents.split(', ')
        contents = [format_item(item) for item in contents]
        
    
    return (bag, contents)

with open('input.txt', 'r') as input_file:
    raw_rules  = input_file.read().splitlines()

    formatted_rules = [format_rule(rule) for rule in raw_rules]

    bags = [rule[0] for rule in formatted_rules]

    rules = { rule[0] : rule[1] for rule in formatted_rules }

#Store results of the function below to limit recursion depth
results = { bag : None for bag in bags }

def total_contents(bag):
    if bag not in results:
        #This should never happen but if it does we will interperate as having no contents
        return 0
    elif results[bag] != None:
        return results[bag]
    else:
        output = sum([ x[0] + (x[0] * total_contents(x[1])) for x in rules[bag]])
        results[bag] = output
        return output

print(total_contents('shiny gold'))
