# Smart Network Logistics Engine (SNLE)

## Author
Gurkirpaljeet Singh


---

## Project Description

This project implements a Smart Network Logistics Engine (SNLE) using core data structures and algorithms. It simulates a logistics system with route optimization, package dispatching, and search features.

---

## How to Run

```bash
python src/main.py
```

(On macOS/Linux you may use `python3 src/main.py`)

---

## Features

### 1. Graph Construction

* Implemented using an adjacency list
* Supports directed and weighted edges
* Loads data from `data/network.txt`

### 2. Shortest Path (Dijkstra’s Algorithm)

* Uses a custom MinHeap
* Computes shortest paths from a source node
* Outputs both path and total cost

### 3. Cycle Detection

* Uses DFS with node coloring (WHITE, GRAY, BLACK)
* Detects cycles in directed graphs

### 4. Priority Dispatch System

* Implemented using a MaxHeap
* Packages are dispatched based on priority

### 5. Hash Map

* Custom implementation with separate chaining
* Supports insert, search, delete, and resizing

### 6. Trie (Autocomplete)

* Supports prefix-based search
* Used for depot name suggestions

---

## Complexity Analysis

### Graph

* Space: O(V + E)

### Dijkstra

* Time: O((V + E) log V)
* Space: O(V)

### Cycle Detection (DFS)

* Time: O(V + E)
* Space: O(V)

### MinHeap / MaxHeap

* Insert: O(log n)
* Extract: O(log n)

### Hash Map

* Average case:

  * Insert/Search/Delete: O(1)
* Worst case: O(n)

### Trie

* Insert: O(L)
* Search: O(L)
* Autocomplete: O(k + m)

  * k = prefix length
  * m = number of results

---

## Sample Usage

```
Choose option: 2
Source: DepotA
Destination: ZoneNorth

Path: DepotA -> WarehouseX -> ZoneSouth -> DepotC -> ZoneNorth
Cost: 8
```

---

## Notes

* All data structures are implemented manually (no built-in shortcuts)
* Designed based on COMP 251 course material (Weeks 2–12)

---
