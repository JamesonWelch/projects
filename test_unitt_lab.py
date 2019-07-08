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
        pass

    def test_callable(self):
        pass

    def test_chr(self):
        pass

    def test_dict(self):
        pass

    def test_divmod(self):
        pass

    def test_enumerate(self):
        pass

    def test_float(self):
        pass

    def test_hex(self):
        pass

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
