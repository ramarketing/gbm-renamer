#Natives from Py
import os
import platform
import time
import sys
import re
import time, threading
import requests
import json

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

class ThreadsWatch:
    def __init__(self):
        self.ListThreads = dict()
        # ID:1 - Name: VarThreads
        # ----
    def Stop_Threads(self,id):
        pass

    def GetList(self):
        return None

    def addThread (self, target, name):
        self.ListThreads[name] = target
        return True

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
        self.thread=threading.Thread(target=self.__MWatcher)
        self.thread.start()
        TWatch.addThread(self, 'controller_login')
        if (block == True):
            self.thread.join()

    def __MWatcher(self) :
        nextTime=time.time()+self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime+=self.interval
            if (self.Data != False and self.Object != False and self.Function != False):
                eval(self.Object + '.' + self.Function + '(' + 'self.Data' +')')
                #eval('OGAuth.W_do_login(self.Data)')
    def cancel(self) :
        self.stopEvent.set()

class Manage_Selenium :
    def __init__():
        pass

    def CheckField_Exist_by_xpath(self, xpath):
        try:
            time.sleep(1)
            self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            print ("No se encontro")
            return False
        return True

    def Get_outerHTML_and_check_partial_text_via_xpath(self, xpath, string):
        try:
            time.sleep(1)
            self.driver.find_element_by_xpath(xpath).get_attribute('outerHTML')
        except NoSuchElementException:
            return False
        target = self.driver.find_element_by_xpath(xpath).get_attribute('outerHTML')
        if (string in target) :
            return True
        else:
            return False

    def Get_outerHTML_and_check_partial_text_via_target(self, target, string):
        try:
            time.sleep(1)
            target.get_attribute('outerHTML')
        except NoSuchElementException:
            return False
        target = target.get_attribute('outerHTML')
        if (string in target) :
            return True
        else:
            return False

    def GetText_IntoXpath (self, xpath):
        try:
            self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            return False
        target = self.driver.find_elements_by_xpath(xpath)
        return target

    def FillField_by_xpath(self, string, xpath, Enter=False):
        try:
            Target = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        time.sleep(1)
        Target.clear()
        if (Enter == True) :
            Target.send_keys(string + Keys.RETURN)
        return True

    def Click_by_xpath(self, xpath) :
        try:
            Target = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        time.sleep(1)
        Target.click()
        return True

