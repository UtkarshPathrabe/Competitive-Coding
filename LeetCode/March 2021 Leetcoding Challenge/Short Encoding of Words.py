class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie, result = {}, 0
        for word in words:
            node = trie
            for char in reversed(word):
                if '$' in node:
                    result -= node.pop('$')
                node = node.setdefault(char, {})
            if not node:
                node['$'] = len(word) + 1
                result += node['$']
        return result