# initialize your stack as an empty list
# hash map to create pairs betw close and open brackets
# you want the close brackets to be the keys
# if a close bracket is found, stack must be empty
# check if both that close bracket and top of the stack (open) are found in hashmap
# pop the successes from stack
# otherwise, append (these appends will be open)
# you can keep adding open brackets 
# return True if the stack is empty (everything was success), else False


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ')' : '(', '}' : '{', ']' : '['}

        for c in s:
            if c in closeToOpen: # checks for close bracket
                if stack and stack[-1] == closeToOpen[c]: # open and close match
                    stack.pop() # pops last value from stack
                else: 
                    return False # identified that they don't match
            else: 
                stack.append(c)
        return len(stack) == 0 # stack is empty = true
