class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        i = 0
        while i < len(temperatures)-1:
            stack.append(i)
            j = i + 1
            while stack and temperatures[stack[-1]] < temperatures[j]:
                    res[stack[-1]] = j - stack[-1]
                    stack.pop()
            i = i + 1

        return res


            







        