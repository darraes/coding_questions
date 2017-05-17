# Cracking the Code Interview
# http://www.careercup.com/question?id=5765784060035072

from collections import deque

def nth_uggly_number(n):
    if n <= 0: raise "Invalid n"
    uggly = [1]
    q2 = deque()
    q3 = deque()
    q5 = deque()

    q2.append(2)
    q3.append(3)
    q5.append(5)

    for i in range(1, n):
        i_uggly = min(q2[0], q3[0], q5[0])

        if i_uggly == q2[0]:
            q2.popleft() 
            q2.append(i_uggly*2)
            q3.append(i_uggly*3)
            q5.append(i_uggly*5)  
        if i_uggly == q3[0]:
            q3.popleft() 
            q3.append(i_uggly*3)
            q5.append(i_uggly*5)
        if i_uggly == q5[0]:
            q5.popleft() 
            q5.append(i_uggly*5)

        uggly.append(i_uggly)

    print uggly
   
nth_uggly_number(50)