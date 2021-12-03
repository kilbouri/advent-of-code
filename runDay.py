#!/usr/bin/env python3

from os import getcwd, system
from sys import argv

if len(argv) != 4:
    print("Invalid number of arguments.")
    print("   Usage: ./runDay <year: int> <day: int> <part: int>")
    exit()

cwd = getcwd()
year = argv[1]
day = argv[2]
part = argv[3]

command = f"python3 {cwd}/{year}/day{day.zfill(2)}/part{part}.py"
system(command)
