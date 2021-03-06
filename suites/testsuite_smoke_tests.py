import unittest

from tests.lost_hat_smoke_tests import LostHatSmokeTests


def smoke_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(smoke_suite())
