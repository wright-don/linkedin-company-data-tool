class GoToPeoplePage():

    def __init__(self, browser, company, company_li_url):
        self.browser = browser
        self.company = company
        self.company_li_url = company_li_url

    def go_to_people_page(self):
        # Navigate to about page
        self.browser.get(f'{self.company_li_url}people/')
        self.browser.implicitly_wait(5)