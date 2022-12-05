from os.path import dirname
from pprint import pprint as print

import re


def parseStacks(stacks: list[str]) -> list[list[str]]:
    """
    Parses stacks like this:
        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3 

    Into a list of stacks like this (first = bottom):
    [
        ['N', 'Z'], 
        ['D', 'C', 'M'], 
        ['P']]
    """
    # Start by prefixing each line with ' '. This will allow us to split the
    # line into chunks of 4 chars, where each is either '    ', '  1 ', or ' [A]'.
    stacks = [' ' + line for line in stacks]
    stacks = [[line[i:i+4] for i in range(0, len(line), 4)] for line in stacks]

    # Transpose the chunks so the list becomes a list of lists of chunks for each stack
    stacks = map(list, zip(*stacks))

    # Now drop the empty sections and the stack numbers from each chunk list
    stacks = [[chunk.strip() for chunk in stack[:-1] if chunk.strip()] for stack in stacks]

    # We now only have letters. Extract letters and we're done.
    return [[chunk[1] for chunk in stack] for stack in stacks]


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        stackSection, instructionsSection = map(str.splitlines, file.read().split('\n\n'))

    stacks = parseStacks(stackSection)

    for line in instructionsSection:
        parse = re.match(r'move (\d+) from (\d+) to (\d+)', line)
        count, source, dest = map(int, parse.groups())

        sourceStack = stacks[source - 1]
        destStack = stacks[dest - 1]

        for _ in range(count):
            popped = sourceStack.pop(0)
            destStack.insert(0, popped)

    print(''.join([stack[0] for stack in stacks]))


if __name__ == "__main__":
    main()
