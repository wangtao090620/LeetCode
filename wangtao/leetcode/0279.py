#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-01-07 17:03


"""
给定正整数 n，找到若干个完全平方数（比如 1, 4, 9, 16, ...）使得它们的和等于 n。你需要让组成和的完全平方数的个数最少。

示例 1:

输入: n = 12
输出: 3
解释: 12 = 4 + 4 + 4.
示例 2:

输入: n = 13
输出: 2
解释: 13 = 4 + 9.
"""

# dp[n] = Min{ dp[n - i*i] + 1 },  n - i*i >=0 && i >= 1


"""
public int numSquares(int n) {
	int[] dp = new int[n + 1];
	Arrays.fill(dp, Integer.MAX_VALUE);
	dp[0] = 0;
	for(int i = 1; i <= n; ++i) {
		int min = Integer.MAX_VALUE;
		int j = 1;
		while(i - j*j >= 0) {
			min = Math.min(min, dp[i - j*j] + 1);
			++j;
		}
		dp[i] = min;
	}		
	return dp[n];
}
"""


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            min_value = float("inf")
            j = 1

            while i - j * j >= 0:
                min_value = min(min_value, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_value
        return dp[n]


if __name__ == '__main__':
    print(Solution().numSquares(13))
