# http://www.careercup.com/question?id=5705619461898240

#we could add a cache using the index as key to avoid recalculations
def count_mapping(input, index, cache):
    if index >= len(input) - 1: return 1
    if cache.has_key(index): return cache[index]

    count = count_mapping(input, index + 1, cache);

    if index + 2 <= len(input) and int(input[index:(index + 2)]) <= 26:
        count = count + count_mapping(input, index + 2, cache);

    cache[index] = count
    return count;

print count_mapping("1231224", 0, dict())