from os.path import dirname
from pprint import pprint as print

import re

DIR_FILES_SIZE_KEY = '__filesSize'
DIR_NAME_KEY = '__dirname'
TOTAL_DIR_SIZE_KEY = '__totalSize'

NON_CHILD_DIR_KEYS = ['..', DIR_NAME_KEY, DIR_FILES_SIZE_KEY, TOTAL_DIR_SIZE_KEY]


def parseFs(input: str):
    commandsWithOutput = input.split('$ ')[1:]  # first is an empty string

    # heh unix go brrrrr
    def makeDir(name, parent=None, size=0): return {
        '..': parent,
        DIR_NAME_KEY: name,
        DIR_FILES_SIZE_KEY: 0,
        DIR_FILES_SIZE_KEY: size
    }

    root = makeDir('/')
    fsDir = root

    for command, *output in map(str.splitlines, commandsWithOutput[1:]):  # first command is to move to root, we're already there
        match command.split():
            case ['cd', target]:
                fsDir = fsDir[target]

            case ['ls']:
                # this is a chonker so I made it a function to shorten the list-comps below
                def getData(pattern, string): return re.match(pattern, string).groups()[0]

                dirs = [getData(r'dir ([^\n]+)', line) for line in output if line.startswith('dir')]
                fileSizes = [getData(r'^(\d+)', line) for line in output if not line.startswith('dir')]

                fsDir[DIR_FILES_SIZE_KEY] = sum(map(int, fileSizes))
                fsDir.update([(dir, makeDir(dir, fsDir)) for dir in dirs])

    return root


def childDirs(folder: dict):
    return [folder[key] for key in folder.keys() if key not in NON_CHILD_DIR_KEYS]


def totalFolderSize(folder: dict):
    """
    Computes and returns the total size of all children in the provided folder.
    ! IMPORTANT: the folder WILL BE MUTATED to contain a memoized total folder size key
    """
    # use memoized value if we have it
    if TOTAL_DIR_SIZE_KEY in folder:
        return folder[TOTAL_DIR_SIZE_KEY]

    childrenSize = sum([totalFolderSize(dir) for dir in childDirs(folder)])
    totalSize = folder[DIR_FILES_SIZE_KEY] + childrenSize

    folder[TOTAL_DIR_SIZE_KEY] = totalSize  # memoize for future calls

    return totalSize


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        log = file.read()

    fs = parseFs(log)

    def traverse(root: dict):
        mySize = totalFolderSize(root)
        myEffectiveSize = mySize if mySize <= 100_000 else 0

        return myEffectiveSize + sum([traverse(dir) for dir in childDirs(root)])

    print(traverse(fs))


if __name__ == "__main__":
    main()
