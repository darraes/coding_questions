# http://www.careercup.com/question?id=5680043955060736

def print_ordered(str, n):
    if (str != "" and int(str) > n): return
    if str == "0":
        print str
        return;

    if str != "":
        print str
    for i in range(10):
        new_str = "{}{}".format(str, i)        
        print_ordered(new_str, n)

print_ordered("", 25)