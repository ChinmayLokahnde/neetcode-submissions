class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)

        for i in range(n):
            j = n - 1
            while i < j:
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
                j -=1        