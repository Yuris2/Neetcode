class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            current = temperatures[i]
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > current:
                    result[i] = j - i
                    break
                elif j == len(temperatures) - 1:
                    result[i] = 0
        return result
    