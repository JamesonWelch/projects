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
        self.assertIsInstance(nums, dict)

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
        x = int("12")
        self.assertIsInstance(x, int)

    def test_len(self):
        l = len([3, 6, 8, 3])
        self.assertEqual(4, l)

    def test_list(self):
        l = [3, 6, 90, 29, 59]
        l_t = (3, 6, 90, 29, 59)
        self.assertEqual(l, list(l_t))

    def test_max(self):
        i = range(10)
        self.assertEqual(9, max(i))

    def test_min(self):
        i = range(10)
        self.assertEqual(0, min(i))

    def test_next(self):
        a = ["level 1", "level 2", "level 3"]
        b = iter(a)
        next_level = next(b)
        after = next(b)
        self.assertEqual("level 1", next_level)
        self.assertEqual("level 2", after)

    def test_oct(self):
        o = oct(8)
        self.assertEqual(o, "0o10")

    def test_sorted(self):
        l = [6, 2, 1, 3, 4]
        self.assertEqual(sorted(l), [1, 2, 3, 4, 6])

    def test_sum(self):
        a = (3, 4)
        s = sum(a)
        self.assertEqual(s, 7)


if __name__ == "__main__":
    unittest.main()
