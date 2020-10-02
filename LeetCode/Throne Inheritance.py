class ThroneInheritance:

    def __init__(self, kingName: str):
        self.inheritance = defaultdict(list)
        self.kingName = kingName
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.inheritance[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        result = []
        def dfs(name):
            nonlocal result
            if name not in self.dead:
                result.append(name)
            for child in self.inheritance[name]:
                dfs(child)
        dfs(self.kingName)
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()