class Google_auth(Manage_Selenium):
    def __init__ (self):
        self.ItSelf = "Google_Auth"

    def NameClass_itSelf(self):
        return self.__class__.__name__

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
        self.Target_User_field_by_xpath = '//*[@id="identifierId"]'
        self.Target_Wrong_User_field_by_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]/div/div[2]/div[2]/div'
        self.Target_Password_field_by_xpath = '//*[@id="password"]/div[1]/div/div[1]/input'
        self.Target_Wrong_Password_message_by_xpath = '//*[@id="password"]/div[2]/div[2]/div'
        self.Target_Text_Verify_are_you_by_xpath = '//*[@id="headingText"]'
        self.Target_Email_Confirm_field_by_xpath = '//*[@id="identifierId"]'
        self.Target_Confirm_Recovery_email_button_by_xpath = '//*[@id="view_container"]/form/div[2]/div/div/div/ul/li[1]/div'
        self.Target_Wrong_Recovery_email_by_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[2]/div/div/div[2]/div[2]/div'
        self.Target_Confirm_message_email_recovery_by_xpath = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[1]'
        self.Target_Step3_asking_captcha = '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/content/section/div/content/div[2]/div/div/div[1]/div/div[1]/div'
        self.Target_Step3_ConfirmField_changing_password = '//*[@id="confirm-passwd"]/div[1]/div/div[1]/div'

        self.LoginStep = 1
        self.LoginStep_ghost = 1
        self.StepError = 0


    def Except_CredentialInvalid (self, credential):
        logger(instance=credential, data='Reported fail')
        credential.report_fail()


    #W -- > Denote methos in mode Watcher with (MWatcher)
    def W_do_login(self, credential):
        print ("! Executing MWatcher GAuth:W_do_login !")
        print ("! LoginStep: " + str(self.LoginStep))
        print ("! LoginStep_ghost: " + str(self.LoginStep_ghost))
        print ("! URL Actually: " + self.driver.current_url)

        if (self.LoginStep == 1) :
            if (self.CheckField_Exist_by_xpath(self.Target_User_field_by_xpath) == True and self.LoginStep == 1):
                print ("# User field detected ")  #OK
                if (self.FillField_by_xpath(credential.email, self.Target_User_field_by_xpath, True) == True):
                    print ("# Success to FillField: User also with Enter")  #OK
                    self.LoginStep_ghost = 11

                if (self.LoginStep_ghost == 11):
                    if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Wrong_User_field_by_xpath, Step1_Target_PTXT_Error_Email) == True) :
                        logger(instance_itself=self.NameClass_itSelf(), data=Email_wasnot_valid)
                        print (Email_wasnot_valid)
                        self.Except_CredentialInvalid(credential)
                        self.driver.quit()
                        TWatch.ListThreads['controller_login'].cancel()
                    else :
                        self.LoginStep = 2
                        print ("#Prepared to go to Step #2")

        if (self.LoginStep == 2) :
            if (self.CheckField_Exist_by_xpath(self.Target_Password_field_by_xpath) == True):
                print ("# Password field detected ")  #OK
                if (self.FillField_by_xpath(credential.password, self.Target_Password_field_by_xpath, True) == True):
                    self.LoginStep_ghost = 21
                    print ("# Success to FillField: Password also with Enter")  #OK

                if (self.LoginStep_ghost == 21) :
                    if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Wrong_Password_message_by_xpath, Step2_Target_PTXT_Error_Password) == True) :
                        logger(instance_itself=self.NameClass_itSelf(), data=Passwword_no_valid)
                        print (Passwword_no_valid)
                        self.Except_CredentialInvalid(credential)
                        self.driver.quit()
                        TWatch.ListThreads['controller_login'].cancel()
                    else :
                        self.LoginStep = 3
                        print ("#Prepared to go to Step #3")
        #There we verify if we access directly without verification of Recovery Email
        if(self.driver.current_url.find('myaccount.google.com') != -1 and self.LoginStep == 3):
            print ("! Login successfull without verification")
            self.SucessLogin = 1
            TWatch.ListThreads['controller_login'].cancel()
        if (self.LoginStep == 3) :
            if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Text_Verify_are_you_by_xpath, Step3_Target_PTXT_Verify_are_you_GAUTH) == True):
                print ("! Detectamos: Are you? body:Header") #OK

                if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_Recovery_email_button_by_xpath, Step3_Target_PTXT_Confirm_email) == True):
                    print ("! Button clicked - Email Recovery")
                    self.Click_by_xpath(self.Target_Confirm_Recovery_email_button_by_xpath)
                    self.LoginStep_ghost = 31
                else :
                    self.LoginStep_ghost = 31
                if (self.LoginStep_ghost == 31):
                    if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_message_email_recovery_by_xpath, Step3_Target_PTXT_Confirm_your_email) == True and self.LoginStep_ghost == 31 ) :
                        self.LoginStep_ghost = 32
                        print ("! Stage to fillfield recovery_email")
                if (self.LoginStep_ghost == 32) :
                    if (self.FillField_by_xpath(credential.recovery_email, self.Target_Email_Confirm_field_by_xpath, True) == True):
                        print ("# Success to FillField: Recovery Email also with Enter")
                        self.LoginStep_ghost = 33
            if (self.LoginStep_ghost == 33) :
                if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Wrong_Recovery_email_by_xpath, Step3_Target_PTXT_Error_Email_Recovery) == True):
                    logger(instance_itself=self.NameClass_itSelf(), data=Acc_invalid_email_recovery)
                    print (Acc_invalid_email_recovery)
                    self.Except_CredentialInvalid(credential)
                    self.driver.quit()
                    TWatch.ListThreads['controller_login'].cancel()
                else:
                    print(self.driver.current_url.find('https://myaccount.google.com'))
                    if(self.driver.current_url.find('https://myaccount.google.com') != -1):
                        print ("! Login successfull.. ")
                        self.SucessLogin = 1
                        TWatch.ListThreads['controller_login'].cancel()
                    else:
                        print ("! Myaccount page not loaded yet ! ")

            if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Step3_asking_captcha, Step3_Target_PTXT_Write_that_you_hear_or_see) == True):
                print ("! Acccount was exploited, Right now are asking for captcha. No procedd")
                self.Except_CredentialInvalid(credential)
                self.driver.quit()
                TWatch.ListThreads['controller_login'].cancel()

            if (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Step3_ConfirmField_changing_password, Step3_Target_PTXT_Step3_Confirmation_password_Field) == True):
                print ("! Acccount was exploited, Right now are asking for change of password. No procedd")
                self.Except_CredentialInvalid(credential)
                self.driver.quit()
                TWatch.ListThreads['controller_login'].cancel()


