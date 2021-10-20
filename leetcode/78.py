class Solution:
    def subsets(self, nums):
        result = []

        def dfs(index, path):
            #매번 경로를 결과에 추가
            result.append(path)

            for i in range(index, len(nums)):
                dfs(i+1, path+[nums[i]])

        dfs(0, [])
        return result



answer = Solution()
print(answer.subsets(nums = [1,2,3]))
print(answer.subsets(nums = [0]))
