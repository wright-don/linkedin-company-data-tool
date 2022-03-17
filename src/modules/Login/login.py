from selenium.webdriver.common.by import By

class Login():

    def __init__(self, browser, email, key,):
        self.browser = browser
        self.By = By
        self.email = email
        self.key = key

    # Method 1 Selenium Driver Login
    def login(self): 
        self.browser.get('https://www.linkedin.com/uas/login')
        elementID = self.browser.find_element(By.ID, 'username')
        elementID.send_keys(self.email)
        elementID = self.browser.find_element(By.ID, 'password')
        elementID.send_keys(self.key)
        elementID.submit()            

    