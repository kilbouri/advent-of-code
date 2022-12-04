# from os.path import dirname
# import re

# def validateTicket(ticket: list, attrRanges: dict) -> bool:
#     for number in ticket:
#         validNumber = False
#         for key in attrRanges.keys():
#             for rng in attrRanges[key]:
#                 if number in rng:
#                     validNumber = True
#                     break
#             if validNumber:
#                 break

#         if not validNumber:
#             return False
#     return True


# def strToTicket(tickStr: str) -> list:
#     return list(map(int, tickStr.split(",")))


# def checkFieldSet(validTickets: list, fieldSet: list, attrRanges: dict) -> bool:
#     for ticket in validTickets:
#         for i, field in enumerate(fieldSet):
#             validNumber = False
#             for rng in attrRanges[field]:
#                 if ticket[i] in rng:
#                     validNumber = True
#                     break
#             if not validNumber:
#                 return False
#     return True


# def generateArrangement(ticket: list, attrRanges: dict) -> list:
#     result = []
#     for number in ticket:
#         validAttributes = set()
#         for key in attrRanges.keys():
#             for rng in attrRanges[key]:
#                 if number in rng:
#                     validAttributes.add(key)

#         result.append(validAttributes)

#     return result


# def main():
#     with open(f"{dirname(__file__)}/input.txt", "r") as file:
#         file = file.read().split("\n\n")

#     # file indices: 0-ticket pattern   1-your ticket   2-other tickets
#     regRes = re.findall(r"(.*): (\d+-\d+) or (\d+-\d+)", file[0])

#     # contains a string name, and a list of valid ranges
#     intToAttrName = {}
#     attributes = {}
#     for index, result in enumerate(regRes):
#         intToAttrName[index] = result[0]
#         ranges = []
#         for i in range(1, len(result)):
#             spl = result[i].split("-")
#             ranges.append(range(int(spl[0]), int(spl[1]) + 1))
#         attributes[index] = ranges

#     allOtherTickets = list(strToTicket(t) for t in (file[2].split("\n"))[1:])
#     validTickets = list(filter(lambda ticket: validateTicket(
#         ticket, attributes), allOtherTickets))

#     # generate the possible fields for each ticket
#     possibleFields = {}  # contains a list of sets for each index
#     for ticket in validTickets:
#         result = generateArrangement(ticket, attributes)
#         for index, fSet in enumerate(result):
#             # We use set intersection here to reduce pointless checks later on.
#             # Since all tickets must have the same layout of fields, if a given
#             # ticket has a new field (except, of course, the first one generated)
#             # then it's unique to some subset of the valid tickets and therefore
#             # not a valid field label.
#             if index in possibleFields.keys():
#                 possibleFields[index] &= fSet
#             else:
#                 possibleFields[index] = fSet

#     print("Removing guaranteed fields...")
#     removed = True
#     while removed:
#         removed = False
#         for key in possibleFields.keys():
#             if len(possibleFields[key]) == 1:
#                 known = list(possibleFields[key])[0]
#                 for subkey in possibleFields.keys():
#                     if subkey == key:
#                         continue
#                     elif known in possibleFields[subkey]:
#                         newVal = possibleFields[subkey]
#                         newVal.remove(known)
#                         possibleFields[subkey] = newVal
#                         removed = True

#     print()
#     matches = list(filter(lambda arrangement: checkFieldSet(
#         validTickets, arrangement, attributes), possibleArrangements))

#     print("Stringifying the layout...")
#     stringified = []
#     for i in matches[0]:
#         stringified.append(intToAttrName[i])

#     myTicket = list(map(int, file[1].split("\n")[1].split(",")))

#     product = 1
#     for i, field in enumerate(stringified):
#         if "departure" in field:
#             product *= myTicket[i]

#     print(product)


# if __name__ == "__main__":
#     main()


from os.path import dirname
from typing import ValuesView
from ticket import Ticket
import re
from pprint import pprint


def strToIntSequence(tickStr: str):
    a = map(int, tickStr.strip().split(","))
    return a


def isValidTicket(ticket: list[int], validTicket: Ticket) -> bool:
    for value in ticket:
        if not validTicket.isValidValue(value):
            return False
    return True


def removeUnique(index: int, label: str, labelList: list[set]):
    for i, lSet in enumerate(labelList):
        if i != index and label in lSet:
            lSet.remove(label)
            if len(lSet) == 1:
                removeUnique(i, list(lSet)[0], labelList)
    pass


def main():
    # open the file, split into blocks: <fields>, <your ticket>, <other tickets>
    with open(f"{dirname(__file__)}/input.txt") as file:
        file = file.read().strip().split("\n\n")

        allFields = re.findall(r"(.*): (\d+-\d+) or (\d+-\d+)", file[0])
        yourTicket = file[1].splitlines()[1]
        otherTickets = file[2].splitlines()[1:]

    validTicket = Ticket()

    # fill the ticket with all the fields and ranges in the input
    for field in allFields:
        validTicket.addFieldRange(field[0], [field[1], field[2]])

    # list of all valid tickets (just tuples of values that appear on the ticket)
    validTickets = [
        tuple(strToIntSequence(line))
        for line in map(str.strip, otherTickets)
        if isValidTicket(strToIntSequence(line), validTicket)
    ]

    # a list of sets of the possible labels for each field
    fieldList = [validTicket.getFields().copy()
                 for _ in range(len(validTickets[0]))]

    # find the arrangement of labels for the tickets
    for i, fieldSet in enumerate(fieldList):
        fieldsToRemove = set()
        for field in fieldSet:
            for ticket in validTickets:
                if not validTicket.isValidForField(field, ticket[i]):
                    fieldsToRemove.add(field)
                    break

        fieldSet -= fieldsToRemove
        if len(fieldSet) == 1:
            removeUnique(i, list(fieldSet)[0], fieldList)

    fieldList = [list(item)[0] for item in fieldList]

    # calculate ticket score
    score = 1
    for label, value in zip(fieldList, strToIntSequence(yourTicket)):
        if label.startswith("departure"):
            score *= value

    print(f"Product of departure fields: {score}")


if __name__ == "__main__":
    main()  # ans: 314360510573
