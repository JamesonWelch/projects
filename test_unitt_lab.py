import unittest


class TestPythonMethods(unittest.TestCase):
    def test_abs(self):
        x = 33.33
        y = abs(-33.33)
        self.assertEqual(x, y)

    def test_bin(self):
        x = 0b111001000
        self.assertTrue(x, bin(456))

    def test_bool(self):
        x = True
        y = False
        self.assertTrue(bool(x))
        self.assertFalse(bool(y))

    def test_callable(self):
        def foo():
            return 5

        x = foo
        nums = 6 + 7
        self.assertTrue(callable(x))
        self.assertFalse(callable(nums))

    def test_chr(self):
        self.assertEqual(chr(457392), "\U0006fab0")

    def test_dict(self):
        nums = dict(x=9, y=10)
        nums_type = type(nums)
        self.assertEqual(type(nums), nums_type)

    def test_divmod(self):
        nums = divmod(5, 2)
        self.assertEqual(nums, (2, 1))

    def test_enumerate(self):
        stuff = [12, 45]
        self.assertEqual(list(enumerate(stuff)), [(0, 12), (1, 45)])

    def test_float(self):
        n = "45"
        self.assertEqual(float(n), 45.0)

    def test_hex(self):
        x = hex(12648430)
        self.assertEqual(x, "0xc0ffee")

    def test_int(self):
        pass

    def test_len(self):
        pass

    def test_list(self):
        pass

    def test_max(self):
        pass

    def test_min(self):
        pass

    def test_next(self):
        pass

    def test_oct(self):
        pass

    def test_sorted(self):
        pass

    def test_sum(self):
        pass


if __name__ == "__main__":
    unittest.main()
