from os import getcwd


def minCost(costGrid, target):
    m, n = target

    # this could be rewritten to use the cost grid itself, but
    # I'm lazy. So, I'm not gonna do it.

    totalCost = [[0] * len(costGrid[0]) for _ in range(len(costGrid))]
    totalCost[0][0] = 0

    # Initialize first column of total cost
    for i in range(1, m+1):
        totalCost[i][0] = totalCost[i-1][0] + costGrid[i][0]

    # Initialize first row of total cost
    for j in range(1, n+1):
        totalCost[0][j] = totalCost[0][j-1] + costGrid[0][j]

    # Construct rest of the total cost list
    for i in range(1, m+1):
        for j in range(1, n+1):
            costs = [totalCost[i-1][j], totalCost[i][j-1]]
            totalCost[i][j] = min(costs) + costGrid[i][j]

    return totalCost[m][n]


def main():
    with open(f"{getcwd()}/2021/day15/input.txt") as file:
        file = file.readlines()

        weights = [[int(w) for w in line.strip()] for line in file]

    lowestRisk = minCost(weights, (len(weights[0]) - 1, len(weights) - 1))
    print(f"The lowest risk path has a risk of {lowestRisk}")

    pass


if __name__ == "__main__":
    main()
