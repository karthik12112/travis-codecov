import unittest

import awesome


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(awesome.smile(), ":)")
 	print("#####hello#####")


if __name__ == '__main__':
    unittest.main()
