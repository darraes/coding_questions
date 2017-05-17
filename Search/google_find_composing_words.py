# Craking the Code Interview - 18.7

#Asked by Google

# Given the domain of an URL and a dictionary, find all possible combinations of words
# from the dictionary find all possible combinations of words user to form the domain

def words2(grammar, word, start, cache):
    if start == len(word): return [[]]
    if cache.has_key(start): return cache[start]

    result = []
    for i in range(start, len(word) + 1):
        token = word[start:i]
        if token in grammar:
            dp_result = words2(grammar, word, i, cache)
            if dp_result and len(dp_result) > 0:
                for phrase in dp_result:
                    buffer = phrase[:]
                    buffer.append(token)
                    result.append(buffer)
    cache[start] = result
    return cache[start]

print words2({"cat", "cats", "and", "dogs", "sand"}, "catsanddogs", 0, dict())
print words2({"cat", "cats", "and", "dogs", "sand"}, "catsan", 0, dict())

