import math

def findMedianSortedArrays(nums1, nums2):
    nums = {}
    index = 0
    nums1_it = iter(nums1)
    nums2_it = iter(nums2)
    n1 = None
    n2 = None
    while True:
        if n1 == None:
            n1 = next(nums1_it, None)
        if n2 == None:
            n2 = next(nums2_it, None)
        if n1 != None and n2 != None:
            if n1 < n2:
                nums[index] = n1
                n1 = None
            else:
                nums[index] = n2
                n2 = None
            index += 1
            continue
        if n1 != None:
            nums[index] = n1
            index += 1
            n1 = None
            continue
        if n2 != None:
            nums[index] = n2
            index += 1
            n2 = None
            continue
        if n1 == None and n2 == None:
            break
    if (len(nums1) + len(nums2)) % 2 == 0:
        median = even_median(nums1, nums2, nums)
        return median
    else:
        median = odd_median(nums1, nums2, nums)
        return median

def even_median(arr1, arr2, nums):
    index1 = int((len(arr1) + len(arr2))/ 2)
    index2 = index1 - 1
    return (nums[index1] + nums[index2]) / 2

def odd_median(arr1, arr2, nums):
    index = int(math.floor((len(arr1) + len(arr2) )/ 2))
    return nums[index]

import unittest

class FindMedianSortedArraysTest(unittest.TestCase):

    def test_find_median_sorted_arrays_1(self):
        nums1 = [1, 3]
        nums2 = [2]

        median = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 2.0)

    def test_find_median_sorted_arrays_2(self):
        nums1 = []
        nums2 = [1]

        median = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 1)

    def test_find_median_sorted_arrays_3(self):
        nums1 = [3]
        nums2 = [-2, -1]

        median = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, -1.0)

    def test_find_median_sorted_arrays_4(self):
        nums1 = [1, 2]
        nums2 = [3, 4]

        median = findMedianSortedArrays(nums1, nums2)
        self.assertEqual(median, 2.5)


unittest.main()