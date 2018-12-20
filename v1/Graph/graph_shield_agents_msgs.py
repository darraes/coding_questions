# http://www.careercup.com/question?id=5104027241021440

# The SHIELD is a secretive organization entrusted with the task of guarding the world 
# against any disaster. Their arch nemesis is the organization called HYDRA. 
# Unfortunately some members from HYDRA had infiltrated into the SHIELD camp. 
# SHIELD needed to find out all these infiltrators to ensure that it was not compromised. 

# Nick Fury, the executive director and the prime SHIELD member figured out that every one 
# in SHIELD could send a SOS signal to every other SHIELD member he knew well. 
# The HYDRA members could send bogus SOS messages to others to confuse others, 
# but they could never receive a SOS message from a SHIELD member. 
# Every SHIELD member would receive a SOS message ateast one other SHIELD member, 
# who in turn would have received from another SHIELD member and so on till NickFury. 
# SHIELD had a sophisticated mechanism to capture who sent a SOS signal to whom. 
# Given this information, Nick needed someone to write a program that could look into 
# this data and figure out all HYDRA members. 

# Sample Input 
# Nick Fury : Tony Stark, Maria Hill, Norman Osborn 
# Hulk : Tony Stark, HawkEye, Rogers 
# Rogers : Thor, 
# Tony Stark: Pepper Potts, Nick Fury 
# Agent 13 : Agent-X, Nick Fury, Hitler 
# Thor: HawkEye, BlackWidow 
# BlackWidow:Hawkeye 
# Maria Hill : Hulk, Rogers, Nick Fury 
# Agent-X : Agent 13, Rogers 
# Norman Osborn: Tony Stark, Thor 

# Sample Output 
# Agent 13, Agent-X, Hitler 


# You can code in any language of your choice. Input and Output must be in the same format as above


def uncover_hydra(communications, fury):
    # This is a simple graph problem where each agent is a vertex. 
    # We will mark all vertexes that can be reached starting with Fury
    # and whatever is left are the HYDRA agents
    messages = dict()
    
    for cmnt in communications:
        _parse_communication(cmnt, messages)
        
    return _find_hydra_agents(messages, fury)
    

def _parse_communication(cmnt, messages):
    msg = cmnt.split(':')
    sender = msg[0].strip()
    receivers = [ receiver.strip() for receiver in msg[1].split(',')]
    
    # An adjacent list to be further used on the vertex navigation
    messages[sender] = receivers    


def _find_hydra_agents(agents_msg, fury):
    hydra, shield_agents, agents = set(), set(), [fury]
    
    while len(agents) > 0:
        # We get the next agent from the unvisited SHIELD agent set,
        # add him to the SHIELD list and then add all agents
        # this agent sent a message to to the unvisited SHIELD agent set.
        # We do this until there are no more SHIELD agents to visit.
        current = agents.pop()
        shield_agents.add(current)
        
        if current in agents_msg:
            for agent in agents_msg[current]:
                if agent not in shield_agents:
                    agents.append(agent)
    
    # We look for all agents in all communications and grab the ones
    # not in the SHIELD set.
    for sender in agents_msg.keys():
        if sender not in shield_agents:
            hydra.add(sender)
            
        for receiver in agents_msg[sender]:
            if receiver not in shield_agents:
                hydra.add(receiver) 
                
    return hydra
    
    
communication = [ "Nick Fury : Tony Stark, Maria Hill, Norman Osborn", 
                  "Hulk : Tony Stark, HawkEye, Rogers",
                  "Rogers : Thor",
                  "Tony Stark: Pepper Potts, Nick Fury", 
                  "Agent 13 : Agent-X, Nick Fury, Hitler", 
                  "Thor: HawkEye, BlackWidow", 
                  "BlackWidow:Hawkeye", 
                  "Maria Hill : Hulk, Rogers, Nick Fury", 
                  "Agent-X : Agent 13, Rogers", 
                  "Norman Osborn: Tony Stark, Thor" ]
                  
print uncover_hydra(communication, "Nick Fury")
                        
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        