import unittest
from mock import *

import Server
import Client
from Client import ClassProduction
from mock import MagicMock
from mock import patch


class Test(unittest.TestCase):
    def test_create(self):
        Server.delete("h")
        self.assertEqual(Server.success, Server.create("h", "h"))
        self.assertEqual("Fail! h : h", Server.create("h", "h"))

    def test_read(self):
        Server.delete("h")
        self.assertEqual("Fail! Record with key \"h\" was not found!", Server.read("h"))
        Server.create("h", "h")
        self.assertEqual("h : h", Server.read("h"))
        return

    def test_update(self):
        Server.delete("h")
        self.assertEqual("Fail! Record with key \"h\" was not found!", Server.update("h", "h"))
        Server.create("h", "u")
        self.assertEqual(Server.success, Server.update("h", "h"))

    def test_delete(self):
        Server.delete("h")
        self.assertEqual("Fail! Record with key \"h\" was not found!", Server.delete("h"))
        Server.create("h", "ha")
        self.assertEqual(Server.success, Server.delete("h"))

    def test_c_create(self):
        thing = ClassProduction
        # thing.method = MagicMock(return_value="Success!")
        with patch('Client.ClassProduction.create') as perm_mock:
            assert isinstance(perm_mock, object)
            perm_mock.return_value = "Success!"
            self.assertEqual(thing.create("1", "1"), "Success!")


if __name__ == '__main__':
    unittest.main()
