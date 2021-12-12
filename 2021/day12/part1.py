from collections import defaultdict
from os import getcwd


# depth-first traversal with one duplicate visit to any non-endpoint lowercase node
def allPaths(u, edges, _visited=set(), _path=[], _returnValue=[]):
    if u.islower():
        _visited.add(u)

    _path.append(u)

    if u == 'end':
        _returnValue.append(_path.copy())
    else:
        for con in edges[u]:
            if con == 'start' or con in _visited:
                continue
            allPaths(con, edges)

    _path.pop()
    _visited -= {u}

    # since this is shared between calls, only the final value will be returned by
    # the original stack frame
    return _returnValue


def main():
    with open(f"{getcwd()}/2021/day12/input.txt") as file:
        inputEdges = [l.strip().split("-") for l in file.readlines()]

    edges = defaultdict(list)
    for edge in inputEdges:
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])

    n = len(allPaths('start', edges))
    print(f"There are {n} unique paths through the cave.")


if __name__ == "__main__":
    main()
