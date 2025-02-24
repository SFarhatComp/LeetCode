from typing import List

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        m = 0
        while left <= right: 
            m = (left + right) // 2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                right = m - 1
            else:
                left = m + 1
        if nums[m] > target:
            return m
        else:
            return m + 1
    

def main():
    nums = [1, 3, 5, 6]
    target = 4
    solution = Solution()
    result = solution.searchInsert(nums, target)
    print(f"Output: {result}")

if __name__ == "__main__":
    main()

# No additional code needed here