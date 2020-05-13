from heapq import heappush, heappop

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    current_capital = initialCapital
    capital_min_heap, profit_max_heap = [], []

    for c, idx in enumerate(capital):
        heappush(capital_min_heap, (c, idx))

    for _ in range(numberOfProjects):
        while len(capital_min_heap) and current_capital >= capital_min_heap[0][0]:
            c, idx = heappop(capital_min_heap)
            heappush(profit_max_heap, (-profits[idx]))

        current_capital += -heappop(profit_max_heap)

    return current_capital


def main():

    print("Maximum capital: " + str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print(
        "Maximum capital: "
        + str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0))
    )


main()
