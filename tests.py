import unittest
from mock import *

import Server
# import Client

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


if __name__ == '__main__':
    unittest.main()
