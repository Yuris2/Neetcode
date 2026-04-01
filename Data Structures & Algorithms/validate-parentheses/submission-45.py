class Solution:
    """
    input: "[]"
    Output: True

    Input: s = "([{}])"
    # Seen:
    Output True

    Input: s = "[(])"
    # Seen: [, (]
    Output False

    Input: s = ""
    Output False

    """
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ["(", "[", "{"]:
                stack.append(s[i])
            elif s[i] == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop(-1)
            elif s[i] == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop(-1)
            else:
                if not stack or stack[-1] != "{":
                    return False
                stack.pop(-1)
        if stack:
            return False
        return True

        # Check if any more open characters, return False if there are some left
        # Return True

        