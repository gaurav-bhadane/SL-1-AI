inf = 999999
k, a, b, u, v, n, ne = 0, 0, 0, 0, 0, 0, 1
mincost = 0
cost = [[0, 10, 20], [12, 0, 15], [16, 18, 0]]
p = [0] * 9
def applyfind(i):
    while p[i] != 0:
        i = p[i]
    return i
def applyunion(i, j):
    if i != j:
        p[j] = i
        return 1
    return 0
n = 3
for i in range(n):
    for j in range(n):
        if cost[i][j] == 0:
            cost[i][j] = inf
print("Minimum Cost Spanning Tree:\n")
while ne < n:
    min_val = inf
    for i in range(n):
        for j in range(n):
            if cost[i][j] < min_val:
                min_val = cost[i][j]
                a = u = i
                b = v = j
    u = applyfind(u)
    v = applyfind(v)
    if applyunion(u, v) != 0:
        print(f"{a} -> {b}")
        mincost += min_val
    cost[a][b] = cost[b][a] = 999
    ne += 1
print(f"\n\tMinimum cost = \n{mincost}")