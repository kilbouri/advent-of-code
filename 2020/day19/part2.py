from os.path import dirname
import re


def parseIndex(rule: str):
    idxRegex = re.search(r"(\d+): ", rule)
    index = int(idxRegex.groups()[0])

    rule = rule[idxRegex.span()[1]:]

    return (index, rule)


def parsePattern(pattern: str, idxToPat: dict):
    # this is an utterly sinful solution, but what if we just use the + modifier when a function calls itself?

    # check 1: is this a final substring?
    regex = re.search(r"\"(.*?)\"", pattern)

    if regex:
        return regex.groups()[0]  # return the single character

    # check 2: is this a logical or?
    regex = re.search(r"(.*) \| (.*)", pattern)
    if regex:
        pattern1 = regex.groups()[0]
        pattern2 = regex.groups()[1]

        if pattern == "42 | 42 8":
            return "(?:(?:" + parsePattern(idxToPat[42], idxToPat) + ")+)"

        elif pattern == "42 31 | 42 11 31":
            return "(?:X)"

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


def checkMessage(message: str, rString: str, idxToPat: dict) -> bool:
    if "X" in rString:
        ft = "(?:" + parsePattern(idxToPat[42], idxToPat) + ")"
        to = "(?:" + parsePattern(idxToPat[31], idxToPat) + ")"

        for i in range(1, len(message)):
            newRString = rString.replace("X", f"{ft * i}{to * i}")
            result = re.search(r"".join(newRString), message)

            if result:
                span = result.span()
                if len(message) == (span[1] - span[0]):
                    return True
    else:
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

    print("Indexing...")
    for rule in rules:
        idxParsed = parseIndex(rule)
        indexToPattern[idxParsed[0]] = idxParsed[1]

    # update rules as per Part 2 requirements
    indexToPattern[8] = "42 | 42 8"
    indexToPattern[11] = "42 31 | 42 11 31"

    print("Parsing rules...")
    for key in indexToPattern.keys():
        indexToRString[key] = parsePattern(indexToPattern[key], indexToPattern)

    print("Checking messages...")
    matches = 0
    for i, message in enumerate(messages):
        print(f"Checking {i}...")
        if checkMessage(message, indexToRString[0], indexToPattern):
            matches += 1

    print(matches)


if __name__ == "__main__":
    main()
