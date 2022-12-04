from os.path import dirname
import re


def parseIndex(rule: str):
    idxRegex = re.search(r"(\d+): ", rule)
    index = int(idxRegex.groups()[0])

    rule = rule[idxRegex.span()[1]:]

    return (index, rule)


def parsePattern(pattern: str, idxToPat: dict):
    # check 1: is this a final substring?
    regex = re.search(r"\"(.*?)\"", pattern)

    if regex:
        return regex.groups()[0]  # return the single character

    # check 2: is this a logical or?
    regex = re.search(r"(.*) \| (.*)", pattern)
    if regex:
        pattern1 = regex.groups()[0]
        pattern2 = regex.groups()[1]

        return f"(?:{parsePattern(pattern1, idxToPat)}|{parsePattern(pattern2, idxToPat)})"

    # check 3: is this a list of numbers?
    regex = re.search(r"([\d ]*)", pattern)
    if regex:
        numbers = list(map(int, regex.groups()[0].split(" ")))

        retVal = "(?:"

        for number in numbers:
            retVal += parsePattern(idxToPat[number], idxToPat)

        return retVal + ")"
    else:
        return None


def checkMessage(message: str, rString: str) -> bool:
    result = re.search(r"".join(rString), message)

    if result:
        span = result.span()
        return len(message) == (span[1] - span[0])

    return False


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        part = file.read().split("\n\n")

    rules = part[0].split("\n")
    messages = part[1].split("\n")

    indexToPattern = {}
    indexToRString = {}

    for rule in rules:
        idxParsed = parseIndex(rule)
        indexToPattern[idxParsed[0]] = idxParsed[1]

    for key in indexToPattern.keys():
        indexToRString[key] = parsePattern(indexToPattern[key], indexToPattern)

    matches = 0
    for message in messages:
        if checkMessage(message, indexToRString[0]):
            matches += 1

    print(matches)


if __name__ == "__main__":
    main()
