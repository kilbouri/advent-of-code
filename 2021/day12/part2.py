from collections import defaultdict
from os.path import dirname


# depth-first traversal with one duplicate visit to any non-endpoint lowercase node
def allPaths(u, edges, _visited=defaultdict(int), _path=[], _returnValue=[]):
    # True iff no other value in the _visited table has a value exceeding 1
    def noDoubleVisit():
        return all([_visited[n] <= 1 for n in _visited])

    # returns the "cost" of visiting the given node
    def nodeIncrement(node):
        return 1 if node.islower() else 0

    _visited[u] += nodeIncrement(u)
    _path.append(u)

    if u == 'end':
        _returnValue.append(_path.copy())
    else:
        for con in edges[u]:
            if con == 'start':  # never ever revisit the start node
                continue

            # tweaked from part 1 to allow revisiting a single lowercase node
            canRevisit = con.islower() and noDoubleVisit()
            if (_visited[con] == 0) or canRevisit:
                allPaths(con, edges)

    _path.pop()
    _visited[u] = max(0, _visited[u] - nodeIncrement(u))

    # since this is shared between calls, only the final value will be returned by
    # the original stack frame
    return _returnValue


def main():
    with open(f"{dirname(__file__)}/input.txt") as file:
        inputEdges = [l.strip().split("-") for l in file.readlines()]

    edges = defaultdict(list)
    for edge in inputEdges:
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])

    n = len(allPaths('start', edges))
    print(f"There are {n} unique paths through the cave.")


if __name__ == "__main__":
    main()
