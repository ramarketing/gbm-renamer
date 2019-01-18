
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
        
