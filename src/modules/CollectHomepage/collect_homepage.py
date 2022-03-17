# CSV
import csv
from bs4 import BeautifulSoup

class CollectHomepage():
    
    def __init__(self, browser, homepage_errors=None, homepage_variables=None):
        self.browser = browser
        if homepage_errors is None:
            self.homepage_errors = []
        else:
            self.homepage_errors = homepage_errors
        
        if homepage_variables is None:
            self.homepage_variables = []
        else:
            self.homepage_variables = homepage_variables
    
    def collect_home(self):        

        try:
            self.browser.implicitly_wait(10)

            src = self.browser.page_source
            soup = BeautifulSoup(src)

            # Name, Tag, and Sector
            name_div = soup.find('div', {'class': 'block mt2'})
            try:
                name = name_div.find('span').get_text().strip()
            except:
                self.homepage_errors.append('name')
                name = ""
            try:
                tag = name_div.find('p').get_text().strip()
            except:
                self.homepage_errors.append('tag')
                tag = ""
            try:
                sector = name_div.div.div.div.get_text().strip()
            except:
                self.homepage_errors.append('sector')
                sector = ""

            ## Location and Followers
            try:
                ## Logic - if followers is first child div, then location is null. If inline-block has two children then location if given, if not, only followers
                loc_followers_wrapper = soup.find(
                    'div', {'class': 'inline-block'})
                try:
                    test = loc_followers_wrapper.find_all(
                        'div', {'class': 'org-top-card-summary-info-list__info-item'})
                    # Second div tag if both loc and foll are present
                    followers_cell = test[1].get_text().strip()
                    space = followers_cell.find(" ")
                    followers = followers_cell[:space]
                    location = test[0].get_text().strip()
                except:
                    followers_cell = loc_followers_wrapper.find(
                        'div', {'class': 'org-top-card-summary-info-list__info-item'}).get_text().strip()
                    # Remove text
                    space = followers_cell.find(' ')
                    followers = followers_cell[:space]
                    self.homepage_errors.append('location')
                    location = ""
            except:
                self.homepage_errors.append('location')
                self.homepage_errors.append('followers')
                location = ""
                followers = ""

            # Employee count
            try:
                employee_count_text = soup.find('span', {
                    'class': 'link-without-visited-state t-bold t-black--light'}).get_text().strip()
                first_num = employee_count_text.find('ll') + 3
                last_num = employee_count_text.find(" em")
                employee_count = employee_count_text[first_num:last_num]
            except:
                self.homepage_errors.append('employee_count')
                employee_count = ""

        
        # If unable to navigate to page and generate soup - all variables should be left blank
        except:
            self.homepage_errors.append('name')
            self.homepage_errors.append('tag')
            self.homepage_errors.append('sector')
            self.homepage_errors.append('location')
            self.homepage_errors.append('followers')
            self.homepage_errors.append('employee_count')
        
        self.homepage_variables.extend([
            name, 
            tag, 
            sector, 
            location,
            followers,
            employee_count
        ])

        return self.homepage_variables
  


