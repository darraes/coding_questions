'''Problem
Given a collection of out of order airline tickets, find what was the trip
done by the customer. For example:

t1: "BOS"  "NYC"
t2: "SFO"  "LAX"
t3: "LAX"  "BOS"

Result => SFO LAX BOS NYC

Expectations
 - Find a O(n) solution
 - Understand the complexity of the solution
 - Question about what is the input data structure and if the tickets list
 is complete and has only tickets from the same trip
 - Break the solution is proper functions
'''

def _find_start(tickets):
    # validations
    dest = set()
    for t in tickets:
        dest.add(t[1])
        
    result = None
    # This is a crappy validation
    for t in tickets:
        if not t[0] in dest:
            if result is not None:
                raise
            
            result = t[0]
    return result
    
def find_path(tickets):
    # validations
    transitions = {}
    for t in tickets:
        transitions[t[0]] = t[1]
        
    start = _find_start(tickets) # Invalid path will raise ex in this line
    
    path = []
    path.append(start)
    current = start
    while transitions.has_key(current):
        path.append(transitions[current])
        current = transitions[current]

    return path


print find_path([("BOS", "NYC"), ("SFO", "LAX"), ("LAX", "BOS")])
        