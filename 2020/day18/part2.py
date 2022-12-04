from os.path import dirname
import re


def indexReplace(source: str, replaceWith: str, start: int, end: int) -> str:
    return str(source)[:start] + str(replaceWith) + str(source)[end:]


def findBrackets(expr: str) -> tuple:
    regex = re.search(r"\(([\d \*\+]*)\)", str(expr))

    if regex is None:
        return None
    else:
        start = regex.span()[0]
        end = regex.span()[1]
        match = regex.group()[1:-1]

        return ((start, end), match)


def findOperation(expr: str) -> tuple:
    regex = re.search(r"(\d+) (\+) (\d+)", str(expr))

    if not regex:
        # if no additions were found, find multiplication
        regex = re.search(r"(\d+) (\*) (\d+)", str(expr))

    if not regex:
        # if neither addition nor multiplication were found, return None
        return None

    start = regex.span()[0]
    end = regex.span()[1]
    operandA = regex.groups()[0]
    operation = regex.groups()[1]
    operandB = regex.groups()[2]

    return ((start, end), operandA, operation, operandB)


def evaluateExpression(expr: str):
    newExpression = expr
    brackets = findBrackets(expr)
    if brackets:
        indices = brackets[0]
        newSubstring = evaluateExpression(brackets[1])

        newExpression = indexReplace(
            newExpression, newSubstring, indices[0], indices[1])
        return evaluateExpression(newExpression)
    else:
        operation = findOperation(expr)
        if operation:
            indices = operation[0]

            operandA = int(operation[1])
            operandB = int(operation[3])

            newSubstring = ""

            if operation[2] == "+":
                newSubstring = str(operandA + operandB)
            elif operation[2] == "*":
                newSubstring = str(operandA * operandB)

            newExpression = indexReplace(
                newExpression, newSubstring, indices[0], indices[1])
            return evaluateExpression(newExpression)

        else:
            return int(expr)


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        expressions = file.read().split("\n")

    total = 0
    for expression in expressions:
        result = evaluateExpression(expression)
        total += result

    print("Total: " + str(total))


if __name__ == "__main__":
    main()
