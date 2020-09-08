# -*- coding: utf-8 -*-
# @Time    : 2020/8/28 10:10 下午
# @Author  : Ian Leto
# @File    : str.py
# 干啥的    :


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        newlist = []
        count = [0] * l
        for i in range(l):
            newlist.append(s[i])
            for j in range(i, l):
                if s[j] not in newlist:
                    newlist.append(s[j])
                    count[i] += 1
                else:
                    newlist = []
                    break
        return max(count) + 1

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        newStr = []
        res = 0
        for i in range(len(s)):
            if s[i] in newStr:
                newStr = newStr[newStr.index(s[i]):]
            else:
                newStr.append(s[i])
            temp = len(newStr)
            res = max(res, temp)

        return res


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring("abcabcbb"))
    print(Solution2().lengthOfLongestSubstring("aabaab!bb"))
