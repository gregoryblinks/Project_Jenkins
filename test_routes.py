import email
import pytest
from urllib import response
from flaskblog import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def test_startpage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
    
    def test_home(self):
        tester = app.test_client(self)
        response = tester.get('/home', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_home_shows_login(self):
        tester = app.test_client(self)
        response = tester.post('/home', follow_redirects=True )
        self.assertTrue(b'Login', response.data)

    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_login_correctly(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="greg@gmail.com", password= "123456"), follow_redirects=True )
        self.assertIn(b'greg', response.data)

    def test_login_incorrectly(self):
        tester = app.test_client(self)
        response = tester.post('/login', data=dict(email="greg@gmail.com", password= "234567"), follow_redirects=True )
        self.assertIn(b'Need An Account?', response.data)

    def test_about(self):
        tester = app.test_client(self)
        response = tester.get('/about', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_register(self):
        tester = app.test_client(self)
        response = tester.get('/register', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        tester = app.test_client(self)
        response = tester.get('/logout', content_type='html/text')
        self.assertEqual(response.status_code, 302)
    
    def test_logout_correctly(self):
        tester = app.test_client(self)
        tester.post('/login', data=dict(email="greg@gmail.com", password= "123456"), follow_redirects=True )
        response = tester.get('/logout', follow_redirects=True )
        self.assertIn(b'CoreyMS', response.data)
   
    def test_account(self):
        tester = app.test_client(self)
        response = tester.get('/account', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_new_post(self):
        tester = app.test_client(self)
        response = tester.get('/post/new', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_id_post(self):
        tester = app.test_client(self)
# Zu tun: Eine For Schleife einbauen um mehrere posts zu finden        
        response = tester.get('/post/28', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_update_post(self):
        tester = app.test_client(self)
# Zu tun: Eine For Schleife einbauen um mehrere posts zu finden        
        response = tester.get('/post/28/update', content_type='html/text')
        self.assertEqual(response.status_code, 302)

    def test_deleted_post(self):
        tester = app.test_client(self)
        response = tester.get('/post/28/delete', content_type='html/text')
        self.assertEqual(response.status_code, 405)

    def test_user_page(self):
        tester = app.test_client(self)
        response = tester.get('/user/greg', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_reset_password(self):
        tester = app.test_client(self)
        response = tester.get('/reset_password', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_reset_password_token(self):
        tester = app.test_client(self)
        response = tester.get('/reset_password/<token>', content_type='html/text')
        self.assertEqual(response.status_code, 302)



if __name__ == '__main__':
    unittest.main()