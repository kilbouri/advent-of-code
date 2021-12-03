from os import getcwd
import math


def main():
    with open(f"{getcwd()}/2020/day13/input.txt", "r") as file:
        file = file.readlines()

    myDepTime = int(file[0])

    busses = list(file[1].split(","))
    busToWait = {}
    for bus in busses:
        if bus == "x":
            continue

        freq = int(bus)
        busToWait[freq] = freq * math.ceil(myDepTime / freq) - myDepTime

    print(busToWait)

    # find lowest wait
    lowestKey = None
    for key in busToWait.keys():
        if lowestKey is None:
            lowestKey = key
        elif busToWait[key] < busToWait[lowestKey]:
            lowestKey = key

    print(lowestKey * busToWait[lowestKey])


if __name__ == "__main__":
    main()
