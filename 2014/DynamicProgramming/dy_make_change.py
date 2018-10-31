# Cracking the Code Interview

## problem variation 1
## We can add a DP cache here but maybe it won't help
def change_combinations(amount, max_coin):
    if amount == 0: return [[]]
    if max_coin == 1: return [[1] * amount]

    next_coin = 0
    if max_coin == 25: next_coin = 10
    elif max_coin == 10: next_coin = 5 
    elif max_coin == 5: next_coin = 1 
    
    results = []

    i = 0
    while i * max_coin <= amount:
        current = [max_coin] * i
        sub = change_combinations(amount - i * max_coin, next_coin)

        for s in sub:
            s.extend (current)
            results.append(s)
        i += 1

    return results

## problem variation 2
def count_possible_change(amount, max_coin):
    if amount == 0: return 1 #above level used all of the amount

    next_coin = 0
    if max_coin == 25: next_coin = 10
    elif max_coin == 10: next_coin = 5 
    elif max_coin == 5: next_coin = 1 
    
    if max_coin == 1: return 1

    sum = i = 0
    while i * max_coin <= amount:
        sum += count_possible_change(amount - i * max_coin, next_coin)
        i += 1

    return sum

## problem variation 3
def best_change(amount, coins):
    change = []
    i = 0

    coins.sort(lambda x, y: y - x)

    while amount > 0 and  i < len(coins):
       if amount >= coins[i]:
            change.append(coins[i])
            amount -= coins[i]
       else:
            i += 1
            
    return change


#tests
print count_possible_change(50, 25)
for r in change_combinations(50, 25):
    print r

print best_change(77, [1, 10, 5, 25])





