from unittest import TestCase
# from connectFour.connectFour.cFour import cFour
import cFour


class TestCFour(TestCase):
    def setUp(self):
        self.cfour = cFour.cFour()

    def tearDown(self):
        self.cfour = None

    def testPutOutOfBounds(self):
        in_bounds, amt = self.cfour.put('red', 0)
        out_left, amt = self.cfour.put('red', -1)
        out_right, amt = self.cfour.put('red', 7)

        overput = 0
        for i in range(10):
            overput, amt = self.cfour.put('red', 0)
        self.assertEqual(in_bounds, 0)
        self.assertEqual(out_left, -5)
        self.assertEqual(out_right, -5)
        self.assertEqual(overput, -5)

    def testCheckRC(self):
        pass

    def testCheckDiag(self):
        pass

    def testWin(self):
        pass
