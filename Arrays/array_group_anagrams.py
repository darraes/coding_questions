# http://www.careercup.com/question?id=5733320654585856

def is_anagram(w1, w2):
    return sorted(w1) == sorted(w2)

# Not so good. We can just hash the sorted values and use a hash table to
# keep count
def anagram_buckets(words):
    buckets = []
    buckets.append([words[0]])

    for i in range(1, len(words)):
        newBucket = True
        for bucket in buckets:
            if (is_anagram(words[i], bucket[0])):
                bucket.append(words[i])
                newBucket = False
                break
        if newBucket:
             buckets.append([words[i]])
    return buckets
    

print anagram_buckets(["dap", "pad", "banjo", "joban", "daniel"])