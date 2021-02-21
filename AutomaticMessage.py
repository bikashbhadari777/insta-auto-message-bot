from selenium import webdriver
import csv
from pprint import pprint
import time
from selenium.common.exceptions import NoSuchElementException




class Login():

    def __init__(self, username, password,user_last_range, maximumuser, Message ):
        self.username = username
        self.password = password
        self.user_last_range = user_last_range
        self.maximumuser = maximumuser
        self.message = Message


    def directToAccount(self, usersid):
        self.driver.get('https://www.instagram.com/{}/'.format(usersid))
        self.driver.implicitly_wait(10)

        # <<<<<<<<<<<<,IF STATEMENT AND REDIRETING TO SENT THE DESIRED MESSAGE

        try:
            followbutton = self.driver.find_element_by_css_selector('._6VtSN')
            followbutton.click()
            time.sleep(5)
            messagebox = self.driver.find_element_by_css_selector('._8A5w5')
            messagebox.click()
            time.sleep(10)
            # <<<<<<<<<<<<< MESSENGING
            message_box = self.driver.find_element_by_css_selector('.focus-visible')
            message_box.send_keys('hey ! '+ str(usersid)+'\n'+ str(self.message))
            submit_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
            submit_button.click()
            time.sleep(4)

        except NoSuchElementException  :
            print('\n Next user ')


    # click and send

    def csvIntoList(self, user_last_range, maximumuser):
        time.sleep(2)
        with open('outputfile.csv', newline='') as file:
            reader = csv.reader(file)
            res = list(map(tuple, reader))
            usinglist = res[user_last_range:maximumuser]
        pprint('Username processing')
        # here we are gonna import all the necessary usernames

        # redirecting from here
        # bikash ko loop
        for user in usinglist:
            user = user[0]
            self.directToAccount(user)
        with open('history.csv','a') as p :
            p.write('from range ' + str(self.user_last_range) + ' to ' + str(self.maximumuser))
        print('\n<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< MISSION SUCESSFULL>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>.')


    def directMessagePage(self, driver):
        # here we will go to direct message section by loging into the website
        self.driver = webdriver.Chrome(driver)
        startUrl = ('https://www.instagram.com/direct/inbox/')
        self.driver.get(startUrl)
        self.driver.implicitly_wait(20)
        # login
        username_Value = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        username_Value.send_keys(self.username)
        self.driver.implicitly_wait(2)
        password_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(self.password)
        self.driver.implicitly_wait(2)
        password_field.submit()
        self.driver.implicitly_wait(16)
        # <<<<<<<<<<<<<<<<<<<<<<<<<<<NOT NOW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        self.driver.find_element_by_css_selector('.aOOlW.HoLwm').click()
        self.driver.implicitly_wait(16)
        self.csvIntoList(self.user_last_range, self.maximumuser)


obj = Login(input('enter your username mr.Bhatta : '),
            input('enter your password mr.Bhatta : '),int(input('Users last time range : ')),
            int(input('\nup the how much profile do you wanna message : ')

                ),
            input('\n what message do you want to send??? : ')
            )
obj.directMessagePage('C:\Program Files (x86)\chromedriver.exe')
