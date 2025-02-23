class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        somme=0
        for i in range(n):
            somme+=nums[i]
        actsomme=(n*(n+1))//2
        return actsomme-somme

nums = list(map(int, input("Enter numbers: ").split()))
solution = Solution()
print(solution.missingNumber(nums))

