class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        processGraph, result, stack = defaultdict(set), [kill,], [kill,]
        for p, pp in zip(pid, ppid):
            processGraph[pp].add(p)
        while stack:
            node = stack.pop()
            for child in processGraph[node]:
                stack.append(child)
                result.append(child)
        return result