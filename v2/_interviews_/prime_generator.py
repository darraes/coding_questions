class PrimeGenerator:
    def __init__(self, stream=None):
        self._test_stream = stream
        # TODO Validation if stream is open. Throw if not.

    def generate(self, n):
        # TODO Validations
        if n < 2:
            return
        if n == 2:
            self._stream_out(2)
            return

        self._stream_out(2)
        self._stream_out(3)
        primes = [2, 3]  # TODO possible reserve memory in advance

        for i in range(5, n + 1):
            if not self._is_divisible(i, primes):
                self._stream_out(i)
                primes.append(i)

    def _stream_out(self, n):
        # TODO Validations
        if self._test_stream:
            self._test_stream.write(n)
        else:
            print(n)

    def _is_divisible(self, n, array):
        # TODO Validations
        for p in array:
            if n % p == 0:
                return True
        return False


###############################################################
import unittest


class TestStream:
    def __init__(self):
        self.primes = []

    def write(self, n):
        self.primes.append(n)


class TestFunctions(unittest.TestCase):
    def test_1(self):
        test_stream = TestStream()
        pg = PrimeGenerator(test_stream)
        pg.generate(15)
        self.assertEqual([2, 3, 5, 7, 11, 13], test_stream.primes)


if __name__ == "__main__":
    unittest.main()
