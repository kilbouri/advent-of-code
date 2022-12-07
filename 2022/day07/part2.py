from os.path import dirname
from pprint import pprint as print


import re


NON_DIR_KEYS = ['..', '__files', '__totalSize', '__dirname']


def parseFs(input: str):
    commandsWithOutput = tuple(map(str.splitlines, input.split('$ ')[1:]))

    root = {
        '__dirname': '/'
    }

    fsDir = root

    for command, *output in commandsWithOutput[1:]:  # first command is to move to root
        if command.startswith('ls'):
            files = [int(re.match(r'^(\d+)', line).groups()[0]) for line in output if not line.startswith('dir')]
            dirs = [re.match(r'dir ([^\n]+)', line).groups()[0] for line in output if line.startswith('dir')]

            fsDir['__files'] = files

            for dir in dirs:
                # create a new dir with parent set to cwd
                fsDir[dir] = {
                    '__dirname': dir,
                    '..': fsDir
                }

        if command.startswith('cd'):
            moveTo = command.split(' ')[1]
            fsDir = fsDir[moveTo]

    return root


def main():
    with open(f"{dirname(__file__)}/input.txt", "r") as file:
        log = file.read()

    fs = parseFs(log)

    def compute_self_sizes(root: dict):
        immediateSize = sum(root['__files'])
        childrenSize = 0

        dirs = [root[key] for key in root.keys() if key not in NON_DIR_KEYS]

        for child in dirs:
            compute_self_sizes(child)
            childrenSize += child['__totalSize']

        totalSize = immediateSize + childrenSize
        root['__totalSize'] = totalSize

    compute_self_sizes(fs)

    diskSize = 70_000_000
    used = fs['__totalSize']

    free = diskSize - used

    targetFree = 30_000_000
    needToRemove = targetFree - free

    def search(root: dict):
        dirs = [root[key] for key in root.keys() if key not in NON_DIR_KEYS]
        bigEnoughChildren = [dir for dir in dirs if dir['__totalSize'] >= needToRemove]

        if len(bigEnoughChildren) == 0:  # none of my children are big enough :(
            return root['__totalSize']

        childrenSearchResult = [search(dir) for dir in bigEnoughChildren]

        return min(childrenSearchResult)

    print(search(fs))


if __name__ == "__main__":
    main()
