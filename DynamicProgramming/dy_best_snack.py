# http://www.careercup.com/question?id=5736766531174400

from collections import deque
import sys

class SnackFinder(object):
    def __init__(self):
        self.min_price = sys.maxint
        self.selected = []

    def best_snack(self, combos, itens):
        self.min_price = sys.maxint
        self.selected = []
        self._best_snack(combos, itens, 0, [])
        return self.selected

    def _best_snack(self, combos, itens, price_so_far, choice):
        if len(itens) == 0:
            if price_so_far < self.min_price:
                self.selected = []
                self.selected.extend(choice)
                self.min_price = price_so_far
            return;

        for combo in combos:
            common = itens.intersection(combo[2])
            if len(common) > 0:
                new_itens = {x for x in itens if x not in common}
                choice.append(combo)
                self._best_snack(combos, new_itens, price_so_far + combo[1], choice)
                choice.pop()

###############################
# Needs cache?
def best_snack(combos, itens):
    if len(itens) == 0: return (0, [])

    current_min = (sys.maxint, [])

    for combo in combos:
        common = itens.intersection(combo[2])
        if len(common) > 0:
            new_itens = {x for x in itens if x not in common}
            tmp_min, choices = best_snack(combos, new_itens)
            if tmp_min + combo[1] < current_min[0]:
                choices.append(combo)
                current_min = (tmp_min + combo[1], choices)

    return current_min


combos = [(1, 5, {"Burguer"}), (2, 4, {"French_Fries"}), (3, 8, {"Colddrink"}), (4, 12, {"Burguer", "French_Fries", "Colddrink"}), (5, 14, {"Burguer", "Colddrink"})]

finder = SnackFinder()
print finder.best_snack(combos, {"Burguer", "French_Fries"})
print best_snack(combos, {"Burguer", "French_Fries"})
