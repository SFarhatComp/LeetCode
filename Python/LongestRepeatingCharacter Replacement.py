from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        alphabet_dict = defaultdict(int)
        L = 0
        max_counter = 0
        for R in range(len(s)):
            alphabet_dict[s[R]] +=1

            while (R-L+1) - max(alphabet_dict.values()) > k:
                alphabet_dict[s[L]] -=1
                L+=1
            max_counter  = max(max_counter , R-L+1)
        return max_counter