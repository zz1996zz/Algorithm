import functools
import collections

graph = collections.defaultdict(list)

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]


for a,b in sorted(tickets):
    graph[a].append(b)


print(list(graph))


