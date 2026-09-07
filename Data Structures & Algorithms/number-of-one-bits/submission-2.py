class Solution:
    '''
Example Walkthrough: Consider n = 23 (binary 10111):

Initial state: n = 10111
After 1st operation: n = 10111 & 10110 = 10110   (flip the lowest-order 1 bit)
After 2nd operation: n = 10110 & 10101 = 10100
After 3rd operation: n = 10100 & 10011 = 10000
After 4th operation: n = 10000 & 01111 = 00000    (binary 00000)

Counting 1 Bits
Each time we perform the operation n = n &(n-1), 
we effectively remove the lowest-order 1 bit from n. 
By counting the number of iterations required until n becomes 0, 
we get the count of 1 bits in the binary representation of n.

Why It Works
Property of AND operation: The AND operation keeps bits where both operands have a 1. 
When subtracting 1, the binary representation flips the lowest-order 1 bit to 0 and all bits after it to 1.

Iterative Reduction: Each iteration removes a single 1 bit, 
effectively counting all 1 bits through repeated reductions.

This technique is efficient because it directly targets the 1 bits and skips over the 0 bits, 
making it faster than examining each individual bit.
    '''

    def hammingWeight(self, n: int) -> int:
        counter = 0
        while n!= 0:
            n = n & (n-1)
            counter +=1
        return counter
        