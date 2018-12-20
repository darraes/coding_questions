# http://www.careercup.com/question?id=5721462438625280

# Finding function returns a tuple with 4 values 
#Tuple[0] = parent of node 1
#Tuple[1] = lefr or right for node 1
#Tuple[2] = parent of node 2
#Tuple[3] = lefr or right for node 1

#For error detection, we can NOT look for a node in the subtrees of the other node. 
#With that in mind, if the search function only returns 1 node, it means that the other
#was a child and therefore no valid swap exists

#After that, it is just a pointer swap if both nodes were found. 
#This is O(N) time and O(1) space