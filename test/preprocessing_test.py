from json import loads
import unittest

from filemanipulation.dirs import Dirs
from filemanipulation.file import Files
from model.EmailModel import EmailModel


class PreprocessingTest(unittest.TestCase):
    
    clean_data = Dirs("preprocessing_data/ready_data")


    def test_gen_file(self):
        
        for i in self.clean_data.list_subdirs():
            f = Files(i)
            file_data = loads(f.read_file())
            node = EmailModel()
            node.set_schema(
                emailFrom=file_data['emailFrom'],
                emailTo=file_data['emailTo']
            )

            self.assertIn("@",node.emailFrom)
            self.assertIn(".",node.emailFrom)
            self.assertNotIn(",",node.emailFrom)
            if type(node.emailTo) is str:
                self.assertIn("@",node.emailFrom)
                self.assertIn(".",node.emailFrom)
                self.assertNotIn(",", node.emailTo)
            else:
                for email in node.emailTo:
                    self.assertIn("@",email)
                    self.assertIn(".",email)
                    self.assertNotIn(",", email)