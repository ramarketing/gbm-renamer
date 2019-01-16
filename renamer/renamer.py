#Natives from Py
import os
import platform
import time

#Selenium Manager
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#From project dirs
from exceptions import CredentialInvalid
from services import BusinessService
from config import BASE_DIR, WAIT_TIME
from constants import TEXT_PHONE_VERIFICATION
from logger import UploaderLogger
from messages import *


logger = UploaderLogger()
success_logger = UploaderLogger('success')

class Google_Bussiness_auth:
    def __init__ (self):
        pass

    def RunDriver(self):
        if platform.system() == 'Windows':
           self.driver = webdriver.Chrome(
               executable_path=os.path.join(BASE_DIR, 'chromedriver'),
                # chrome_options=chrome_options
            )
        else:
            self.driver = webdriver.Chrome(
                # chrome_options=chrome_options
            )
        self.wait = WebDriverWait(self.driver, WAIT_TIME)
        self.driver.get('https://accounts.google.com/ServiceLogin')

    def do_login(self, credential):
        logger(instance=credential)
        target_element_in_browser = self.driver.find_element_by_id('identifierId')
        target_element_in_browser.send_keys(credential.email + Keys.RETURN)
        time.sleep(1)
        
        target_element_in_browser = self.wait.until(
            EC.element_to_be_clickable((By.NAME, 'password'))
        )
        target_element_in_browser.send_keys(credential.password + Keys.RETURN)
        time.sleep(1)
        

OGBAuth = Google_Bussiness_auth()

class Renamer(): #Master for robot

    service_biz = BusinessService()
    biz_list = None

    def __init__(self, *args):
        self.__nameApp = type(self).__name__ + " bot "
        pass

    def handle(self, *args, **options):
        file_index = 0
    
        #credential_list = self.service_cred.get_list()
        #Hard-Coding - BEGIN (Credential)
        class cFake : 
            def __init__ (self):
                self.email = "laurencebeadle7@gmail.com"
                self.password = "3AF5qCXZbA"
            def report_fail(self):
                print ("cFake: Reporting fail")

        credential_1 = cFake()
        #credential_list = [credential_1] # With Values
        credential_list = [] # Empty
        #Hard-Coding - END (Credential)

        #Dummie, if credential is ZERO. Stop Robot
        if len(credential_list) == 0 :
            
            #logger(data= __nameApp + Credentials_problem_0001)
            print (self.__nameApp + Credentials_problem_0001)
            return 

        # Looping each credenditals (Here we start loop and also run driver)
        # Method 1X1
        for credential in credential_list:

            # THERE VERIFICATION
            # CONSIDERATE EMAIL IS EMAIL. WITH @ ALSO
            # PASSWORD (NOTHING SPECIAL)

            OGBAuth.RunDriver()          
            try:
                OGBAuth.do_login(credential)
            except CredentialInvalid:
                logger(instance=credential, data='Reported fail')
                credential.report_fail()
                OGBAuth.RunDriver().quit()
                continue
            except Exception as e:
                text = OGBAuth.driver.find_element_by_xpath('//body').text.strip()

                if "t find your Google Account" in text:
                    logger(instance=credential, data="Account doesn't exists.")
                    logger(instance=credential, data='Reported fail')
                    #credential.report_fail()
                    continue
                elif "Account disabled" in text:
                    logger(instance=credential, data="Account disabled.")
                    logger(instance=credential, data='Reported fail')
                    #credential.report_fail()
                    continue
                else: 
                    '''
                    self.driver.get(
                        'https://business.google.com/manage/?noredirect=1#/upload'
                    )
                    if not self.driver.current_url.startswith(
                        'https://business.google.com/'
                    ):
                        logger(instance=credential, data='Pass')
                        self.driver.quit()
                        continue
                    '''
