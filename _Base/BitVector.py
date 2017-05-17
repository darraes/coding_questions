import sys
import array

class BitVector(object):
    OUTER_SHIFT = 5
    INNER_ROTATION = 31

    def __init__(self, max_bit_count):
        remainder = max_bit_count & BitVector.INNER_ROTATION
        storage_size = max_bit_count >> BitVector.OUTER_SHIFT
        if remainder > 0: storage_size += 1

        self._storage = array.array('I', [0]*storage_size )  
        self._max_bit_count = max_bit_count


    def get_at(self, i):
        if i > self._max_bit_count or i < 0: raise
        array_i = i >> BitVector.OUTER_SHIFT
        return self._storage[array_i] & (1 << (i & BitVector.INNER_ROTATION)) > 0


    def clear_at(self, i):
        if i > self._max_bit_count or i < 0: raise
        array_i = i >> BitVector.OUTER_SHIFT
        self._storage[array_i] = (self._storage[array_i] & ~(1 << (i & BitVector.INNER_ROTATION)))


    def set_at(self, i, value):
        if i > self._max_bit_count or i < 0: raise
        if value != 0 and value != 1: raise
        array_i = i >> BitVector.OUTER_SHIFT
        self.clear_at(i)
        self._storage[array_i] = (self._storage[array_i] | (value << (i & BitVector.INNER_ROTATION)))


    def print_storage(self):
        result = ""
        for i in range(self._max_bit_count):
            result += "1" if self.get_at(i) else "0"
        print result


bv = BitVector(64)
print sys.getsizeof(bv._storage)
bv.print_storage()
bv.set_at(5, 1)
bv.print_storage()
bv.set_at(33, 1)
bv.set_at(31, 1)
bv.print_storage()
bv.set_at(0, 1)
bv.print_storage()
bv.set_at(0, 0)
bv.print_storage()
bv.clear_at(5)
bv.clear_at(33)
bv.clear_at(31)
bv.clear_at(0)
bv.print_storage()

