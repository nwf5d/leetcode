#!/usr/bin/env python
#encoding: GBK
#https://oj.leetcode.com/problems/combination-sum/
import copy

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
    	resList = []
    	sumList = []
    	candidates.sort()
    	self.findOneSum(candidates, target, 0, sumList, resList)
    	return resList

    def findOneSum(self, candidates, target, index, sumList, resList):
    	# sumList = []
    	# maxNum = min(sumList)
    	if target == 0:
   			resList.append(sumList)
   			return

    	for i in xrange(index, len(candidates)):
    		if candidates[i] <= target:
    			copyList = copy.copy(sumList)
    			copyList.append(candidates[i])
    			newTarget = target - candidates[i]
    			self.findOneSum(candidates, newTarget, i, copyList, resList)

if __name__ == '__main__':
	candidates = [2, 3, 6, 7]
	target = 7
	sol = Solution()
	resList = sol.combinationSum(candidates, target)
	print resList
