# http://www.careercup.com/question?id=5106757177180160

def reverse(str, start, end):
    if start >= end: return
    while start < end:
        tmp = str[start]
        str[start] = str[end - 1]
        str[end - 1] = tmp

        start += 1
        end -= 1

def reverse_words(str):
    start = end = 0

    while True:
        while start < len(str) and str[start] == ' ':
            start += 1

        end = start
        while end < len(str) and str[end] != ' ':
            end += 1

        reverse(str, start, end)
        if end == len(str): break

        start = end

    return str

print "".join(reverse_words(list("the boy ran")))
print "".join(reverse_words(list("the boy ran   some timesagain")))
print "".join(reverse_words(list("the boy    fell")))
