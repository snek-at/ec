import unittest
from app.config import dev
from app import create_app
import json

app = create_app(dev.DevConfig)


class BasicTestCase(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

        app.testing = True
        self.tester = app.test_client(self)
