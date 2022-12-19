from functools import reduce
from os.path import dirname
from collections import deque
import re
from timeit import timeit


def maximizeGeodes(costOre, costClay, costObsidianOre, costObsidianClay, costGeodeOre, costGeodeObsidian, numMinutes):
    best = 0

    # state is (ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, timeRemaining)
    queue = deque([(0, 0, 0, 0, 1, 0, 0, 0, numMinutes)])
    visited = set()

    while queue:
        ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, timeRemaining = queue.pop()

        best = max(best, geodes)

        if timeRemaining == 0:
            continue

        maxOrePerMinuteRequired = max(costOre, costClay, costObsidianOre, costGeodeOre)

        maxOreNeededNow = timeRemaining * maxOrePerMinuteRequired - oreRobots * (timeRemaining - 1)
        ore = min(ore, maxOreNeededNow)

        maxClayNeededNow = timeRemaining * costObsidianClay - clayRobots * (timeRemaining - 1)
        clay = min(clay, maxClayNeededNow)

        maxObsidianNeededNow = timeRemaining * costGeodeObsidian - obsidianRobots * (timeRemaining - 1)
        obsidian = min(obsidian, maxObsidianNeededNow)

        # prevent checking states we've already seen
        newState = (ore, clay, obsidian, geodes, oreRobots, clayRobots, obsidianRobots, geodeRobots, timeRemaining)
        if newState not in visited:
            visited.add(newState)
        else:
            continue

        # explore doing nothing for the next minute
        queue.append((ore + oreRobots, clay + clayRobots, obsidian + obsidianRobots,
                      geodes + geodeRobots, oreRobots, clayRobots, obsidianRobots, geodeRobots, timeRemaining - 1))

        # Use selective exploration based on number of robots and resource requirements.
        # There is no reason to create more of a given type of robot than we could possibly use of its resources
        # per minute (except geode robots, as many of them as possible please :D)

        if ore >= costOre and maxOrePerMinuteRequired > oreRobots:  # try buying ore robot
            queue.append((ore - costOre + oreRobots, clay + clayRobots, obsidian + obsidianRobots,
                          geodes + geodeRobots, oreRobots + 1, clayRobots, obsidianRobots, geodeRobots, timeRemaining - 1))

        if ore >= costClay and costObsidianClay > clayRobots:  # try buying clay robot
            queue.append((ore - costClay + oreRobots, clay + clayRobots, obsidian + obsidianRobots,
                          geodes + geodeRobots, oreRobots, clayRobots + 1, obsidianRobots, geodeRobots, timeRemaining - 1))

        if ore >= costObsidianOre and clay >= costObsidianClay and costGeodeObsidian > obsidianRobots:  # try buying obsidian
            queue.append((ore - costObsidianOre + oreRobots, clay - costObsidianClay + clayRobots, obsidian + obsidianRobots,
                          geodes + geodeRobots, oreRobots, clayRobots, obsidianRobots + 1, geodeRobots, timeRemaining - 1))

        if ore >= costGeodeOre and obsidian >= costGeodeObsidian:  # try buying geode robot
            queue.append((ore - costGeodeOre + oreRobots, clay + clayRobots, obsidian - costGeodeObsidian + obsidianRobots,
                          geodes + geodeRobots, oreRobots, clayRobots, obsidianRobots, geodeRobots + 1, timeRemaining - 1))

    return best


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        lines = file.read().splitlines()

    def parseBlueprint(text):
        numbers = re.findall(r'\d+', text)

        id, oreCost, clayCost, obsidianOreCost, obsidianClayCost, geodeOreCost, geodeObsidianCost = map(int, numbers)
        return (id, oreCost, clayCost, obsidianOreCost, obsidianClayCost, geodeOreCost, geodeObsidianCost)

    TIME_LIMIT = 32

    blueprints = [parseBlueprint(line) for line in lines]
    maxGeodes = [maximizeGeodes(*costs, TIME_LIMIT) for _, *costs in blueprints[:3]]

    print(reduce(lambda a, b: a * b, maxGeodes))


if __name__ == "__main__":
    print(timeit(main, number=1))
