from graph import Graph
from trie import Trie
from dispatch import DispatchQueue
from utils import Package

def reconstruct_path(prev, start, end):
    path = []
    current = end

    while current is not None:
        path.append(current)
        current = prev[current]

    path.reverse()

    if path[0] == start:
        return path
    return []

def main():
    import os
    g = Graph()

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "..", "data", "network.txt")
    g.load_from_file(file_path)

    trie = Trie()
    for node in g.get_nodes():
        trie.insert(node)

    dispatch = DispatchQueue()

    while True:
        print("\n===== Smart Network Logistics Engine =====")
        print("1. Display Network")
        print("2. Find Shortest Path")
        print("3. Detect Cycles")
        print("4. Dispatch Package")
        print("5. Search Depot")
        print("6. Autocomplete")
        print("7. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            g.display()

        elif choice == "2":
           src = input("Source: ").strip()
           dest = input("Destination: ").strip()

           dist, prev = g.dijkstra(src)

           if dest not in dist or dist[dest] == float('inf'):
             print("No path found")
           else:
             path = reconstruct_path(prev, src, dest)
             print("Path:", " -> ".join(path))
             print("Cost:", dist[dest])

        elif choice == "3":
            has_cycle, nodes = g.detect_cycle()
            print("Cycle:", has_cycle)
            print("Nodes:", nodes)

        elif choice == "4":
            pid = input("Package ID: ")
            priority = int(input("Priority (1-10): "))
            dest = input("Destination: ")
            weight = float(input("Weight: "))

            pkg = Package(pid, priority, dest, weight)
            dispatch.enqueue(pkg)

            print("Dispatched:", dispatch.dequeue())

        elif choice == "5":
            name = input("Search depot: ")
            print("Exists:", name in g.get_nodes())

        elif choice == "6":
            prefix = input("Prefix: ")
            print(trie.search_prefix(prefix))

        elif choice == "7":
            break


if __name__ == "__main__":
    main()