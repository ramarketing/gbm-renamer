#Natives from Py
import os
import platform
import time
import sys
import re

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
from logger import Logger
from messages import *


logger = Logger()
success_logger = Logger('success')

class Google_auth:
    def __init__ (self):
        self.ItSelf = "Google_Auth"

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

# Intialization of object.
OGAuth = Google_auth() #Same for all clasess


class Renamer(): #Master for robot

    service_biz = BusinessService()
    biz_list = None

    def __init__(self, *args):
        self.__nameApp = type(self).__name__ + " bot "
        self.credential_list = [] # Initilizatiion
        pass

    def NameClass_itSelf(self):
        return self.__class__.__name__

    def is_Driver_GAuth_loaded(self):
        if OGAuth is not None: 
            return True
        else :    
            logger(instance_itself=self.NameClass_itSelf(), data=OGAuth_not_loaded)
            print (self.__nameApp + OGAuth_not_loaded)            
            self.CloseApp()
            return False
            
    def is_empty_credentials (self) :
        if len(self.credential_list) == 0 :
            logger(instance_itself=self.NameClass_itSelf(), data=Credentials_problem_0001)
            print (self.__nameApp + Credentials_problem_0001)
            return True
        else :
            return False

    def is_valid_email (self, email):
        valid_re = re.compile(r'^.+@.+')
        if(valid_re.match(email)):
            return True
        else:
            return False

    def verification_of_credential(self, credential=None):
        try:
            print (credential.email)
        except AttributeError:
            logger(instance_itself=self.NameClass_itSelf(), data=Object_Credential_novalid + ": email")
            print (Object_Credential_novalid + ": email")                

        try:
            print (credential.recovery_email)
        except AttributeError:
            logger(instance_itself=self.NameClass_itSelf(), data=Object_Credential_novalid + ": recovery_mail")
            print (Object_Credential_novalid + ": recovery_email")                

        try:
            print (credential.password)
        except AttributeError:
            logger(instance_itself=self.NameClass_itSelf(), data=Object_Credential_novalid + ": password")
            print (Object_Credential_novalid + ": password")                


        if (self.is_valid_email(credential.email) == False) :
            logger(instance_itself=self.NameClass_itSelf(), data=self.credential.email + " " + Email_wasnot_valid)
            print (self.credential.email + Email_wasnot_valid)                
            # THERE THIS LINE WE CAN ADD EXTRA VERIFICATION
            return False     
        if (self.is_valid_email(credential.recovery_email) == False) :
            logger(instance_itself=self.NameClass_itSelf(), data=self.credential.email + " " + Email_wasnot_valid)
            print (self.credential.email + Email_wasnot_valid)                
            # THERE THIS LINE WE CAN ADD EXTRA VERIFICATION
            return False     
        if (len(credential.password)  < 6):
            logger(instance_itself=self.NameClass_itSelf(), data="For mail: " + self.credential.email + " " + Passwword_no_valid)
            print ("For mail: " + self.credential.email + " " + Passwword_no_valid  )                            
            return False
        return True

    def CloseApp(self) : 
        logger(instance_itself=self.NameClass_itSelf(), data= self.__nameApp + Application_was_closed)
        print (Application_was_closed)
        sys.exit()

    def handle(self, *args, **options):
        file_index = 0
        #credential_list = self.service_cred.get_list()
        #Hard-Coding - BEGIN (Credential)
        class cFake :
            def __init__ (self):
                #self.email = "fake100"
                self.email = "drabblefabe@gmail.com"
                self.password = "XyN6Lm5Apf"
                self.recovery_email = "vernenl00dk@outlook.com"
            def report_fail(self):
                print ("cFake: Reporting fail")

        credential_fake_1 = cFake()
        self.credential_list = [credential_fake_1] # With Values
        #self.credential_list = [] # Empty
        #Hard-Coding - END (Credential)
        if (self.is_empty_credentials() == True) :
            self.CloseApp()
        #Dummie, if credential is ZERO. Stop Robot
        # Looping each credenditals (Here we start loop and also run driver)
        # Method 1X1

        for credential in self.credential_list:
            if (self.verification_of_credential(credential) == True) :
                continue

            # THERE VERIFICATION
            # CONSIDERATE EMAIL IS EMAIL. WITH @ ALSO
            # PASSWORD (NOTHING SPECIAL)
            if (self.is_Driver_GAuth_loaded() == True) :
                OGAuth.RunDriver()
            try:
                OGAuth.do_login(credential)          
            except CredentialInvalid:
                logger(instance=credential, data='Reported fail')
                credential.report_fail()
                OGBAuth.RunDriver().quit()
                continue
            except Exception as e:
                text = OGAuth.driver.find_element_by_xpath('//body').text.strip()

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

        self.Finished_app()


    def Finished_app(self):
        logger(instance_itself=self.NameClass_itSelf(), data=self.__nameApp + Finished_app_run)
        print (self.__nameApp + Finished_app_run)


