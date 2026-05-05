from collections import defaultdict
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        courses = defaultdict(list)
        for a, b in prerequisites:
            courses[a].append(b)

        UNVISITED = 0
        VISITING = 1
        VISITED = 2

        states = [UNVISITED] * numCourses

        def dfs(node):
            if states[node] == VISITED:
                return True
            if states[node] == VISITING:
                return False

            states[node] = VISITING

            for nei in courses[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True