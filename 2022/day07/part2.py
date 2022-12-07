from os.path import dirname
from pprint import pprint as print

import re


DIR_FILES_SIZE_KEY = '__filesSize'
DIR_NAME_KEY = '__dirname'
TOTAL_DIR_SIZE_KEY = '__totalSize'

NON_CHILD_DIR_KEYS = ['..', DIR_NAME_KEY, DIR_FILES_SIZE_KEY, TOTAL_DIR_SIZE_KEY]


def childDirs(folder: dict):
    return [folder[key] for key in folder.keys() if key not in NON_CHILD_DIR_KEYS]


def totalFolderSize(folder: dict):
    """
    Computes and returns the total size of all children in the provided folder.

    ! IMPORTANT: the folder WILL BE MUTATED to contain a memoized total folder size key,
    ! TOTAL_DIR_SIZE_KEY, to avoid repeating work!
    """
    # use memoized value if we have it
    if TOTAL_DIR_SIZE_KEY in folder:
        return folder[TOTAL_DIR_SIZE_KEY]

    childrenSize = sum([totalFolderSize(dir) for dir in childDirs(folder)])
    totalSize = folder[DIR_FILES_SIZE_KEY] + childrenSize

    folder[TOTAL_DIR_SIZE_KEY] = totalSize  # memoize for future calls
    return totalSize


def parseFs(input: str):
    commandsWithOutput = tuple(map(str.splitlines, input.split('$ ')[1:]))

    root = {
        DIR_NAME_KEY: '/',
        DIR_FILES_SIZE_KEY: 0
    }

    fsDir = root

    for command, *output in commandsWithOutput[1:]:  # first command is to move to root
        if command.startswith('ls'):
            files = [int(re.match(r'^(\d+)', line).groups()[0]) for line in output if not line.startswith('dir')]
            dirs = [re.match(r'dir ([^\n]+)', line).groups()[0] for line in output if line.startswith('dir')]

            fsDir[DIR_FILES_SIZE_KEY] = sum(files)

            for dir in dirs:
                # create a new dir with parent set to cwd
                fsDir[dir] = {
                    '..': fsDir,  # parent ref
                    DIR_NAME_KEY: dir,  # name for debugging
                    DIR_FILES_SIZE_KEY: 0,  # self-size
                }

        if command.startswith('cd'):
            moveTo = command.split(' ')[1]
            fsDir = fsDir[moveTo]

    return root


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        log = file.read()

    fs = parseFs(log)

    diskSize = 70_000_000
    used = totalFolderSize(fs)

    free = diskSize - used

    targetFree = 30_000_000
    needToRemove = targetFree - free

    def search(root: dict):
        bigEnoughChildren = [dir for dir in childDirs(root) if totalFolderSize(dir) >= needToRemove]

        if len(bigEnoughChildren) == 0:  # none of my children are big enough :(
            return root['__totalSize']

        return min([search(dir) for dir in bigEnoughChildren])

    print(search(fs))


if __name__ == "__main__":
    main()
