from os import path
import unittest
from unittest.mock import patch, MagicMock
from app import Staff, email_format, getDB

from app import email_format, displayMessage, getDB, checkEmail, checkNames

class BarhopUnmockedTestCase(unittest.TestCase):
    def test_email_format(self):
        self.assertEqual(email_format("TEST@TEST.COM"), "test@test.com")
    
    def test_displayMessage1(self):
        self.assertEqual(displayMessage("No email"), "No email entered , please sign in!")

    def test_displayMessage2(self):
        self.assertEqual(displayMessage("Error"), "Unknown error!")

class BarhopMockedTestCase(unittest.TestCase):

    def setUp(self):
        self.mock_db_entries = [
            Staff(
                employee_first_name = "Test", 
                employee_last_name = "Ttest",
                employee_email = "test@tests.com", 
                employee_availability = "NEVER"
                employee_password = "")
        ]
    def get_mocked_db_entries(self):
            return self.mock_db_entries

    def test_getDB(self):
        expected_first_name = []
        expected_last_name = []
        expected_email = []
        expected_availability = []
        for item in self.mock_db_entries:
            expected_first_name.append(item.employee_first_name)
            expected_last_name.append(item.employee_last_name)
            expected_email.append(item.employee_email)
            expected_availability.append(item.employee_availability)
            expected_password.append(item.employee_password)
        
        with patch ("app.Staff.query") as mocked_query:
            mocked_query.all = self.get_mocked_db_entries
            employees = getDB()
            self.assertEqual(employees, (expected_first_name, expected_last_name, expected_email, expected_availability, expected_password))

    def test_checkEmail(self):
        expected_email = []
        for item in self.mock_db_entries:
            expected_email.append(item.employee_email)
        
        with patch ("app.Staff.query") as mocked_query:
            mocked_query.all = self.get_mocked_db_entries
            email = checkEmail(expected_email[0])
            self.assertEqual(email, True)
    
    def test_checkName(self):
        expected_first_name = []
        expected_last_name = []
        expected_email = []
        for item in self.mock_db_entries:
            expected_first_name.append(item.employee_first_name)
            expected_last_name.append(item.employee_last_name)
            expected_email.append(item.employee_email)
        
        with patch ("app.Staff.query") as mocked_query:
            mocked_query.all = self.get_mocked_db_entries
            name = checkNames(expected_first_name[0], expected_last_name[0])
            self.assertEqual(name, True)

    # def test_already_User(self):
    #     with patch("app.already_User().flask.request.form") as mock:
    #         mock_response = MagicMock()
    #         mock_response.side_effect = "test"
    #         mock.return_value = mock_response

    #         first_name_list, last_name_list, email_list , availability_list= getDB()

    #         self.assertEqual(already_User(first_name_list, last_name_list, email_list), ("","","",False)) 

    # def test_display(self):
    #     with patch("app.test", return_value = False) as mock:
    #         expected_value = False
    #         self.assertEqual(mock.return_value, expected_value)

if __name__ == "__main__":
    unittest.main()

# class BarhopTestCase(unittest.TestCase):

#     # John suggestion == Break off small functions to to test querys of db and

#     def setUp(self):
#         self.mock_db_entry = [
#             Staff(
#                 employee_first_name="John",
#                 employee_last_name="Martin",
#                 employee_email="jmartin191@gsu.edu",
#                 employee_availability=None,
#             ),
#             Staff(
#                 employee_first_name="Rice",
#                 employee_last_name="Maxwell",
#                 employee_email="pmaxwell6@student.gsu.edu",
#                 employee_availability=None,
#             ),
#             Staff(
#                 employee_first_name="Gayoung",
#                 employee_last_name="Kim",
#                 employee_email="gkim70@student.gsu.edu",
#                 employee_availability=None,
#             ),
#             Staff(
#                 employee_first_name="Matthew",
#                 employee_last_name="Nguyen",
#                 employee_email="mnguyen101@student.gsu.edu",
#                 employee_availability=None,
#             ),
#         ]
#         self.email_mockery = "notricesreal@email.com"

#     # Test email is in all lower case befor added to the DB
#     def test_email_format_mocked(self):
#         test_email = app.email_format("NOTRicesReal@email.com")
#         self.assertEqual(test_email, self.email_mockery)

#     def test_user_preference_mocked(self):
#         with patch("app.Staff.query") as mocke_query:

#             for emp in self.mock_db_entry:
#                 emp = getDB
#                 self.assertTrue(emp.u)

#             # # mocke_query.all.return_value =
#             # print(emp)
#             # self.assertEqual(emp, emp)
