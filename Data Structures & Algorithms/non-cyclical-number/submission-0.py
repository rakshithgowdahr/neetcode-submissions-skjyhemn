class Solution:
    def isHappy(self, n: int) -> bool:
        hash_set = set()
        while True:
            if n == 1:
                return True
            if n in hash_set:
                return False
            hash_set.add(n)
            square = 0
            while n > 0:
                last_digit = n % 10
                square += (pow(last_digit, 2))
                n = n // 10
            n = square
        return False