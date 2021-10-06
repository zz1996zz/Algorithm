class Solution:
    def combinationSum(self, candidates, target: int):
        result = []

        def dfs(csum, index, path):
            if csum < 0:
                return
            elif csum == 0:
                result.append(path)
                return

            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])

        dfs(target, 0, [])
        return result


answer = Solution()
print(answer.combinationSum(candidates = [2,3,6,7], target = 7))
print(answer.combinationSum(candidates = [2,3,5], target = 8))
print(answer.combinationSum(candidates = [2], target = 1))
print(answer.combinationSum(candidates = [1], target = 1))
print(answer.combinationSum(candidates = [1], target = 2))

