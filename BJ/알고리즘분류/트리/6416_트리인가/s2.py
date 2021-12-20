import sys

sys.stdin = open('input.txt')
lines = sys.stdin.readlines()

trees = {}
tc = 1
edge = 0
node = set()
p = {}

for line in lines:
    for pair in line.split("  "):
        if len(pair) > 2:
            u, v = map(int, pair.split())
            if u == v == 0:
                if len(node) - 1 == edge or edge == 0:
                    print("Case " + str(tc) + " is a tree.")
                else:
                    print("Case " + str(tc) + " is not a tree.")
                node = set()
                edge = 0
                tc += 1
            elif u > 0 and v > 0:
                edge += 1
                node.add(u)
                node.add(v)


