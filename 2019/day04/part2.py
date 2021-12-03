input = (138241, 674034)  # range of values the password can be in


def checkPassword(password: str):
    doubles = set()
    lastNumber = -1
    repeats = 1

    for num in password:
        if int(num) > lastNumber:
            repeats = 1
            lastNumber = int(num)
            continue

        elif int(num) == lastNumber and repeats == 1:
            doubles.add(int(num))
            repeats += 1
            continue

        elif int(num) == lastNumber and repeats != 1:
            if int(num) in doubles:
                doubles.remove(int(num))
            repeats += 1
            continue

        elif int(num) < lastNumber:
            return False

    return len(doubles) > 0


def main():
    min, max = input
    validPasses = set()
    print("Thinking...")
    for password in range(min, max + 1):
        if checkPassword(str(password)) is True:
            validPasses.add(password)

    print(f"There were {len(validPasses)} valid passcodes in the range.")


if __name__ == "__main__":
    main()
