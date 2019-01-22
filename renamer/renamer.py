#Natives from Py
import os
import platform
import time
import sys
import re
import time, threading


#Selenium Manager
from selenium import webdriver
from selenium.common.exceptions import ElementNotVisibleException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#From project dirs
from exceptions import CredentialInvalid
from services import BusinessService
from config import BASE_DIR, WAIT_TIME
from constants import TEXT_PHONE_VERIFICATION
from logger import Logger
from messages import *
logger = Logger()
success_logger = Logger('success')


class ThreadsWatch:
    def __init(self):
        self.ListThreads = list() 
        # ID:1 - Name: VarThreads
        # ----
    def Stop_Threads(self,id):
        pass

    def GetList(self):
        return None

    def CheckStatus_thread_by_id(self,id):
        pass

    def Block_Thread_by_id (self, id):
        pass

    def ClasurePythonicApp():
        #Kill app
        #Generate a logger
        # - What Thread faild and where.
        pass

class MWatcher :
    def __init__(self,interval,object_name=False, function_name=False, data_to_load=False, block=False) :
        self.interval=interval
        self.stopEvent=threading.Event()
        self.Object = object_name
        self.Function = function_name
        self.Data = data_to_load 
        thread=threading.Thread(target=self.__MWatcher)
        thread.start()
        if (block == True):
            thread.join()


    def __MWatcher(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            if (self.Data != False and self.Object != False and self.Function != False):
                eval(self.Object + '.' + self.Function + '(' + 'self.Data' +')')
                #eval('OGAuth.W_do_login(self.Data)')
    def cancel(self) :
        self.stopEvent.set()
        
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
        self.Target_User_field_by_xpath = '//*[@id="identifierId"]1'
        self.Target_User_field_by_id = 'identifierId'
        self.Target_Password_field_by_name = 'password'
        self.Target_Wrong_Password_message_by_xpath = '//*[@id="password"]/div[2]/div[2]/div'
        self.Target_Confirm_Recovery_email_button_by_xpath = '//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[1]/div'
        self.Target_Email_Confirm_field_by_id = '//*[@id="identifierId"]'
        self.LoginStep = 1
        self.ErrorStatus = False

    def testing(self):
        pass


    def CheckField_Exist_by_xpath(self, xpath):
        try:
            self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            print ("No se encontro")
            return False
        
        return True

    #W -- > Denote methos in mode Watcher with (MWatcher)
    def W_do_login(self, credential):

        #LoginStep == 1 :: Showing just Login field
        if (self.LoginStep == 1) : 
            if (self.CheckField_Exist_by_xpath(self.Target_User_field_by_xpath) == True):
                self.LoginStep = 2



    def do_login(self, credential):

        logger(instance=credential)

        target_element_in_browser = self.driver.find_element_by_id(User_field_by_id)
        target_element_in_browser.send_keys(credential.email + Keys.RETURN)

        time.sleep(1)
        target_element_in_browser = self.wait.until(
            EC.element_to_be_clickable((By.NAME, Password_field_by_name))
        )

        time.sleep(1)
        target_element_in_browser.send_keys(credential.password + Keys.RETURN)
        time.sleep(1)

        #Trying to search if message wrong message are there
        target_element_in_browser = self.driver.find_element_by_xpath(Wrong_Password_message_by_xpath)

        time.sleep(1)
        self.driver.find_element_by_xpath(Confirm_Recovery_email_button_by_xpath).click();
        time.sleep(1)

        target_element_in_browser = self.driver.find_element_by_xpath(Email_Confirm_field_by_id)
        target_element_in_browser.send_keys(credential.recovery_email + Keys.RETURN)


# Intialization of object.
OGAuth = Google_auth() #Same for all clasess

#Class HardCode for Credential object. 
class cFake :
    def __init__ (self):
        self.email = "lacychristoph@gmail.com"
        self.password = "KAx7TqwRdd"
        self.recovery_email = "sigbsn55j@hotmail.com"

    def report_fail(self):
        print ("cFake: Reporting fail")


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
            credential.email
        except AttributeError:
            logger(instance_itself=self.NameClass_itSelf(), data=Object_Credential_novalid + ": email")
            print (Object_Credential_novalid + ": email")                
        try:
            credential.recovery_email
        except AttributeError:
            logger(instance_itself=self.NameClass_itSelf(), data=Object_Credential_novalid + ": recovery_mail")
            print (Object_Credential_novalid + ": recovery_email")                
        try:
            credential.password
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

        credential_fake_1 = cFake()
        self.credential_list = [credential_fake_1] # With Values
        #self.credential_list = [] # Empty
        #Hard-Coding - END (Credential)
        if (self.is_empty_credentials() == True) :
            self.CloseApp()
        #Dummie, if credential is ZERO. Stop Robot
        # Looping each credenditals (Here we start loop and also run driver)
        # Method 1X1 (First method)
        for credential in self.credential_list:
            if (self.verification_of_credential(credential) == False) :
                logger(instance_itself=self.NameClass_itSelf(), data=Skiping_to_next_credential)
                print (Skiping_to_next_credential)
                continue
            # THERE VERIFICATION
            # CONSIDERATE EMAIL IS EMAIL. WITH @ ALSO
            # PASSWORD (NOTHING SPECIAL)
            if (self.is_Driver_GAuth_loaded() == True,) :
                OGAuth.RunDriver()
            try:
                Controller_Login = MWatcher(0.5, 'OGAuth', 'W_do_login' ,credential, True)
                # Si el block funciona, esto jamas deberia de funcionar hasta que terminemos el thread
                print ("Controller_login (BLOCK failing)")
                          
            except CredentialInvalid:
                logger(instance=credential, data='Reported fail')
                credential.report_fail()
                OGBAuth.RunDriver().quit()
                continue

        self.Finished_app()


    def Finished_app(self):
        logger(instance_itself=self.NameClass_itSelf(), data=self.__nameApp + Finished_app_run)
        print (self.__nameApp + Finished_app_run)
        #self.CloseApp()


