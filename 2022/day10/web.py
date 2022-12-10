#!/usr/bin/python3
import sys
from collections import defaultdict
from os.path import dirname

with open(f'{dirname(__file__)}/input.txt', 'r') as file:
    lines = file.read().splitlines()


screen = [['?' for _ in range(40)] for _ in range(6)]
p1 = 0
x = 1
clock = 0


def handle_tick(t, x):
    global p1
    global screen
    t1 = t-1
    screen[t1//40][t1 % 40] = ('#' if abs(x-(t1 % 40)) <= 1 else ' ')
    if t in [20, 60, 100, 140, 180, 220]:
        p1 += x*t


for line in lines:
    words = line.split()
    if words[0] == 'noop':
        clock += 1
        handle_tick(clock, x)
    elif words[0] == 'addx':
        clock += 1
        handle_tick(clock, x)
        clock += 1
        handle_tick(clock, x)
        x += int(words[1])
print(p1)
for r in range(6):
    print(''.join(screen[r]))
