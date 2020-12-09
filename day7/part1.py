"""
Complexity: This depends on a number of factors:
a) If there is a constant bound on the number of types of bag in a given bag
b) How python evaluates line 54. If it attempts to work through the recursion stack of each function in parrallel there is potential
to introduce unwanted higher order complexity.

Explanation: ASSUME BAG TREE IS ACYCLIC. ASSUME AT MOST 1 RULE PER BAG. We recursivly calculate if a bag can eventually contain a 
shiny gold bag. We use memoization to ensure the recursion happens quickly and we dont calculate any results twice. 

"""
def format_rule(rule):

    def format_item(item):
        if item[-1] == 's':
            return item[2:-5] 
        else:
            return item[2:-4]

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

def can_contain_shiny_gold(bag):
    if not bag in results:
        #In this case we have no information about the contents of the bag
        return False
    elif results[bag] != None:
        #In this case we have already calculated the result
        return results[bag]
    elif 'shiny gold' in rules[bag]:
        results[bag] = True
        return True
    else:
        output = any([can_contain_shiny_gold(x) for x in rules[bag] ])
        results[bag] = output
        return output

total = 0
for bag in bags:
    if can_contain_shiny_gold(bag):
        total += 1

print(total)
