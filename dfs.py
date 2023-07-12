from queue import Queue

adj_list = {
    "C": ["F"],
    "E": ["B"],
    "A": ["B"],
    "B": ["A", "D", "E"],
    "D": ["B"],
    "F": ["C"],
}

# Required array and dictionary
color = {}  # W, G, B
parent = {}
trav_time = {}  # [ start ,end ]
dfs_traversal_output = []

# initialize

for node in adj_list.keys():
    color[node] = "W"
    parent[node] = None
    trav_time[node] = [-1, -1]

time = 0


def dfs_util(u):
    global time
    color[u] = "G"
    trav_time[u][0] = time
    dfs_traversal_output.append(u)
    time += 1
    for v in adj_list[u]:
        if color[v] == "W":
            parent[v] = u
            dfs_util(v)

    color[u] = "B"
    trav_time[u][1] = time
    time += 1


for node in adj_list.keys():
    if color[node] == "W":
        dfs_util(node)

print(dfs_traversal_output)
print(parent)
print(trav_time)