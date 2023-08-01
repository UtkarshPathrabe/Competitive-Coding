class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        n, m, skillId = len(people), len(req_skills), dict()
        for i, skill in enumerate(req_skills):
            skillId[skill] = i
        skillsMaskOfPerson = [0] * n
        for person in range(n):
            for skill in people[person]:
                skillsMaskOfPerson[person] |= (1 << skillId[skill])
        dp = [(1 << n) - 1] * (1 << m)
        dp[0] = 0
        for skillsMask in range(1, 1 << m):
            for person in range(n):
                smallerSkillsMask = skillsMask & ~skillsMaskOfPerson[person]
                if smallerSkillsMask != skillsMask:
                    # currentMask is the mask that represents the new team once you add the current person.
                    currentMask = dp[smallerSkillsMask] | (1 << person)
                    if currentMask.bit_count() < dp[skillsMask].bit_count():
                        dp[skillsMask] = currentMask
        resultMask = dp[(1 << m) - 1]
        result = []
        for person in range(n):
            if (resultMask >> person) & 1:
                result.append(person)
        return result