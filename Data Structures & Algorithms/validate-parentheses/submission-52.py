class Solution:
    def isValid(self, s: str) -> bool:
        char_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for char in s:
            if char not in char_dict:
                stack.append(char)
            elif stack and stack[-1] == char_dict[char]:
                stack.pop(-1)
            else:
                return False
        if len(stack) > 0:
            return False
        else:
            return True