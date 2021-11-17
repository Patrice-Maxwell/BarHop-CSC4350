import unittest
from app import returnAvailability, checkEmail, checkName

class BarhopTestCase(unittest.TestCase):
    def testCheckEmail(self):
        KEY_INPUT = "ttesting@email.com"
        KEY_EXPECTED = True
        actual_result = checkEmail(KEY_INPUT)
        expected_result = KEY_EXPECTED

        self.assertEqual(actual_result, expected_result)

    def testcheckName(self):
        KEY_INPUT = "pmaxwell6@student.gsu.edu"
        KEY_EXPECTED = "Rice"
        actual_result = checkName(KEY_INPUT)
        expected_result = KEY_EXPECTED

        self.assertEqual(actual_result, expected_result)

    def testAvailability(self):
        KEY_INPUT = "a10@a"
        KEY_EXPECTED = '{"Thursday Night","Friday Night","Saturday Night","Sunday Night"}'
        actual_result = returnAvailability(KEY_INPUT)
        expected_result = KEY_EXPECTED

        self.assertEqual(actual_result, expected_result)



if __name__ == "__main__":
    unittest.main()