class GBusiness (Manage_Selenium):
    #Go{name_part_of_site} - Go to a part of Google Business
    #DetectDialog{ID} - What Dialog?
    def __init__ (self):

        self.MainPage = "https://business.google.com/"
        self.Url_List_of_business = 'https://business.google.com/locations'

        # Control of flow Verify_an_business_step {MWatcher}
        self.W_Verify_an_business_step = 0
        self.W_Verify_an_business_Match = False

        #Handlers_XPath para (W_Verify_an_business) - BEGIN
        self.W_Verify_an_business_Target_TBody_Locations = '//*[@id="main_viewpane"]/c-wiz[1]/div/c-wiz[3]/div/content/c-wiz[2]/div[2]/table/tbody'

        self.W_Verify_an_business_Target_Text_to_sendVerify_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div/div[1]/div/div[2]/button[2]'
        #Handlers_XPath para (W_Verify_an_business) - END

        self.W_Verify_an_business_Target_Text_Box_Enter6Digit = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/p'

        self.W_Verify_an_business_Target_EnterVerifyCode_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'

        self.W_Verify_an_business_Target_PhoneNumber = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/p/strong'

    def setDriver (self, driver):
        self.driver = driver
        return True

    def GoMainPage (self):
        print ("! - GBusiness-> Redirecting to: " +  self.MainPage)
        self.driver.get(self.MainPage)

    def GoLocationsPage(self):
        print ("! - GBusiness-> Redirecting to: " +  self.Url_List_of_business)
        self.driver.get(self.Url_List_of_business)
        return True

    def GettingElement_by_xpath(self, xpath):
        try:
            Value_of_return = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return Value_of_return

    def GettingElements_by_tag_name_with_target (self, target, tagname):
        try:
            Value_of_return = target.find_elements_by_tag_name(tagname)
        except NoSuchElementException:
            return False
        return Value_of_return


    def W_Verify_an_business(self, credential):

        print ("W_Verify_an_business_step -> MWatcher Running")
        print ("W_Verify_an_business_step: " + str(self.W_Verify_an_business_step))

        time.sleep(1)

        # Verify_an_business_step:
        # Codigos:
        # 1 - Lista de negocios
        # 11 - Pedimos lista de negocios con https://business.google.com/locations
        # 12 - Obteniendo la lista
        # 13 - Targeteando a la empresa
        # 14 - Clicleando el Verify Now
        # 2 - Detectando "Chosse a way to verify"
        # 21 - Detectamos el boton "text"
        # 22 - Hacemos clic, Loop con Matrix (120 timeout)
        # 21 - Detectamos el Enter code
        # 22 - Ingresando codigo
        # 23 - Espera y clic en Verify now.

        # 1 - Lista de negocios - BEGIN
        if (self.W_Verify_an_business_step == 0) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            if (self.GoLocationsPage() == True):
               self.W_Verify_an_business_step = 1
        # 1 - Lista de negocios - END

        # 11 - Lista de negocios - BEGIN
        if (self.W_Verify_an_business_step == 1) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            if (self.W_Verify_an_business_Match == False) :
                self.Google_Business_Locations_Data_Table_Target_Selenium = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_TBody_Locations)
                if (self.Google_Business_Locations_Data_Table_Target_Selenium != False) :
                    Rows_Table = self.GettingElements_by_tag_name_with_target(self.Google_Business_Locations_Data_Table_Target_Selenium, 'tr')
                    for Item in Rows_Table:
                        Columns = Rows_Table = self.GettingElements_by_tag_name_with_target(Item, 'td')
                        if(self.Get_outerHTML_and_check_partial_text_via_target(Columns[2], credential.name) == True) :
                            print ("! - La empresa es: " + credential.name)
                            print ("! - Salida del HTML: " + Columns[2].get_attribute('outerHTML'))
                            print ("! - Match de la empresa")
                            self.W_Verify_an_business_Match_Columns = Columns
                            self.W_Verify_an_business_Match = True
                            break
                        else:
                            print ("! - No existe la empresa")
            else:
                self.W_Verify_an_business_Match_Columns[4].click()
                print ("! - Hicimos click en verify now.")
                time.sleep(1)
                self.W_Verify_an_business_step = 2
                #self.W_Verify_an_business_step = 2

        if (self.W_Verify_an_business_step == 2) :
            print ("! - Estamos en chosse a way (Verify now.")
            TextButton = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_Text_to_sendVerify_xpath)
            if (TextButton != False):
                print ("! - Hicimos click en Text button.")
                TextButton.click()
                self.W_Verify_an_business_step = 21
            Box_Enter6Digit = self.Get_outerHTML_and_check_partial_text_via_xpath(self.W_Verify_an_business_Target_Text_Box_Enter6Digit, Step_Enter6Digits_Text_fromVerifynow_bussiness)
            if (Box_Enter6Digit == True ):
                self.W_Verify_an_business_step = 21

        if (self.W_Verify_an_business_step == 21) :
            print ("! - Consultando a la Matrix sobre el codigo")
            GB_phoneNumber = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_PhoneNumber).text
            GB_phoneNumber = GB_phoneNumber.replace('(', '').replace(')', '').replace('-', '').strip()
            GB_phoneNumber = '+1{}'.format(GB_phoneNumber)
            GB_phoneNumber = GB_phoneNumber.replace(' ', '')
            print ("Numero de telefono :" + GB_phoneNumber)
            status_code = 204
            while(status_code == 204):
                time.sleep(10)
                response = credential.get_validation_code(
                phone_number=GB_phoneNumber
                )
                status_code = response.status_code
                response_json = response.json()
                if 'msg' in response_json:
                    code = response_json['msg']

                if (response.status_code not in (200, 204)):
                    print('! -Imposible porque', response_json['phone_number'])
                    # credential.report_fail() # Do not report as fail here, YET.
                    TWatch.ListThreads['W_Verify_an_business'].cancel()
                    break
            if (self.FillField_by_xpath(str(code), self.W_Verify_an_business_Target_EnterVerifyCode_xpath, True) == True):
                    self.W_Verify_an_business_step == 23

        if (self.W_Verify_an_business_step == 23) :
            ButtonText = self.GettingElement_by_xpath()



        # 11 - Lista de negocios - END

