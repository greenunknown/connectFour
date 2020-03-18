from unittest import TestCase
from connectFour.connectFour.minimax import MinimaxConnectFour


class TestMinimax(TestCase):
    def setup(self):
        self.mmcfour = MinimaxConnectFour()

    def tearDown(self):
        self.mmcfour = None

    def testDisplay(self):
        pass