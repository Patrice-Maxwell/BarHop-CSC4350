from os import path
import unittest
from unittest import mock
from unittest import result
from unittest.mock import patch
import app
from app import Staff, login_post, email_format, user_preference, getDB
import flask


class BarhopTestCase(unittest.TestCase):

    # John suggestion == Break off small functions to to test querys of db and

    def setUp(self):
        self.mock_db_entry = [
            Staff(
                employee_first_name="John",
                employee_last_name="Martin",
                employee_email="jmartin191@gsu.edu",
                employee_availability=None,
            ),
            Staff(
                employee_first_name="Rice",
                employee_last_name="Maxwell",
                employee_email="pmaxwell6@student.gsu.edu",
                employee_availability=None,
            ),
            Staff(
                employee_first_name="Gayoung",
                employee_last_name="Kim",
                employee_email="gkim70@student.gsu.edu",
                employee_availability=None,
            ),
            Staff(
                employee_first_name="Matthew",
                employee_last_name="Nguyen",
                employee_email="mnguyen101@student.gsu.edu",
                employee_availability=None,
            ),
        ]
        self.email_mockery = "notricesreal@email.com"

    # Test email is in all lower case befor added to the DB
    def test_email_format_mocked(self):
        test_email = app.email_format("NOTRicesReal@email.com")
        self.assertEqual(test_email, self.email_mockery)

    def test_user_preference_mocked(self):
        with patch("app.Staff.query") as mocke_query:

            for emp in self.mock_db_entry:
                emp = getDB
                self.assertTrue(emp.u)

            # # mocke_query.all.return_value =
            # print(emp)
            # self.assertEqual(emp, emp)


if __name__ == "__main__":
    unittest.main()


#     # Nothing yet

#     # Test if login_post is returning data in expected format
#     def signin_unmocked_client(self):
#         self.sucess_test_params = []

#         self.failure_test_params = []

#     # def test_login__mocked_server(self):

#     #     # expected_employee_first_name = []
#     #     # expected_employee_last_name = []
#     #     # expected_employee_email = []
#     #     # expected_employee_availability = []

#     #     # for employ in self.mock_db_entry:
#     #     #     expected_employee_first_name.append(employ.employee_first_name)
#     #     #     expected_employee_last_name.append(employ.employee_last_name)
#     #     #     expected_employee_email.append(employ.employee_email)
#     #     #     expected_employee_availability.append(employ.employee_availability)
#     #     #         mocke_query.all.return_value = self.mock_db_entry
#     #     #         yolo = login_post()

#     #     # self.assertEqual(
#     #     #     yolo,
#     #     #     (
#     #     #         expected_employee_first_name,
#     #     #         expected_employee_last_name,
#     #     #         expected_employee_email,
#     #     #         expected_employee_availability,
#     #     #     ),
#     #     # )


# if __name__ == "__main__":
#     unittest.main()