class Renamer(): #Master for robot
    service_biz = BusinessService()
    biz_list = None
    def __init__(self, *args):
        self.__nameApp = type(self).__name__ + " bot "
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
        from services import BusinessService
        business_service = BusinessService()
        business_list = business_service.get_list()

        counter = 0
        self.credential_list = business_list
        for credential in self.credential_list:

            #counter = counter + 1
            #if (counter == 1) :
            #    credential.report_fail()

            OGAuth.SucessLogin = 0 # SuccessLogin Default: 0
            print(credential.name, credential.email , credential.password, credential.recovery_email)
            if (self.verification_of_credential(credential) == False) :
                logger(instance_itself=self.NameClass_itSelf(), data=Skiping_to_next_credential)
                print (Skiping_to_next_credential)
                continue
            # THERE VERIFICATIONfrom services import BusinessService
            # CONSIDERATE EMAIL IS EMAIL. WITH @ ALSO
            # PASSWORD (NOTHING SPECIAL)
            if (self.is_Driver_GAuth_loaded() == True) :
                OGAuth.RunDriver()
            try:
                print ("# Email: " + credential.email)
                Controller_Login = MWatcher(0.5, 'OGAuth', 'W_do_login' , credential, True)
            except CredentialInvalid:
                continue
            if (OGAuth.SucessLogin == 1) :
                print ("Setting up driver for Google Bussiness")
                GBusiness_handle.setDriver(OGAuth.driver)
                print ("Sleeping 1s")
                time.sleep(1)
                VerifyBusiness = MWatcher(0.5, 'GBusiness_handle', 'W_Verify_an_business' , credential, True)

        self.Finished_app()

    def Finished_app(self):
        logger(instance_itself=self.NameClass_itSelf(), data=self.__nameApp + Finished_app_run)
        print (self.__nameApp + Finished_app_run)
        #self.CloseApp()


# Intialization of object.
OGAuth = Google_auth() #Same for all clasess
GBusiness_handle = GBusiness()
#Matrix_Handle = Matrix()
TWatch = ThreadsWatch()
logger = Logger()
success_logger = Logger('success')
