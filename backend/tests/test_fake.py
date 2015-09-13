# -*- coding: utf-8 -*-
__author__ = 'fdgogogo'

import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
