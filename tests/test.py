g = Graph()
g.load_from_file("data/network.txt")

dist, prev = g.dijkstra("DepotA")

print(dist)