from os.path import dirname
import re as regex


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        passports = input.read().split("\n\n")

    valid = 0
    for passport in passports:

        # use regex to get each of the attributes in the passport
        # as per the specification. Numbers will need further validation.
        attrs = {
            'ecl': regex.findall(r'\becl:(amb|blu|brn|gry|grn|hzl|oth)\b', passport),
            'pid': regex.findall(r'\bpid:[0-9]{9}\b', passport),
            'hcl': regex.findall(r'\bhcl:#([0-9a-f]{6})\b', passport),
            'eyr': regex.findall(r'\beyr:([0-9]{4})\b', passport),
            'byr': regex.findall(r'\bbyr:([0-9]{4})\b', passport),
            'iyr': regex.findall(r'\biyr:([0-9]{4})\b', passport),
            'hgt': regex.findall(r'\bhgt:(\d+)(cm|in)\b', passport)
        }

        # make sure all 7 checked attributes were found
        attrSum = (len(attrs['ecl']) + len(attrs['pid']) + len(attrs['eyr']) +
                   len(attrs['hcl']) + len(attrs['byr']) + len(attrs['iyr']) + len(attrs['hgt']))

        if attrSum == 7:

            # check the years are within their respective ranges
            if (int(attrs['eyr'][0]) in range(2020, 2031) and
                    int(attrs['byr'][0]) in range(1920, 2003) and
                    int(attrs['iyr'][0]) in range(2010, 2021)):

                # unpack the height attribute and compare quantity range by unit
                amount, unit = attrs['hgt'][0]
                if ((unit == "cm" and int(amount) in range(150, 194)) or
                        (unit == "in" and int(amount) in range(59, 77))):
                    valid += 1

    print(f"There were this many valid: {valid}")


if __name__ == "__main__":
    main()
