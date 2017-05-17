class Quicksort(object):

    @staticmethod
    def sort(array):
        Quicksort._sort(array, 0, len(array) - 1)

    @staticmethod
    def _sort(array, left, right):
        if left >= right: return

        pivot = Quicksort._partition(array, left, right)
        Quicksort._sort(array, left, pivot - 1)
        Quicksort._sort(array, pivot + 1, right)

    @staticmethod
    def _partition(array, left, right):
        pivot = (left + right)/2
        Quicksort._swap(array, pivot, right)

        store = left
        for i in range(left, right):
            if array[i] < array[right]:
                Quicksort._swap(array, i, store)
                store += 1

        Quicksort._swap(array, right, store)
        return store

    @staticmethod
    def _swap(array, x, y):
        tmp = array[x]
        array[x] = array[y]
        array[y] = tmp


array = [2, 4, 6, 3, 1, 8, 0, 3, 7]
Quicksort.sort(array)
print array
