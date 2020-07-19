#!/usr/bin/env python

# -*- encoding: utf-8 -*-

# @Author  :   wangtao

# @Contact :   wangtao090620@gmail.com

# @Time    :   2020-07-18 11:37


"""
如果一个数是素数，则该数的整数倍都不是素数
例如2是素数，则4、6、8、10、12...都不是素数。基于该方法，我们可以把素数的倍数直接置为非素数。



"""


class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [1] * n
        count = 0
        for i in range(2, n):
            if isPrimes[i] == 1:
                count += 1
                j = i * 2
                while j < n:
                    isPrimes[j] = 0
                    j += i
                    print(j)
        return count


if __name__ == '__main__':
    print(Solution().countPrimes(10))
