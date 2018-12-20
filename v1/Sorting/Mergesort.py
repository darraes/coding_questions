class Mergesort(object):
    
    @staticmethod
    def sort(array):
        return Mergesort._sort(array, 0, len(array) - 1, [0] * len(array))


    @staticmethod
    def _sort(array, start, end, buffer):
        if start >= end: return

        mid = (start + end) / 2
        Mergesort._sort(array, start, mid, buffer)
        Mergesort._sort(array, mid + 1, end, buffer)
        Mergesort._merge(array, start, mid, end, buffer)

        
    @staticmethod
    def _merge(array, start, mid, end, buffer):
        left = start
        right = mid + 1
        for i in range(start, end + 1):
            if left <= mid and (right > end or array[left] < array[right]):
                buffer[i] = array[left]
                left += 1
            else:
                buffer[i] = array[right]
                right += 1

        Mergesort._copy(buffer, array, start, end)


    @staticmethod
    def _copy(source, target, start, end):
        for i in range(start, end + 1):
            target[i] = source[i]


array = [2, 4, 6, 3, 1, 8, 0, 3, 7]
Mergesort.sort(array)
print array