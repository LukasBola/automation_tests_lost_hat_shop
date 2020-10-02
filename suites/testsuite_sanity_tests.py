import unittest

from tests.lost_hat_login_page_tests import LostHatLoginPageTests
from tests.lost_hat_front_page_tests import LostHatFrontTestsClassTests


def sanity_suite():
    test_suite = unittest.TestSuite()
    # adding test classes:
    test_suite.addTest(LostHatLoginPageTests('test_login_with_correct_login_and_password'))
    test_suite.addTest(LostHatLoginPageTests('test_login_with_incorrect_login_and_password'))
    test_suite.addTest(LostHatFrontTestsClassTests('test_front_page_products_have_price_in_pln'))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(sanity_suite())
