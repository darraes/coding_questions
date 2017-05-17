from collections import deque

# Bottom up DP solution
def is_valid(str):
    if len(str) == 0 or len(str) > 3: return False
    if str[0] == '0': return False
    else:
        p = int(str)
        return p >=1 and p <= 255

#Needs the cache
def _find_ips(str, parts, index):
    if parts == 0: raise
    elif parts == 1:
        if is_valid(str[index:]):
            return [str[index:]]
        else:
            return []
    else:
        result = []
        for end in range(index + 1, max(index + 4, len(str))):
            part = str[index:end]
            if is_valid(part):
                tails = _find_ips(str, parts - 1, end)
                for tail in tails:
                    result.append(part + "." + tail)
        return result

print _find_ips("102556178", 4, 0)


#Solution propagation (Top-Down)
def ips_internal(str, index, parts):
    if len(str) < 4: raise

    if len(parts) == 3:
        if len(str) - index <= 3:
            parts.append(str[index:])
            print parts
            parts.pop()
    else:
        for i in range(index + 1, min(index + 4, len(str))):
            parts.append(str[index:i])
            ips_internal(str, i, parts)
            parts.pop()

