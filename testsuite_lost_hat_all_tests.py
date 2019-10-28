import unittest

from lost_hat_smoke_tests import LostHatSmokeTests
from lost_hat_front_page_tests import LostHatFrontPageTests
from lost_hat_product_page_tests import LostHatProductPageTests
from lost_hat_login_page_tests import LostHatLoginPageTests

def lost_hat_full_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(unittest.makeSuite(LostHatSmokeTests))
    test_suite.addTest(unittest.makeSuite(LostHatFrontPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatProductPageTests))
    test_suite.addTest(unittest.makeSuite(LostHatLoginPageTests))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(lost_hat_full_suite())