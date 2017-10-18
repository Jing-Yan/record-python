# -*- coding:utf-8 -*-


def BinarySearch(arr, key):
    min = 0
    max = len(arr)-1

    if key in arr:
        while True:
            mid = (min + max) // 2
            if arr[mid] > key:
                max = mid - 1
            elif arr[mid] < key:
                min = mid + 1
            elif arr[mid] == key:
                print str(key) + "在数组里面的第" + str(mid+1) + "个位置"
                break
    else:
        print "没有该数字"

arr = [45, 8, 55, 77, 99, 110, 456, 782, 10, 7]
key = input("请输入你要查找的数字：")
BinarySearch(arr, int(key))
