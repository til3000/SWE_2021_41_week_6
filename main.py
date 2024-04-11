# -*- coding: utf-8 -*-

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    numToIndex = {}
    for index, num in enumerate(nums):
        comp = target - num
        if comp in numToIndex:
            return [numToIndex[comp], index]
        numToIndex[num] = index
    return []