from collections import defaultdict, deque
from email.policy import default
from os.path import dirname
from pprint import pprint

import re


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    def parseValveRateTunnels(text):
        pattern = r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? ([^\n]+)'
        valve, rate, tunnels = re.match(pattern, text).groups()

        return (valve, int(rate), tunnels.split(', '))

    valves = [parseValveRateTunnels(line) for line in lines]

    usefulValves = [name for name, flowRate, _ in valves if flowRate > 0]
    usefulIndices = {name: i for i, name in enumerate(usefulValves)}

    # Decompose valves into a pair of dictionaries cuz we're gonna do a lot of
    # lookups by valve name
    adjacent = dict()
    flowRate = dict()

    for valve, rate, connected in valves:
        flowRate[valve] = rate
        adjacent[valve] = connected

    maxFlowRate = sum(flowRate.values())

    TIME_LIMIT = 30

    limOpenValveFlags = 2**len(usefulValves)

    def isUsefulValveOpen(flags, valveId):
        return (flags >> usefulIndices[valveId] & 1) == 1

    def getUsefulValveBitFlag(valveId):
        return 1 << usefulIndices[valveId]

    # dp[time][open valves][current position] = resulting flow
    dp = [[defaultdict(lambda: -1) for _ in range(limOpenValveFlags)] for _ in range(TIME_LIMIT + 1)]

    # Initial condition
    dp[0][0]["AA"] = 0

    best = 0

    for time in range(TIME_LIMIT):
        print(f'{time=}')

        nextTime = time + 1
        timeLeftAfterOpening = TIME_LIMIT - time - 1

        for openValveFlags in range(limOpenValveFlags):
            for myPosition, resultingFlow in dp[time][openValveFlags].items():
                # Prune this branch of processing if, even with max flow rate for the rest of
                # the time, we don't beat our best (or we match it, since we don't care about multiple best paths)
                if maxFlowRate * timeLeftAfterOpening + resultingFlow <= best:
                    continue

                best = max(best, resultingFlow)

                if myPosition in usefulIndices and not isUsefulValveOpen(openValveFlags, myPosition):
                    valveOpenedFlags = openValveFlags | getUsefulValveBitFlag(myPosition)
                    dp[nextTime][valveOpenedFlags][myPosition] = timeLeftAfterOpening * flowRate[myPosition] + resultingFlow

                for nextValve in adjacent[myPosition]:
                    if dp[nextTime][openValveFlags][nextValve] < resultingFlow:
                        dp[nextTime][openValveFlags][nextValve] = resultingFlow

    print(best)


if __name__ == "__main__":
    main()
