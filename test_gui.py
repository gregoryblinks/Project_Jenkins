from re import search
from threading import Thread
from webbrowser import Chrome
from selenium import webdriver
import selenium.webdriver
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait


options = EdgeOptions()
options.use_chromium = True
#options.headless = True
options.add_experimental_option("detach", True)
driver = Edge(options=options, executable_path=r'msedgedriver')

URL = 'http://127.0.0.1:5000/home'

def launch_click_around():
    driver.get(URL)
    driver.find_element_by_link_text('Home').click()
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_link_text('About').click()
    driver.find_element_by_link_text('Register').click()

def launch_login_logout():
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_id('email').send_keys('greg@gmail.com')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.find_element_by_link_text('Logout').click()

def launch_login():
    driver.get(URL)
    driver.find_element_by_link_text('Login').click()
    driver.find_element_by_id('email').send_keys('greg@gmail.com')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('submit').click()

def launch_register_used_username():
    driver.get(URL)
    driver.find_element_by_link_text('Register').click()
    driver.find_element_by_id('username').send_keys('greg')
    driver.find_element_by_id('email').send_keys('1234@gmail.com')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('confirm_password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")

def launch_register_used_email():
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('email').clear() 
    driver.find_element_by_id('username').send_keys('paulie')
    driver.find_element_by_id('email').send_keys('greg@gmail.com')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('confirm_password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")

def launch_register_passwords_not_equal():
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('email').clear() 
    driver.find_element_by_id('username').send_keys('paulie')
    driver.find_element_by_id('email').send_keys('greg2@gmail.com')
    driver.find_element_by_id('password').send_keys('123956')
    driver.find_element_by_id('confirm_password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")

def launch_register_email_not_valid():
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('email').clear() 
    driver.find_element_by_id('username').send_keys('paulie')
    driver.find_element_by_id('email').send_keys('greg2')
    driver.find_element_by_id('password').send_keys('123456')
    driver.find_element_by_id('confirm_password').send_keys('123456')
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")

def launch_walkthrough_posts():
    driver.find_element_by_link_text('Home').click()
    driver.find_element_by_link_text('Jenkins Project').click()
    driver.find_element_by_link_text('greg').click()
    driver.find_element_by_tag_name('h1').text
    driver.find_element_by_link_text('Home').click()
    driver.find_element_by_link_text('TestUser').click()
    driver.find_element_by_link_text('Home').click()
    
def launch_check_account():
    launch_login()
    driver.find_element_by_link_text('Account').click()
    driver.find_element_by_xpath("//legend[contains(.,'Account Info')]").text
    driver.find_element_by_css_selector('p.text-secondary').text
    driver.find_element_by_id('username').clear()
    driver.find_element_by_id('email').clear()
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")
    driver.find_element_by_link_text('Logout').click()

def launch_create_new_post():
    launch_login()
    driver.find_element_by_link_text('New Post').click()
    driver.find_element_by_id('submit').click()
    driver.find_element_by_class_name("invalid-feedback")
    driver.find_element_by_id('title').send_keys('Test ending')
    driver.find_element_by_id('content').send_keys('So far you have seen the movement of this GUI-Test')




launch_click_around()
launch_login_logout()
launch_register_used_username()
launch_register_used_email()
launch_register_passwords_not_equal()
launch_register_email_not_valid()
launch_walkthrough_posts()
launch_check_account()
launch_create_new_post()
driver.close()


