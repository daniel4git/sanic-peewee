from . import FakeSanis as Sanic

from sanic_peewee import Peewee

import unittest

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.widget = Widget('The widget')


    @unittest.expectedFailure
    def test_fail(self):
        self.assertEqual(1, 0, "broken")
