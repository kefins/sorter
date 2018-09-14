#!/usr/bin/evn python3
# -*- coding: utf-8 -*-

import sys

class Sorter:
    #array - array to be heapify as max root
    #size  - size of array
    #pos   - root position
    #最大堆化
    def maxHeapify(self, array, size, pos):
        left  = 2 * pos + 1
        right = 2 * pos + 2

        maximum = left if left < size and array[left] > array[pos] else pos
        maximum = right if right < size and array[right] > array[maximum] else maximum

        #如果当前根节点不是最大值，那么交换位置，使最大值处于根节点处
        if maximum != pos:
            array[maximum], array[pos] = array[pos], array[maximum]

            #因为交换了根节点，需要重新堆化新节点
            self.maxHeapify(array, size, maximum)

        return

    #最小堆化
    def minHeapify(self, array, size, pos):
        left  = 2 * pos + 1
        right = 2 * pos + 2

        minimum = left if left < size and array[left] < array[pos] else pos
        minimum = right if right < size and array[right] < array[minimum] else minimum

        #如果当前根节点不是最小值，那么交换位置，使最大值处于根节点处
        if minimum != pos:
            array[minimum], array[pos] = array[pos], array[minimum]

            #因为交换了根节点，需要重新堆化新节点
            self.minHeapify(array, size, minimum)

        return

    def heapSort(self, array):
        size = array.__len__()

        #堆化输入列表
        for i in range(size-1, -1, -1):
            print("size = %d, i = %d" %(size, i))
            self.maxHeapify(array, size, i)

        for i in range(size-1, 0, -1):
            #交换最大值和末尾
            array[0], array[i] = array[i], array[0]
            #继续堆化剩余的元素
            self.maxHeapify(array, i, 0)



    #快速排序分区，从中间选取pivot
    def quickSortPartitionm(self, array, left, right):
        #sign pivot position
        ps    = (left + right) // 2
        newps = 0
        pivot = array[ps]
        pp    = left

        print("input from %2d to %2d: %s" %(left, right, array[left:right+1]))
        for i in range(left, right+1):
            #print("array[i]=%d, pp=%d, pivot=%d" %(array[i], pp, pivot))
            if array[i] <= pivot:
                array[i],array[pp] = array[pp],array[i]
                print("temp array(pp=%d, i=%d): %s" %(pp, i, array[left:right+1]))
                newps = pp if i == ps else newps
                pp += 1

        pp -= 1
        #print("pivot is %2d: %s, ps=%d, newps=%d, pp=%d\n" %(pivot, array[left:right+1], ps, newps, pp))
        array[pp],array[newps] = array[newps],array[pp]
        print("pivot is %2d: %s, pp=%d\n" %(pivot, array[left:right+1], pp))

        return pp

    #快速排序分区，从右端选取pivot
    def quickSortPartitionr(self, array, left, right):
        #sign pivot position
        pp    = left
        pivot = array[right]

        print("input from %2d to %2d: %s" %(left, right, array[left:right+1]))
        for i in range(left, right):
            #print("array[i]=%d, pp=%d, pivot=%d" %(array[i], pp, pivot))
            if array[i] <= pivot:
                array[i],array[pp] = array[pp],array[i]
                print("temp array(pp=%d, i=%d): %s" %(pp, i, array[left:right+1]))
                pp += 1

        array[pp],array[right] = array[right],array[pp]
        print("pivot is %2d: %s, pp=%d\n" %(pivot, array[left:right+1], pp))

        return pp

    #快速排序分区，从左端选取pivot
    def quickSortPartitionl(self, array, left, right):
        #sign pivot position
        pp    = left
        pivot = array[left]

        print("input from %2d to %2d: %s" %(left, right, array[left:right+1]))
        for i in range(left, right+1):
            #print("array[i]=%d, pp=%d, pivot=%d" %(array[i], pp, pivot))
            if array[i] <= pivot:
                array[i],array[pp] = array[pp],array[i]
                print("temp array(pp=%d, i=%d): %s" %(pp, i, array))
                pp += 1

        #decrease one to get the pivot position
        pp -= 1
        array[pp],array[left] = array[left],array[pp]
        print("pivot is %2d: %s, pp=%d\n" %(pivot, array, pp))
        return pp

    #快速排序
    def quickSort(self, array, left, right):
        if left < right:
            pi = self.quickSortPartitionm(array, left, right)

            self.quickSort(array, 0,    pi-1)
            self.quickSort(array, pi+1, right)

    def merge(self, array, left, mid, right):
        i = left
        j = mid+1
        array_new = []
        print("left=%d, mid=%d, right=%d\n" %(left, mid, right))
        print("L=%s, R=%s\n" %(array[left:mid+1], array[mid+1:right+1]))
        while i <= mid and j <= right:
            if array[i] <= array[j]:
                array_new.append(array[i])
                print("+++++Larray_new=%s\n" %(array_new))
                i += 1
            else:
                array_new.append(array[j])
                print("++++Rarray_new=%s\n" %(array_new))
                j += 1

        print("i=%d, mid=%d, j=%d, array=%s\n" %(i, mid, j, array))
        l = array_new.__len__()
        if i <= mid:
            array_new[l:] = array[i : mid+1]
            print("+++++LLarray_new=%s\n" %(array_new))


        l = array_new.__len__()
        if j <= right:
            array_new[l:] = array[j : right+1]
            print("++++RRarray_new=%s\n" %(array_new))


        print("****array_new=%s\n" %(array_new))
        array[left:right+1] = array_new
        print("****array=%s\n" %(array))

    def mergeSort(self, array, left, right):
        mid = (left + right - 1) // 2
        if left < right:
            self.mergeSort(array, left, mid);
            self.mergeSort(array, mid+1, right);

            self.merge(array, left, mid, right)

        return

    def bubbleCommonSort(self, array):
        size = array.__len__()

        for i in range(size):
            for j in range(size-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]

        return

    def bubbleCockTailSort(self, array):
        size = array.__len__()

        for i in range(size):
            if i // 2:
                for j in range(size-1):
                    if array[j] > array[j+1]:
                        array[j], array[j+1] = array[j+1], array[j]
            else:
                for j in range(1,size).__reversed__():
                    if array[j] < array[j-1]:
                        array[j], array[j-1] = array[j-1], array[j]

        return

    def insertCommonSort(self, array):
        size = array.__len__()
        if size < 2:
            return
        temp = []

        if array[0] > array[1]:
            temp.append(array[1])
            temp.append(array[0])
        else:
            temp = arrap[0:1]

        print("at first %s" %temp)
        #确保temp长度为2
        for i in range(2, size):
            target = array[i]
            #如果待插入目标比第一个小，直接在队首插入该元素
            if target <= temp[0]:
                temp.insert(0, target)
                print("head   insert %2d, temp = %s" %(target, temp))
                continue

            #在队中插入该元素
            insert_flag = 0
            for j in range(temp.__len__() - 1):
                if target >= temp[j] and target <= temp[j+1]:
                    #print("target=%d, temp[j] = %d, temp[j+1]=%d, j=%d" %(target, temp[j], temp[j+1], j))
                    temp.insert(j+1, target)
                    insert_flag = 1
                    print("middle insert %2d, temp = %s" %(target, temp))
                    break

            #如果上述两次插入均未成，直接在队尾插入该元素
            if 0 == insert_flag:
                temp.append(target)
                print("tail   insert %2d, temp = %s" %(target, temp))

        array[0 : size+1] = temp[0 : size+1]

    def insertBSearchSort(self, array):
        size = array.__len__()
        if size < 2:
            return
        temp = []

        if array[0] > array[1]:
            temp.append(array[1])
            temp.append(array[0])
        else:
            temp = arrap[0:1]

        print("at first %s" %temp)
        #确保temp长度为2
        for i in range(2, size):
            target = array[i]
            left  = 0
            right = temp.__len__() - 1

            insert_flag = 0
            while left <= right:
                mid = (left + right) // 2
                if (temp[mid] == target):
                    temp.insert(mid, target)
                    insert_flag = 1
                    break

                if (temp[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1

                print("left=%d, right=%d mid=%d target=%d temp=%s" %(left, right, mid, target, temp))

            if insert_flag == 0:
                temp.insert(left, target)

            print("current temp=%s" %temp)

        array[0 : size+1] = temp[0 : size+1]

    def selectSort(self, array):
        size       = array.__len__()
        temp_array = []

        for i in range(size):
            target     = array[0]
            target_pos = 0

            for j in range(1, array.__len__()):
                if array[j] <= target:
                    target     = array[j]
                    target_pos = j
            array.pop(target_pos)

            print("target=%d" %target)

            temp_array.append(target)

        array[0 : size+1] = temp_array[0 : size+1]

if __name__ == '__main__':
    array = [12, 11, 5, 3, 7, 4, 19, 3, 8, 6]
    size  = array.__len__()
    target = Sorter()

    print("original array is: %s\n" %array)

    #堆排序
    #target.heapSort(array)

    #快速排序
    #target.quickSort(array, 0, size - 1)

    #归并排序
    #target.mergeSort(array, 0, size - 1)

    #普通冒泡排序
    #target.bubbleCommonSort(array)

    #鸡尾酒冒泡排序
    #target.bubbleCockTailSort(array)

    #插入排序
    #target.insertCommonSort(array)

    #二分插入排序
    target.insertBSearchSort(array)

    #选择排序
    #target.selectSort(array)

    print("sorted array is: %s" %array)
