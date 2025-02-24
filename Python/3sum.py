from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for index, item in enumerate(nums):
            l = index + 1
            r = len(nums) - 1
            if index > 0 and nums[index] == nums[index - 1]:
                continue
            while l < r :
                if item + (nums[l] + nums[r]) == 0:
                    result.append([nums[l], nums[r], item])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
            
                elif item + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r-=1
        return result



def main():
    solution = Solution()
    test_input = [-1, 0, 1, 2, -1, -4]
    result = solution.threeSum(test_input)
    print(result)

if __name__ == "__main__":
    main()