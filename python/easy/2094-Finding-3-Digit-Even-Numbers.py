class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        """
        [2,1,3,0]

        [3,2,1,0]
         i
           j
             k
               ^

        100 - 999

        100
        102
        104
        """
        counts = collections.Counter(digits)
        result = []
        n = len(digits)

        for num in range(100, 999, 2):
            result.append(num)

            all_digits = []

            while num:
                digit = num % 10
                num //= 10
                if counts[digit] > 0:
                    counts[digit] -= 1
                    all_digits.append(digit)

            for d in all_digits:
                counts[d] += 1
            if len(all_digits) != 3:
                result.pop()
        return result

    """
    [102,120,130,132,210,230,302,310,312,320]

    """