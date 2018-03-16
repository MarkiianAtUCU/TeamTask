# File: test.py
# Module has tests for main.py file.
import main
import unittest


class TestMail(unittest.TestCase):
    """ Represent tests for main pachage. """
    def setUp(self):
        """ Initialize field before every test. """
        # Create client and mail_info fields that will be tested in next
        # methods.
        self.client = main.Client("Andrii", 12, "male",
                                  "prysiazhnyk@ucu.edu.ua", "")
        self.mail_info = main.MailInfo(self.client, "Mail code", "Message")

    def test_client(self):
        """ Test client object. """
        client = self.client
        # Test name and sex of client.
        self.assertEquals(client.name + ", " + client.sex, "Andrii, male")

    def test_mail_info(self):
        """ Test MailInfo class """
        # Test str method and message field.
        self.assertEqual(str(self.mail_info), "Andrii")
        self.assertEqual(self.mail_info.message, "Message")

    def test_mail_box(self):
        """ Test MailBox class. """
        # Create instance of class MailBox.
        box = main.MailBox()
        # Test if inf field is empty list.
        self.assertFalse(box.inf)
        box.add_mail_info(self.mail_info)
        # Test add_mail_info method.
        self.assertEqual(box.inf, [self.mail_info])


if __name__ == "__main__":
    unittest.main()