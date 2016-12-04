# pylint: disable=C0103,C0111
import unittest

from bumblebee.engine import Engine
from bumblebee.config import Config

class TestEngine(unittest.TestCase):
    def setUp(self):
        self.engine = Engine(Config())
        self.testModule = "test"
        self.testModuleSpec = "bumblebee.modules.{}".format(self.testModule)
        self.testModules = [
            {"module": "test", "name": "a"},
            {"module": "test", "name": "b"},
        ]

    def test_stop(self):
        self.assertTrue(self.engine.running())
        self.engine.stop()
        self.assertFalse(self.engine.running())

    def test_load_module(self):
        module = self.engine.load_module(self.testModule)
        self.assertEquals(module.__module__, self.testModuleSpec)

    def test_load_modules(self):
        modules = self.engine.load_modules(self.testModules)
        self.assertEquals(len(modules), len(self.testModules))
        self.assertEquals(
            [module.__module__ for module in modules],
            [self.testModuleSpec for module in modules]
        )

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
