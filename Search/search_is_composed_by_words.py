# http://www.careercup.com/question?id=5705581721550848

def is_composed(words, full_word, start):
    if start == len(full_word): return True

    end = start + 1
    while end <= len(full_word):
        token = full_word[start:end]
        if token in words:
            rest = is_composed(words, full_word, end)
            if rest: return True
        end += 1

    return False

words = ["world", "hello", "super", "hell"]
print is_composed(words, "helloworld", 0)
print is_composed(words, "superman", 0)
print is_composed(words, "hellohello", 0)
