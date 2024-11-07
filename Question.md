# [2275. Largest Combination With Bitwise AND Greater Than Zero](https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero)

__Type:__ Medium <br>
__Topics:__ Array, Hash Table, Bit Manipulation, Counting <br>
__Companies:__ Microsoft, Amazon, Adobe <br>
<hr>

The __bitwise AND__ of an array `nums` is the bitwise AND of all integers in `nums`.

- For example, for `nums = [1, 5, 3]`, the bitwise AND is equal to `1 & 5 & 3 = 1`.
- Also, for `nums = [7]`, the bitwise AND is `7`.

You are given an array of positive integers `candidates`. Evaluate the __bitwise AND__ of every __combination__ of numbers of `candidates`. Each number in `candidates` may only be used __once__ in each combination.

Return _the size of the __largest__ combination of_ `candidates` _with a bitwise AND __greater__ than_ `0`
<hr>

### Examples:

- __Example 1:__ <br>
__Input:__ candidates = [16,17,71,62,12,24,14] <br>
__Output:__ 4 <br>
__Explanation:__ The combination [16,17,62,24] has a bitwise AND of 16 & 17 & 62 & 24 = 16 > 0. <br>
The size of the combination is 4. <br>
It can be shown that no combination with a size greater than 4 has a bitwise AND greater than 0. <br>
Note that more than one combination may have the largest size. <br>
For example, the combination [62,12,24,14] has a bitwise AND of 62 & 12 & 24 & 14 = 8 > 0.

- __Example 2:__ <br>
__Input:__ candidates = [8,8] <br>
__Output:__ 2 <br>
__Explanation:__ The largest combination [8,8] has a bitwise AND of 8 & 8 = 8 > 0. <br>
The size of the combination is 2, so we return 2.
<hr>

### Constraints:
- <code>1 <= candidates.length <= 10<sup>5</sup></code>
- <code>1 <= candidates[i] <= 10<sup>7</sup></code>
<hr>

### Hints:
- For the bitwise AND to be greater than zero, at least one bit should be 1 for every number in the combination.
- The candidates are 24 bits long, so for every bit position, we can calculate the size of the largest combination such that the bitwise AND will have a 1 at that bit position.