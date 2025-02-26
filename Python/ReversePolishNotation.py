from typing import List
class Solution:
    def perform_operation(self, firstoperand, secondoperand, operation):
        answer = 0
        if operation == "*":
            answer = firstoperand * secondoperand
        elif operation == "+":
            answer = firstoperand + secondoperand
        elif operation == "-":
            answer = firstoperand - secondoperand
        else:
            answer = int(firstoperand / secondoperand)
        return answer  

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        answer = 0
        for element in tokens:
            if element not in {"+", "-", "*", "/"}:
                stack.append(int(element))

            else:
                second_operand = stack.pop()
                first_operand = stack.pop()
                stack.append(self.perform_operation(first_operand, second_operand, element))
                
        return stack.pop()

if __name__ == "__main__":
    # tokens = ["2", "1", "+", "3", "*"]
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    solution = Solution()
    result = solution.evalRPN(tokens)
    print(result)