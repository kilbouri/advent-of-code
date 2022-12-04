from os.path import dirname
import re as regex


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as input:
        passports = input.read().split("\n\n")

    valid = 0
    for passport in passports:
        attrs = {
            'ecl': len(regex.findall(r'ecl:', passport)),
            'pid': len(regex.findall(r'pid:', passport)),
            'eyr': len(regex.findall(r'eyr:', passport)),
            'hcl': len(regex.findall(r'hcl:', passport)),
            'byr': len(regex.findall(r'byr:', passport)),
            'iyr': len(regex.findall(r'iyr:', passport)),
            'cid': len(regex.findall(r'cid:', passport)),
            'hgt': len(regex.findall(r'hgt:', passport))
        }

        attrSum = (attrs['ecl'] + attrs['pid'] + attrs['eyr'] +
                   attrs['hcl'] + attrs['byr'] + attrs['iyr'] +
                   attrs['cid'] + attrs['hgt'])

        if (attrSum == 8):
            valid += 1
        elif (attrSum == 7 and attrs['cid'] == 0):
            valid += 1

    print("There were this many valid: " + str(valid))


if __name__ == "__main__":
    main()
