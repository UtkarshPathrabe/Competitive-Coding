class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        currentPlantTime, result = 0, 0
        data = sorted([(plant, grow) for plant, grow in zip(plantTime, growTime)], key=lambda x: -x[1])
        for plant, grow in data:
            currentPlantTime += plant
            result = max(result, currentPlantTime + grow)
        return result