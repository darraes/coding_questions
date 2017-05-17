# http://www.careercup.com/question?id=6234634354425856

def paren(left, right, string):
    if(left == 0 and right == 0):
        print string
    if(left > right):
        return
    if (left > 0):
        paren(left-1, right, string + "(")
    if (right > 0):
        paren(left, right-1, string + ")")

def parentheses(n):
    paren(n,n,"")

parentheses(6)