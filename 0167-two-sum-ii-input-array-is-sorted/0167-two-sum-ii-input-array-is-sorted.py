class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in numbers:
            if target-i in numbers:
                if i == target-i:
                    t = numbers.index(i)
                    return [t+1, t+numbers[t+1:].index(i)+2]
                return [numbers.index(i)+1,numbers.index(target-i)+1]