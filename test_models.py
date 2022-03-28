from flask_login import current_user
from pathlib import Path
from flask_login import UserMixin
import pytest
from urllib import response
from flaskblog import app
import unittest

from flaskblog.models import User, load_user

class FlaskTestCase(unittest.TestCase):
    def test_startpage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
   


    


    

if __name__ == '__main__':
    unittest.main()