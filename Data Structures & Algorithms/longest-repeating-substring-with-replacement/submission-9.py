class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = {}
        left, maxLen = 0, 0

        for right in range(len(s)):
            counter[s[right]] = 1 + counter.get(s[right], 0)
            while (right - left + 1) > (k + max(counter.values())):
                counter[s[left]] -= 1
                left += 1
            maxLen = max(maxLen, right - left + 1)
        
        return maxLen
        