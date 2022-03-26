class Solution:
    def maxDiff(self, number: int) -> int:
        number_as_string = str(number)
        size = len(number_as_string)
        larger_number = str(number_as_string)
        for i in range(size):
            digit = number_as_string[i]
            if digit < "9":
                larger_number = larger_number.replace(digit, "9")
                break
        smaller_number = str(number_as_string)
        if smaller_number[0] != "1":
            smaller_number = smaller_number.replace(smaller_number[0], "1")
            return int(larger_number) - int(smaller_number)
        # 101
        for i in range(1, size):
            digit = number_as_string[i]
            if digit not in "01":
                smaller_number = smaller_number.replace(digit, "0")
                break
        return int(larger_number) - int(smaller_number)
