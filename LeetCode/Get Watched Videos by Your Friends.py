class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        visited = set()
        queue = deque([(id, 0)])
        visited.add(id)
        requiredFriends = []
        while queue:
            person, lev = queue.popleft()
            if lev == level:
                requiredFriends.append(person)
            if lev > level:
                break
            for friend in friends[person]:
                if friend not in visited:
                    queue.append((friend, lev + 1))
                    visited.add(friend)
        videosFrequency = defaultdict(int)
        for friend in requiredFriends:
            for video in watchedVideos[friend]:
                videosFrequency[video] += 1
        return [video[0] for video in sorted(videosFrequency.items(), key = lambda x : (x[1], x[0]))]