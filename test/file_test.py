
import unittest
import sys
from os.path import realpath


src_realpath = realpath("./src")
print(src_realpath)
sys.path.insert(1, src_realpath)

from filemanipulation.file import Files




class FileTest(unittest.TestCase):
    

    def test_read_file(self):
        a = Files("1", data_workdir="carson-m/_sent_mail")
        reader = a.read_file()
        self.assertIn("From: mike.carson@enron.com",reader)
        self.assertIn("Message-ID: <18924171.1075858198540.JavaMail.evans@thyme>",reader)
        self.assertIn("To: macharta@yahoo.com",reader)
        self.assertIn("Subject: Welcome to the information age!",reader)
        self.assertIn("What is up ?? What do you think about the cotton bowl??? Are you going??",reader)
        self.assertIn("Date: Mon, 11 Dec 2000 02:34:00 -0800 (PST)",reader)

    def test_read_file(self):
        a = Files("3", data_workdir="carson-m/inbox")
        reader = a.read_file()
        splito = reader.split("\n")
        print(splito[4])
if __name__ == "__main__":
    unittest.main()
