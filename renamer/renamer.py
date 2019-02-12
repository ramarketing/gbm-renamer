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
from config import BASE_DIR, WAIT_TIME, RETRY_AT, MAX_RETRIES
from constants import TEXT_PHONE_VERIFICATION
from logger import Logger
from messages import *
from services import BusinessService


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

    def ClasurePythonicApp(self):
        #Kill app
        #Generate a logger
        # - What Thread faild and where.
        pass

class MWatcher :
    def __init__(self,interval, VarInit, object_name=False, function_name=False, pretty_name_process=None, data_to_load=False, block=False) :
        self.interval=interval
        self.stopEvent=threading.Event()
        self.Object = object_name
        self.Function = function_name
        self.pretty_name_process = pretty_name_process
        self.Data = data_to_load
        self.thread=threading.Thread(target=self.__MWatcher)
        self.thread.start()

        TWatch.addThread(self, VarInit)
        if (block == True):
            self.thread.join()

    def __MWatcher(self) :
        nextTime = time.time() + self.interval
        while not self.stopEvent.wait(nextTime-time.time()) :
            nextTime += self.interval
            if (self.Data != False and self.Object != False and self.Function != False):
                eval(self.Object + '.' + self.Function + '(' + 'self.Data' +')')
                #eval('OGAuth.W_do_login(self.Data)')

    def cancel(self) :
        print(TWatch_Cancel + self.pretty_name_process)
        self.stopEvent.set()

