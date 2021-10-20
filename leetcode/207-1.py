import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        graph = collections.defaultdict(list)

        for a, b in prerequisites:
            graph[a].append(b)

        traced = set()
        visited = set()

        def dfs(i):
            if i in traced: # 순환구조이면 False
                return False

            if i in visited: # 이미 방문했던 노드이면 True
                return True

            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False

            traced.remove(i)
            visited.add(i)

            return True

        for x in list(graph):
            if not dfs(x):
                return False

        return True


answer = Solution()
print(answer.canFinish(numCourses = 2, prerequisites = [[1,0]]))
print(answer.canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]]))
