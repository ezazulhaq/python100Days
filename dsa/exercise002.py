"""
Given an integer n, return true if it is a power of four.
Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x
"""


class Solution:
    def is_power_of_four(self, n: int) -> bool:
        if n < 1 and n % 4 != 0:
            return False

        if n == 1:
            return True

        return self.is_power_of_four(n / 4)


print(Solution().is_power_of_four(16))
