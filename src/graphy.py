class Graph:
    def __init__(self):
        self.adj = {}

    def add_node(self, node):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u, v, weight):
        self.add_node(u)
        self.add_node(v)
        self.adj[u].append((v, weight))

    def load_from_file(self, filename):
        with open(filename, "r") as f:
            lines = f.readlines()

        mode = None

        for line in lines:
            line = line.strip()

            if line == "NODES":
                mode = "nodes"
                continue
            elif line == "EDGES":
                mode = "edges"
                continue

            if not line:
                continue

            if mode == "nodes":
                nodes = line.split()
                for n in nodes:
                    self.add_node(n)

            elif mode == "edges":
                u, v, w = line.split()
                self.add_edge(u, v, int(w))

    def display(self):
        for node in self.adj:
            print(node, "->", self.adj[node])

    def get_nodes(self):
        return list(self.adj.keys())

    def get_neighbors(self, node):
        return self.adj.get(node, [])

    # =========================
    # Cycle Detection
    # =========================

    def detect_cycle(self):
        color = {node: "WHITE" for node in self.adj}
        cycle_nodes = []

        for node in self.adj:
            if color[node] == "WHITE":
                if self._dfs_cycle(node, color, cycle_nodes):
                    return True, cycle_nodes

        return False, []

    def _dfs_cycle(self, node, color, cycle_nodes):
        color[node] = "GRAY"
        cycle_nodes.append(node)

        for neighbor, _ in self.get_neighbors(node):

            if color[neighbor] == "GRAY":
                cycle_nodes.append(neighbor)
                return True

            if color[neighbor] == "WHITE":
                if self._dfs_cycle(neighbor, color, cycle_nodes):
                    return True

        color[node] = "BLACK"
        cycle_nodes.pop()
        return False