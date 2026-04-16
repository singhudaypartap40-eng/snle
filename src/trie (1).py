class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]

        current.is_end = True

    def search_prefix(self, prefix):
        current = self.root

        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        results = []
        self._dfs(current, prefix, results)
        return results

    def _dfs(self, node, prefix, results):
        if node.is_end:
            results.append(prefix)

        for char in node.children:
            self._dfs(node.children[char], prefix + char, results)