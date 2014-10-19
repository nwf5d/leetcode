#!/usr/bin/env python
#encoding: GBK
#url:https://oj.leetcode.com/problems/two-sum/

class Solution:
    # @return a tuple, (index1, index2)
    # solution 1 is more quickly
    def twoSum(self, num, target):
    	dict_num = {}
    	(index1, index2) = (0, 0)
    	for i in range(len(num)):
    		print "i", i, len(num)
    		if target - num[i] in dict_num:
    			index1 = dict_num[target - num[i]] + 1
    			index2 = i + 1
    		else:
    			dict_num[num[i]] = i

  		return (index1, index2)

    def twoSum2(self, num, target):
        dict_num = {}
    	(index1, index2) = (0, 0)
    	for i in range(len(num)):
        	try:
    		    flag = dict_num[target - num[i]]
    		except KeyError:
    			dict_num[num[i]] = i
    		else:
    			index1 = flag + 1
    			index2 = i + 1

    	return (index1, index2)

if __name__ == '__main__':
	sol = Solution()
	num = [3, 2, 4]
	target = 6
	print sol.twoSum(num, target)
	print sol.twoSum2(num, target)
