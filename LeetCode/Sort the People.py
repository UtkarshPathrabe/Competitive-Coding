class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        data = [(height, name) for height, name in zip(heights, names)]
        data.sort(reverse = True)
        return [name for _, name in data]