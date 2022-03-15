class Solution1:

    def multiply(self, elem1, elem2):
        return elem1 * elem2

    def findRLEArray(self, encoded1, encoded2):
        p1, p2 = 0, 0
        output = []
        while p1 < len(encoded1) and p2 < len(encoded2):
            freq1, freq2 = encoded1[p1][1], encoded2[p2][1]
            if freq1 == freq2:
                element = self.multiply(encoded1[p1][0], encoded2[p2][0])
                freq = freq1
                p1 += 1
                p2 += 1

            elif freq1 < freq2:
                element = self.multiply(encoded1[p1][0], encoded2[p2][0])
                freq = min(freq1, freq2)
                p1 += 1

            else:
                element = self.multiply(encoded1[p1][0], encoded2[p2][0])
                freq = min(freq1, freq2)
                p2 += 1

            if len(output) and output[-1][0] == element:
                output[-1][1] += freq
            else:
                output.append([element, freq])

        return output

class Solution:
    def findRLEArray(self, encoded1: List[List[int]], encoded2: List[List[int]]) -> List[List[int]]:
        """
        
        Ideas:
        Idea 1. Brute force - decode both arrays, do product of two arrays, encode it back
            Time: O(nums1) + O(nums2) + O(output)
            Space: O(nums1) + O(nums2) + O(output)
        Idea 2. Two pointer iteration
        Time: O(max(en1, en2))
            Space: O(output)
        if freq1[i] == freq2[i]:
        Multiplying the val1[i] * val2[i]
        Place the result in output[i] = [product, min_freq]
        Move both p1 and p2
        if freq1[i] < freq2[i]: move p1, decrement freq2[i] -= freq1[i]
        if freq1[i] > freq2[i]: move p2, decrement freq1[i]

        
        """
        encoded_product = []
        p1, p2 = 0, 0
        while p1 < len(encoded1) and p2 < len(encoded2):
            val1, freq1 = encoded1[p1]
            val2, freq2 = encoded2[p2]
            product = val1 * val2
            min_freq = min(freq1, freq2)
            if encoded_product and encoded_product[-1][0] == product:
                encoded_product[-1][1] += min_freq
            else:    
                encoded_product.append([product, min_freq])
            if freq1 == freq2:
                p1 += 1
                p2 += 1
            elif freq1 < freq2:
                p1 += 1
                encoded2[p2][1] -= min_freq
            else:
                p2 += 1
                encoded1[p1][1] -= min_freq
                
        return encoded_product
        