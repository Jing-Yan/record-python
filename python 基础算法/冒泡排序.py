# -*- coding: utf-8 -*-
"""
重复走访排序的数列，一次比较两个元素
"""


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i+1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists

arr = [45, 8, 55, 77, 99, 110, 456, 782, 10, 7]

print bubble_sort(arr)
