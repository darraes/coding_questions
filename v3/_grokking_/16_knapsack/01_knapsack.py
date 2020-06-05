def solve_knapsack(profits, weights, capacity):
    return solve_knapsack_impl({}, 0, profits, weights, capacity)


def solve_knapsack_impl(memo, idx, profits, weights, capacity):
    if capacity == 0 or idx == len(weights):
        return 0

    if (idx, capacity) in memo:
        return memo[(idx, capacity)]

    # not using current weight
    max_profit = solve_knapsack_impl(memo, idx + 1, profits, weights, capacity)

    if weights[idx] <= capacity:
        max_profit = max(
            max_profit,
            profits[idx]
            + solve_knapsack_impl(
                memo, idx + 1, profits, weights, capacity - weights[idx]
            ),
        )

    memo[(idx, capacity)] = max_profit
    return max_profit


def main():
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))
    print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))


main()
