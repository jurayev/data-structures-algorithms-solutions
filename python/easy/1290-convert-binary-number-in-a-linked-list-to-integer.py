# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValueBinaryToNumber(self, head: ListNode) -> int:
        """
        Time Complexity  - O(2N)
        Space Complexity - O(1)

        Approach: Count the lenght, use pure base 2 to base 10 conversion

        Examples:
        1 -> 0 -> 1


        101 -> 5


        base 2 -> base 10

        1*2^2 + 0*2^1 + 1*2^0

        """
        node = head
        size = 0

        while node:
            size += 1
            node = node.next

        number = 0
        node = head

        while node:
            size -= 1
            number += node.val * 2 ** size
            node = node.next

        return number

    def getDecimalValueFromBinaryStringToNumber(self, head: ListNode) -> int:
        """
        Time Complexity  - O(2N)
        Space Complexity - O(N)

        Approach: Collect all numbers in array, convert to binary string, and use builtin method for conversion.

        Examples:
        1 -> 0 -> 1


        101 -> 5


        """

        number_array = []

        node = head

        while node:
            number_array.append(str(node.val))
            node = node.next

        binary = "".join(number_array)

        return int(binary, 2)