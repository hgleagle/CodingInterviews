#!/usr/bin/env python3

"""
File: test11_minNumberInRotateArray.py
Author: heguilong
Email: hgleagle@gmail.com
Github: https://github.com/hgleagle
Description:把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
"""


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if rotateArray == []:
            return 0
        low = 0
        high = len(rotateArray) - 1
        while high - low > 1:
            mid = (low + high) // 2

            # 异常情况顺序查找,比如 [1, 1, 1, 0, 1] [1, 0, 1, 1, 1]
            if rotateArray[low] == rotateArray[mid] and rotateArray[mid] == rotateArray[high]:
                min_val = rotateArray[low]
                for i in rotateArray[low: high + 1]:
                    if i < min_val:
                        min_val = i
                return min_val
            # [1, 2, 3, 4, 5]
            if rotateArray[low] <= rotateArray[mid]:
                low = mid
            elif rotateArray[high] >= rotateArray[mid]:
                high = mid

        return rotateArray[high]


if __name__ == "__main__":
    arr = [3, 4, 5, 1, 2]
    s = Solution()
    print(s.minNumberInRotateArray(arr))