class Manage_Selenium :
    def __init__(self):
        self.driver = False
        pass

    def CheckField_Exist_by_xpath(self, xpath):
        try:
            time.sleep(1)
            self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            print('No se encontro el elemento "{}"'.format(xpath))
            return False
        return True

    def Get_outerHTML_and_check_partial_text_via_xpath(self, xpath, string):
        try:
            time.sleep(1)
            target = self.driver.find_element_by_xpath(xpath).get_attribute('outerHTML')
        except NoSuchElementException:
            target = False
        return string in target if target else False

    def Get_outerHTML_and_check_partial_text_via_target(self, target, string):
        try:
            time.sleep(1)
            target = target.get_attribute('outerHTML')
        except NoSuchElementException:
            target = None
        return string in target if target else False

    def GetText_IntoXpath (self, xpath):
        try:
            target = self.driver.find_elements_by_xpath(xpath)
        except NoSuchElementException:
            target = False
        return target

    def FillField_by_xpath(self, string, xpath, Enter=False):
        try:
            target = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        time.sleep(1)

        try:
            target.clear()
        except:
            pass
        if (Enter == True) :
            target.send_keys(string + Keys.RETURN)
        return True

    def Click_by_xpath(self, xpath) :
        try:
            target = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        time.sleep(1)
        target.click()
        return True

    def GettingElement_by_xpath(self, xpath):
        try:
            value = self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        return value

    def GettingElements_by_tag_name_with_target (self, target, tagname):
        try:
            return target.find_elements_by_tag_name(tagname)
        except NoSuchElementException:
            return False


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

    def Except_CredentialInvalid(self, credential):
        logger(instance=credential, data='Reported fail')
        credential.report_fail()

    #W -- > Denote methods in mode Watcher with (MWatcher)
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
            if (
                self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Text_Verify_are_you_by_xpath, Step3_Target_PTXT_Verify_are_you_GAUTH) == True or
                self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Text_Verify_are_you_by_xpath, Step3_Target_PTXT_Verify_are_you_GAUTH_en) == True
            ):
                print ("! Detectamos: Are you? body:Header") #OK
                if (
                    self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_Recovery_email_button_by_xpath, Step3_Target_PTXT_Confirm_email) == True or
                    self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_Recovery_email_button_by_xpath, Step3_Target_PTXT_Confirm_email_en) == True
                ):
                    print ("! Button clicked - Email Recovery")
                    self.Click_by_xpath(self.Target_Confirm_Recovery_email_button_by_xpath)
                    self.LoginStep_ghost = 31
                else :
                    self.LoginStep_ghost = 31
                if (self.LoginStep_ghost == 31):
                    if (
                        (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_message_email_recovery_by_xpath, Step3_Target_PTXT_Confirm_your_email) == True and self.LoginStep_ghost == 31) or
                        (self.Get_outerHTML_and_check_partial_text_via_xpath(self.Target_Confirm_message_email_recovery_by_xpath, Step3_Target_PTXT_Confirm_your_email_en) == True and self.LoginStep_ghost == 31)
                    ):
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

        #URL TO REDIRECT IN SAME GOOGLE -- BEGIN
        self.MainPage = "https://business.google.com/"
        self.Url_List_of_business = 'https://business.google.com/'
        #URL TO REDIRECT IN SAME GOOGLE -- END


        # Control of flow Verify_an_business_step - BEGIN
        self.W_Verify_an_business_step = 0
        self.W_Verify_an_business_Match = False
        # Control of flow Verify_an_business_step - END

        # Control of flow Verify_an_business_step - BEGIN
        self.W_Update_an_business_step = 0
        self.W_Update_an_business_Match = False
        # Control of flow Verify_an_business_step - END


        # Return from control Flow  - BEGIN
        self.Verify_an_business_Skip = False
        # Return from control Flow  - END

        #Handlers_XPath para (W_Verify_an_business) - BEGIN
        self.W_Verify_an_business_Target_TBody_Locations_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/c-wiz[3]/div/content/c-wiz[2]/div[2]/table/tbody'
        self.W_Verify_an_business_Target_Text_to_sendVerify_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div/div[1]/div/div[2]/button[2]'
        self.W_Verify_an_business_Target_Text_Box_Enter6Digit_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/p'
        self.W_Verify_an_business_Target_EnterVerifyCode_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div/div[1]/input'
        self.W_Verify_an_business_Target_PhoneNumber_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div/div[1]/div/div[1]/h3'
        self.W_Verify_an_business_Target_PhoneNumber_xpath_21 = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/p/strong'
        self.W_Verify_an_business_Target_Button_Verify_Now = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div[1]/div[3]/button'
        self.W_Verify_an_business_Target_TextAgain_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div[2]/div/div[1]/button/span'
        self.W_Verify_an_business_Target_Cellphone_rin_rin_xpath = '//*[@id="main_viewpane"]/c-wiz[1]/div/div[2]/div/div/div[1]/div/div[3]/div/div/div'
        #Handlers_XPath para (W_Verify_an_business) - END


        #Handlers_XPATH para (W_update_a_business) - BEGIN

        self.W_Update_an_business_popup_get_started_button_xpath = '//*[@id="js"]/div[10]/div/div[2]/div[3]/div/content'
        self.W_Update_an_business_popup_left_panel_info_xpath = '//*[@id="gb"]/div[4]/div[2]/div/div[1]/div[4]/a/span[2]'

        self.W_Update_an_business_button_edit_name_in_info_page_xpath = '//*[@id="ow47"]/div[2]/svg'
        self.W_Update_an_business_button_edit_category_in_info_page_xpath = '//*[@id="ow48"]/div[2]/svg'

        #self.W_Update_an_business_button_change_name_of_business = '//*[@id="ow48"]/div[1]'
        self.W_Update_an_business_button_change_name_of_business = '//*[@id="main_viewpane"]/div[2]/div/div/div[1]/div[2]/content/div[2]/div[1]'
        self.W_Update_an_business_button_input_name_of_business = '//*[@id="js"]/div[10]/div/div[2]/content/div/div[4]/div/div[1]/div/div[1]/input'
        self.W_Update_an_business_button_apply_name_of_business = '//*[@id="js"]/div[10]/div/div[2]/content/div/div[5]/div[2]/content/span'

        self.W_Update_an_business_button_change_category_of_business = '//*[@id="main_viewpane"]/div[2]/div/div/div[1]/div[2]/content/div[3]/div[1]'
        self.W_Update_an_business_button_input_category_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[4]/div/div[1]/div/div[1]/div[1]/input[2]'
        self.W_Update_an_business_button_apply_category_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[5]/div[2]/content/span'

        self.W_Update_an_business_button_change_description_of_business = '//*[@id="ow36"]/div[1]/div[2]/content/div[11]/div[2]/div'
        self.W_Update_an_business_button_input_description_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[4]/div/div[1]/div[1]/textarea'
        self.W_Update_an_business_button_apply_description_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[5]/div[2]/content/span'

        self.W_Update_an_business_button_change_website_of_business = '//*[@id="main_viewpane"]/div[2]/div/div/div[1]/div[2]/content/div[9]'
        self.W_Update_an_business_button_input_website_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[4]/div[1]/div[1]/div/div[1]/input'
        self.W_Update_an_business_button_apply_website_of_business = '//*[@id="js"]/div[11]/div/div[2]/content/div/div[5]/div[2]/content/span'

        #Control Validations - BEGIN
        self.BusinessValidation = 0
        self.UpdateBusinessValidation = False
        #Control Validations - END

    def setDriver(self, driver):
        self.driver = driver
        return True

    def GoMainPage (self):
        time.sleep(1)
        print ("! - GBusiness-> Redirecting to: " +  self.MainPage)
        self.driver.get(self.MainPage)

    def GoLocationsPage(self):
        time.sleep(3)
        print ("! - GBusiness-> Redirecting to: " +  self.Url_List_of_business)
        self.driver.get(self.Url_List_of_business)
        return True

    def W_Update_an_business(self, credential):
        print ("Here we go with Update Business")
        print ("self.W_Update_an_business_step: " + str(self.W_Update_an_business_step))
        # 1 - Lista de negocios - BEGIN
        if (self.W_Update_an_business_step == 0) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            print ("! - Redirigiendo a la lista de negocios de Google Business")
            self.GoLocationsPage()
            self.W_Update_an_business_step = 3
        # 1 - Lista de negocios - END
        # 11 - Lista de negocios - BEGIN
        if (self.W_Update_an_business_step == 1) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            if (self.W_Update_an_business_Match == False) :
                self.Google_Business_Locations_Data_Table_Target_Selenium = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_TBody_Locations_xpath)
                if (self.Google_Business_Locations_Data_Table_Target_Selenium != False) :
                    Rows_Table = self.GettingElements_by_tag_name_with_target(self.Google_Business_Locations_Data_Table_Target_Selenium, 'tr')
                    Qty_Rows = len(Rows_Table)
                    Counter_Interactios_rows_table = 0
                    for Item in Rows_Table:
                        Counter_Interactios_rows_table += 1
                        Columns = Rows_Table = self.GettingElements_by_tag_name_with_target(Item, 'td')
                        if(
                            (self.Get_outerHTML_and_check_partial_text_via_target(Columns[2], credential.name) == True) or
                            (credential.final_name and (self.Get_outerHTML_and_check_partial_text_via_target(Columns[2], credential.final_name)) == True)):
                            print ("! - La empresa es: " + credential.name)
                            print ("! - Salida del HTML: " + Columns[2].get_attribute('outerHTML'))
                            print ("! - Match de la empresa")
                            self.W_Update_an_business_Match = True
                            self.W_Update_an_business_Match_Columns = Columns

                            if(
                                self.Get_outerHTML_and_check_partial_text_via_target(Columns[3], Status_colum_location_business_Verification_required) == True or
                                self.Get_outerHTML_and_check_partial_text_via_target(Columns[3], Status_colum_location_business_Verification_pending) == True
                            ):
                                print ("! - La empresa no se encuentra verificada, Vamos a veriricarla")
                                break
                            else :
                                credential.report_validation()
                                GBusiness_handle.BusinessValidation = 1
                                TWatch.ListThreads['VerifyBusiness'].cancel()
                                print ("! -No es necesario la verificacion.  La empresa se encuentra verificada. ")
                        else:
                            print ("! - No match con la empresa")
                            if (Counter_Interactios_rows_table == Qty_Rows):
                                print ("!- No hay match con la empresa que estamos buscando.")
                                credential.report_fail()
                                TWatch.ListThreads['VerifyBusiness'].cancel()
                                return
            else:
                try:
                    BusinessTarget = self.W_Update_an_business_Match_Columns[2]
                    try:
                        BusinessTarget.find_element_by_partial_link_text(credential.name).click()
                    except:
                        BusinessTarget.find_element_by_partial_link_text(credential.final_name).click()
                    print ("! - Hicimos click para ingresar a la empresa.")
                    self.W_Update_an_business_step = 2
                except Exception as err:
                    print (err)

        if (self.W_Update_an_business_step == 2) :
            print ("Sleeping 10s for get stared")
            time.sleep(10)

            if (self.Click_by_xpath(self.W_Update_an_business_popup_get_started_button_xpath) == True) :
                pass
            self.W_Update_an_business_step = 3

        if (self.W_Update_an_business_step == 3) :

            #print ("! - Exc : Block 3")
            Edit_Info_url = self.driver.current_url
            Edit_Info_url = Edit_Info_url.replace('dashboard', 'edit')
            try:
                self.driver.get(Edit_Info_url)
                self.W_Update_an_business_step = 4
            except Exception as err:
                print ("! - Error en step 3:")
                print(err)

        if (self.W_Update_an_business_step == 4) :
            Data = dict()
            Data['name'] = credential.final_name
            Data['category'] = credential.final_category_1
            Data['description'] = credential.final_description
            Data['website'] = credential.final_website

            print ("### Values ###")
            print (Data['name'], Data['category'], Data['description'], Data['website'])


            print ("Sleeping 6 seconds for load info page")
            time.sleep(6)
            print ("! - Here we are going to update business")
            for key, value in Data.items():
                if (not value) :
                    print ("Skipping process, why value is false")
                    continue
                print ("El valor de key: " + str(key)  + "  y el valor de value: " + str(value))
                Target_for_change = self.ObtainParam_ToUpdate_Business(key, value)
                if (Target_for_change == False) :
                    print ("! - Key value no exist to update")
                    continue
                time.sleep(1)
                if (self.UpdateBusiness_in_info_page(Target_for_change, key, value) == True) :
                    print ("Change of business done for : " + str(key))
                else :
                    print ("We could not change this value: " + (key))
            self.W_Update_an_business_step = 5

        if (self.W_Update_an_business_step == 5) :
            credential.report_renamed()
            print ("! - La empresa ha sido renombrada. ")
            self.UpdateBusinessValidation = True
            TWatch.ListThreads['UpdateBusiness'].cancel()



            '''
            try:
                self.driver.find_element_by_xpath('//*[@id="ow48"]/div[1]').click()
                self.W_Update_an_business_step = 5
            except:
                pass
            '''

    def UpdateBusiness_in_info_page(self, Params, key, value) :

        print ("! - Internal: Starting process of changing for:  - " + str(key))
        print ("Sleeping 1")
        time.sleep(1)
        if (self.Click_by_xpath(Params['change']) == True ):
            print (" [Button.Change] - Done")
        else:
            print ("[Button.Change] - Error")
            return False
        time.sleep(1)
        if (self.FillField_by_xpath(value, Params['input'], True)  == True) :
            print (" [Fill.Change] - Done")
        else:
            print ("[Fill.Change] - Error")
            return False
        time.sleep(1)
        if (self.Click_by_xpath(Params['apply']) == True) :
            print ("[Button.Click] - Done")
        else:
            print ("[Button.Click] - Error")
            return False
        print ("! - Waiting to save (10 seconds)")
        time.sleep(10)
        return True

    def ObtainParam_ToUpdate_Business (self, key, value):

        '''
        [ self.W_Update_an_business_button_change_name_of_business ]
        [ self.W_Update_an_business_button_input_name_of_business ]
        [ self.W_Update_an_business_button_apply_name_of_business ]

        [ self.W_Update_an_business_button_change_category_of_business ]
        [ self.W_Update_an_business_button_input_category_of_business ]
        [ self.W_Update_an_business_button_apply_category_of_business ]

        [ self.W_Update_an_business_button_change_description_of_business ]
        [ self.W_Update_an_business_button_input_description_of_business ]
        [ self.W_Update_an_business_button_apply_description_of_business ]

        [ self.W_Update_an_business_button_change_website_of_business ]
        [ self.W_Update_an_business_button_input_website_of_business ]
        [ self.W_Update_an_business_button_apply_website_of_business ]
        '''

        ReturnValue = dict()

        if (key == 'name') :
            ReturnValue['change'] = self.W_Update_an_business_button_change_name_of_business
            ReturnValue['input'] = self.W_Update_an_business_button_input_name_of_business
            ReturnValue['apply'] = self.W_Update_an_business_button_apply_name_of_business
        elif (key == 'category') :
            ReturnValue['change'] = self.W_Update_an_business_button_change_category_of_business
            ReturnValue['input'] = self.W_Update_an_business_button_input_category_of_business
            ReturnValue['apply'] = self.W_Update_an_business_button_apply_category_of_business
        elif (key == 'description') :
            ReturnValue['change'] = self.W_Update_an_business_button_change_description_of_business
            ReturnValue['input'] = self.W_Update_an_business_button_input_description_of_business
            ReturnValue['apply'] = self.W_Update_an_business_button_apply_description_of_business
        elif (key == 'website') :
            ReturnValue['change'] = self.W_Update_an_business_button_change_website_of_business
            ReturnValue['input'] = self.W_Update_an_business_button_input_website_of_business
            ReturnValue['apply'] = self.W_Update_an_business_button_apply_website_of_business
        else :
            print ("! - Printing right now value inneed. ")
            return False
        ReturnValue['value'] = value
        return ReturnValue

    def W_Verify_an_business(self, credential):
        print ("W_Verify_an_business_step -> MWatcher Running")
        print ("W_Verify_an_business_step: " + str(self.W_Verify_an_business_step))

        time.sleep(1)

        # Verify_an_business_step:
        # Codigos:
        # 1  - Lista de negocios
        # 11 - Pedimos lista de negocios con https://business.google.com/locations
        # 12 - Obteniendo la lista
        # 13 - Targeteando a la empresa
        # 14 - Clicleando el Verify Now
        # 2 -  Detectando "Chosse a way to verify"
        # 21 - Detectamos el boton "text"
        # 22 - Hacemos clic, Loop con Matrix (120 timeout)
        # 21 - Detectamos el Enter code
        # 22 - Ingresando codigo
        # 23 - Espera y clic en Verify now.
        # 24 - Verificado ya el business


        # 1 - Lista de negocios - BEGIN
        if (self.W_Verify_an_business_step == 0) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            print ("! - Redirigiendo a la lista de negocios de Google Business")
            if (self.GoLocationsPage() == True) :
               self.W_Verify_an_business_step = 1
        # 1 - Lista de negocios - END

        # 11 - Lista de negocios - BEGIN
        if (self.W_Verify_an_business_step == 1) :
            time.sleep(0.25) #Sleeping 0.25 Seconds
            if (self.W_Verify_an_business_Match == False) :
                self.Google_Business_Locations_Data_Table_Target_Selenium = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_TBody_Locations_xpath)
                if (self.Google_Business_Locations_Data_Table_Target_Selenium != False) :
                    Rows_Table = self.GettingElements_by_tag_name_with_target(self.Google_Business_Locations_Data_Table_Target_Selenium, 'tr')
                    Qty_Rows = len(Rows_Table)
                    Counter_Interactios_rows_table = 0
                    for Item in Rows_Table:
                        Counter_Interactios_rows_table += 1
                        Columns = Rows_Table = self.GettingElements_by_tag_name_with_target(Item, 'td')
                        if(
                            self.Get_outerHTML_and_check_partial_text_via_target(Columns[2], credential.name) == True or
                            (credential.final_name and self.Get_outerHTML_and_check_partial_text_via_target(Columns[2], credential.final_name) == True)
                        ):
                            print ("! - La empresa es: " + credential.name)
                            print ("! - Salida del HTML: " + Columns[2].get_attribute('outerHTML'))
                            print ("! - Match de la empresa")
                            self.W_Verify_an_business_Match_Columns = Columns
                            self.W_Verify_an_business_Match = True

                            if(
                                self.Get_outerHTML_and_check_partial_text_via_target(Columns[3], Status_colum_location_business_Verification_required) == True or
                                self.Get_outerHTML_and_check_partial_text_via_target(Columns[3], Status_colum_location_business_Verification_pending) == True
                            ):
                                print ("! - La empresa no se encuentra verificada, Vamos a veriricarla")
                                break
                            else :
                                credential.report_validation()
                                GBusiness_handle.BusinessValidation = 1
                                TWatch.ListThreads['VerifyBusiness'].cancel()
                                print ("! -No es necesario la verificacion.  La empresa se encuentra verificada. ")
                        else:
                            print ("! - No match con la empresa")

                            if (Counter_Interactios_rows_table == Qty_Rows):
                                print ("!- No hay match con la empresa que estamos buscando.")
                                credential.report_fail()
                                TWatch.ListThreads['VerifyBusiness'].cancel()
                                return
            else:
                self.W_Verify_an_business_Match_Columns[4].click()
                print ("! - Hicimos click en verify now.")
                time.sleep(1)
                self.W_Verify_an_business_step = 2



        if (self.W_Verify_an_business_step == 2) :
            time.sleep(5)
            print ("! - We are on choose the way to verify (Verify now.")
            GB_phoneNumber = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_PhoneNumber_xpath)
            if not GB_phoneNumber:
                TWatch.ListThreads['VerifyBusiness'].cancel()
                return
            GB_phoneNumber = GB_phoneNumber.text
            GB_phoneNumber = GB_phoneNumber.replace('(', '').replace(')', '').replace('-', '').replace(' ', '').strip()
            try:
                GB_phoneNumber = int(GB_phoneNumber)
            except ValueError:
                print("This isn't a phone number: ", GB_phoneNumber)
                credential.report_fail()
                TWatch.ListThreads['VerifyBusiness'].cancel()
                return
            GB_phoneNumber = '+1{}'.format(GB_phoneNumber)
            print ("Numero de telefono :" + GB_phoneNumber)

            TextButton = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_Text_to_sendVerify_xpath)

            '''
            1. ¿The phone number is connected?
            yes. Check for the last existing code
            no. Purchase the number
            '''
            code = None
            response = credential.get_validation_code(
                phone_number=GB_phoneNumber
            )
            status_code = response.status_code
            response = response.json()

            if status_code == 200 and 'msg' in response:
                code = response['msg'] if len(response['msg']) == 6 else None
                if code:
                    print ("El code es: {}".format(code))
            elif response['phone_number'][0] == '000000':
                print('! - The phone was just purchased. Please hold 5 seconds.')
                time.sleep(5)
            else:
                print('! - Unable to purchase phone ', response['phone_number'][0])
                credential.report_fail()
                TWatch.ListThreads['VerifyBusiness'].cancel()
                return

            if (TextButton != False):
                print ("! - Hicimos click en Text button.")
                TextButton.click()
                self.W_Verify_an_business_step = 21
            else:
                RinRinCellPhone_Animate = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_Cellphone_rin_rin_xpath)
                if (RinRinCellPhone_Animate == True) :
                    print ("! - Sleeping 1 : RinRin Cellphone Animation appear.")
                    time.sleep(1)
                    Clicking_RinRinCellPhone = self.Click_by_xpath(self.W_Verify_an_business_Target_Cellphone_rin_rin_xpath)
                    if (Clicking_RinRinCellPhone == True):
                        print ("! - Sleeping 1 : RinRin Cellphone Animation appear.")
                        time.sleep(10)
                        print ("! - Sleeping 10 seconds - While Receving sms")

            Box_Enter6Digit = self.Get_outerHTML_and_check_partial_text_via_xpath(self.W_Verify_an_business_Target_Text_Box_Enter6Digit_xpath, Step_Enter6Digits_Text_fromVerifynow_bussiness)
            if (Box_Enter6Digit == True ):
                self.W_Verify_an_business_step = 21

        if (self.W_Verify_an_business_step == 21) :
            print ("! - Sleeping 3s")
            time.sleep(3)

            if (self.Get_outerHTML_and_check_partial_text_via_xpath('Text',self.W_Verify_an_business_Target_TextAgain_xpath)  == True ) :
                print ("TEXT AGAIN EXIST")

            Retries_loop_sms = 0
            GB_phoneNumber = self.GettingElement_by_xpath(self.W_Verify_an_business_Target_PhoneNumber_xpath_21).text
            GB_phoneNumber = GB_phoneNumber.replace('(', '').replace(')', '').replace('-', '').strip()
            GB_phoneNumber = '+1{}'.format(GB_phoneNumber)
            GB_phoneNumber = GB_phoneNumber.replace(' ', '')
            print ("Numero de telefono :" + GB_phoneNumber)
            code = None

            while(code == None):
                Retries_loop_sms += 1
                if (Retries_loop_sms == RETRY_AT) :
                    print ("! - Solicitando el mensaje de texto de nuevo")
                    time.sleep(3)
                    if (self.Get_outerHTML_and_check_partial_text_via_xpath('Text',self.W_Verify_an_business_Target_TextAgain_xpath)  == True ) :
                            self.Click_by_xpath(self.W_Verify_an_business_Target_TextAgain_xpath)
                            print ("! - Sleeping 15 seconds - While Receving sms")
                            time.sleep(15)
                    else :
                        print ("! - No pudimos reenviar el mensaje")
                elif (Retries_loop_sms == MAX_RETRIES) :
                    print ("!- Hemos alcazando el maximo de Numero de reintentos. ")
                    GBusiness_handle.Verify_an_business_Skip = True
                    TWatch.ListThreads['VerifyBusiness'].cancel()
                    return

                time.sleep(1)
                print ("! - Doing response to Matrix")
                response = credential.get_validation_code(
                    phone_number=GB_phoneNumber
                )
                status_code = response.status_code
                response = response.json()

                if status_code == 200 and 'msg' in response:
                    print('! - Response', response)
                    code = response['msg'] if len(response['msg']) == 6 else None
                    print ("El code es: {}".format(code))

            if (self.FillField_by_xpath(str(code), self.W_Verify_an_business_Target_EnterVerifyCode_xpath, True) == True):
                print ('! - Ha sido rellenado el campo de verificacion')
                self.W_Verify_an_business_step = 23

        if (self.W_Verify_an_business_step == 23) :
            if (self.Click_by_xpath(self.W_Verify_an_business_Target_Button_Verify_Now) == True) :
                self.W_Verify_an_business_step = 24

        if (self.W_Verify_an_business_step == 24):
            time.sleep(3)
            print ("Pantalla de ya se ha verificado el business")
            credential.report_validation()
            GBusiness_handle.BusinessValidation = 1
            TWatch.ListThreads['VerifyBusiness'].cancel()
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

    def handle (self, *args, **options):
        business_service = BusinessService()
        business_list = business_service.get_list()
        self.credential_list = business_list

        counter = 0

        for credential in self.credential_list:
            if all([
                credential.date_renamed,
                credential.date_validation
            ]):
                continue

            counter = counter + 1
            OGAuth.SucessLogin = 0 # SuccessLogin Default: 0

            GBusiness_handle.BusinessValidation = 0 # BusinessValidation Default : 0
            GBusiness_handle.W_Verify_an_business_step = 0 # W_Verify_an_business_step
            GBusiness_handle.Verify_an_business_Skip = False # Skip Reset.
            GBusiness_handle.W_Verify_an_business_Match = False # Business wan't found yet
            GBusiness_handle.W_Update_an_business_step = 0
            GBusiness_handle.W_Update_an_business_Match = False
            GBusiness_handle.UpdateBusinessValidation = False

            print(credential.name, credential.email, credential.password, credential.recovery_email)

            if (self.verification_of_credential(credential) == False) :
                logger(instance_itself=self.NameClass_itSelf(), data=Skiping_to_next_credential)
                print (Skiping_to_next_credential)
                continue
            # THERE VERIFICATIONfrom services import BusinessService
            # CONSIDERATE EMAIL IS EMAIL. WITH @ ALSO
            # PASSWORD (NOTHING SPECIAL)
            if (self.is_Driver_GAuth_loaded() == True) :
                OGAuth.RunDriver()
                GBusiness_handle.setDriver(OGAuth.driver)
            try:
                print ("# Email: " + credential.email)
                Controller_Login = MWatcher(0.5, 'controller_login' , 'OGAuth', 'W_do_login', TWache_GAuth_login, credential, True)
            except CredentialInvalid:
                continue

            if (OGAuth.SucessLogin == 1) :
                print ("Setting up driver for Google Bussiness")
                print ("Sleeping 1s")
                time.sleep(1)

            if not credential.date_renamed: # Can we rename this business? YES
                Data=dict()
                Data['credential'] = credential
                Data['Parameters'] = dict(
                    Name=True,
                    Category=False
                )
                #Calling MWatcher to start process of Update
                BusinessUpdate = MWatcher(0.5, 'UpdateBusiness', 'GBusiness_handle', 'W_Update_an_business' , 'TWatch_UpdateanBusiness', credential, True)

            if not credential.date_validation:
                #Calling MWatcher to start process of Verification
                VerifyBusiness = MWatcher(0.5, 'VerifyBusiness', 'GBusiness_handle', 'W_Verify_an_business' , 'TWatch_VerifyBusiness', credential, True)

            print ("!- Hemos concluido con la credenecial de business: " + credential.name )
            GBusiness_handle.driver.quit()

        # self.Finished_app()



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
