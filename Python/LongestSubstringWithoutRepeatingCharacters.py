class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        visited = set()
        l = 0
        result = 0
        for r,value in enumerate(s):
            while value in visited:
                visited.remove(s[l])
                l+=1
            
            visited.add(value)
            result = max(result, r - l + 1)
        return result
        