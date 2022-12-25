from os.path import dirname


def main():
    with open(f'{dirname(__file__)}/input.txt', 'r') as file:
        snafuNumbers = file.read().splitlines()

    def snafuToBaseTen(snafu: str or list[str]):
        digits = reversed(snafu)

        coefficient = 1
        total = 0

        for digit in digits:
            total += ("=-012".find(digit) - 2) * coefficient
            coefficient *= 5

        return total

    def baseTenToSnafu(base10: int):
        result = []

        while base10 != 0:
            remainder = base10 % 5
            base10 //= 5

            if remainder <= 2:
                result += str(remainder)
            else:
                result.append("=-"[remainder - 3])
                base10 += 1

        return ''.join(reversed(result))

    fuelRequired = sum(snafuToBaseTen(snafu) for snafu in snafuNumbers)
    print(baseTenToSnafu(fuelRequired))


if __name__ == "__main__":
    main()
