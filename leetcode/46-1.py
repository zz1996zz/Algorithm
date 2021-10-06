class Solution:
    def permute(self, nums):
        result = []
        prev_elements = []

        def dfs(elements):
            if len(elements) == 0:
                result.append(prev_elements[:])

            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)

                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()

        dfs(nums)
        return result


answer = Solution()
print(answer.permute(nums = [1,2,3]))
print(answer.permute(nums = [0,1]))
print(answer.permute(nums = [1]))

