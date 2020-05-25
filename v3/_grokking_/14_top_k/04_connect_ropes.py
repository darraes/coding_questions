from heapq import *

def minimum_cost_to_connect_ropes(ropeLengths):
    result = 0
    heap = []
    
    for l in ropeLengths:
        heappush(heap, l)

    while len(heap) > 1:
        cost = heappop(heap) + heappop(heap)
        result += cost
        heappush(heap, cost)

    return result


def main():

    print(
        "Minimum cost to connect ropes: "
        + str(minimum_cost_to_connect_ropes([1, 3, 11, 5]))
    )
    print(
        "Minimum cost to connect ropes: "
        + str(minimum_cost_to_connect_ropes([3, 4, 5, 6]))
    )
    print(
        "Minimum cost to connect ropes: "
        + str(minimum_cost_to_connect_ropes([1, 3, 11, 5, 2]))
    )


main()
