# EggDrop

import sys

def egg_drop(eggs, floors, cache):
    if floors == 0 or floors == 1: return floors
    if eggs == 1: return floors

    if cache.has_key((eggs, floors)): return cache[(eggs, floors)]

    min_drops = sys.maxint

    for i in range(1, floors + 1):
        c = max(egg_drop(eggs - 1, i - 1, cache), egg_drop(eggs, floors - i, cache))
        if c < min_drops:
            min_drops = c

    cache[(eggs, floors)] = min_drops + 1
    return cache[(eggs, floors)]

print egg_drop(2, 100, dict())