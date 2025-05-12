from typing import List

class SortMethods:

    @staticmethod
    def sort_bubble(array: List[int]) -> List[int]:
        n = len(array)
        for i in range(n):
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
    
    @staticmethod
    def sort_bubble_optimized(array: List[int]) -> List[int]:
        n = len(array)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
                    swapped = True
            if not swapped:
                break
        return array

    @staticmethod
    def sort_selection(array: List[int]) -> List[int]:
        n = len(array)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if array[j] < array[min_idx]:
                    min_idx = j
            array[i], array[min_idx] = array[min_idx], array[i]
        return array
    
    @staticmethod
    def sort_insertion(array: List[int]) -> List[int]:
        for i in range(1, len(array)):
            key = array[i]
            j = i - 1
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
            array[j + 1] = key
        return array

    @staticmethod
    def sort_shell(array: List[int]) -> List[int]:
        n = len(array)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = array[i]
                j = i
                while j >= gap and array[j - gap] > temp:
                    array[j] = array[j - gap]
                    j -= gap
                array[j] = temp
            gap //= 2
        return array
