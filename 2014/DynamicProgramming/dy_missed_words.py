#Cracking the code Interview - Moderate

import sys

def solve(str, start, words, max_word_length, cache):
    if str is None or len(str) == 0 or start >= len(str): return (0, [])
    
    if cache.has_key(start): return cache[start]
    else:
        min_miss, level_phrase = (sys.maxint, [])
        end = start + 1
        while end <= min(start + max_word_length, len(str)):
            current_token = str[start:end]
            miss_sub, phrase = solve(str, end, words, max_word_length, cache)
            
            curr_miss, curr_phrase = (0, [])
            curr_phrase.extend(phrase)
            if current_token in words:
                curr_phrase.append(current_token)
                curr_miss, curr_phrase = (miss_sub, curr_phrase)
            else:
                curr_phrase.append(current_token.upper())
                curr_miss, curr_phrase = (miss_sub + 1, curr_phrase)
            
            if (curr_miss < min_miss):
                min_miss, level_phrase = (curr_miss, curr_phrase)

            end += 1
        
        if len(level_phrase) > 0:
            cache[start] = (min_miss, level_phrase)

        return (min_miss, level_phrase)

words = set(["looked", "just", "like", "her", "brother"])
print solve("jesslookedjustliketimherbrother", 0, words, 7, dict())
    
    
        