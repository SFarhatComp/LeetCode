import itertools
import time
from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        inital_dict = {"2":"abc", "3": "def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs", "8":"tuv", "9":"wxyz"}
        vector = []
        if digits == "":
            return []
        
        if len(digits) == 1:
            return [letter for letter in inital_dict[digits]] 
        
        vector = [inital_dict[digit] for digit in digits]
        combination = ["".join(element) for element in itertools.product(*vector)]    
        
        
        return combination
    
if __name__ == "__main__":
    solution = Solution()
    digits = "237"
    start_time = time.time()
    combinations = solution.letterCombinations(digits)
    end_time = time.time()
    print(combinations)
    print(f"Time taken: {end_time - start_time} seconds")