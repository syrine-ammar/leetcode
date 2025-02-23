class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h=set()
        for i in range(len(nums)):
            if(nums[i]in h):
                return True
            else:
                h.add(nums[i])
        return False

nums = list(map(int, input("Enter numbers separated by spaces: ").split()))
solution = Solution()

