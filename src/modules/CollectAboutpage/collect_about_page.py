# CSV
import csv

from bs4 import BeautifulSoup

class CollectAboutPage():

    def __init__(self, browser, about_page_errors=None, about_page_variables=None):
        self.browser = browser
        
        if about_page_errors is None:
            self.about_page_errors = []
        else:
            self.about_page_errors = about_page_errors
        
        if about_page_variables is None:
            self.about_page_variables = []
        else:
            self.about_page_variables = about_page_variables

    def collectAbout(self):
        try:
            about_src = self.browser.page_source
            about_soup = BeautifulSoup(about_src)

            try:
                company_website_parent = about_soup.find(
                    'dl', {'class': 'overflow-hidden'})                
                company_website = company_website_parent.find(
                    'span', {'class': 'link-without-visited-state', 'dir': 'ltr'}).get_text()

            except:
                self.errors.append('company_website')
                company_website = ""
                print('Error collecting website')

            # Founded Date
            try:
                dt_tags = about_soup.find_all('dt')
                dl_tag = about_soup.find('dl', {'class': 'overflow-hidden'})
                dd_tags = dl_tag.find_all('dd')

                i = 0
                founded_index = None
                for dt_tag in dt_tags:
                    if dt_tag.text.strip() == "Founded":
                        founded_index = i
                    else:
                        i += 1
                        if i == len(dt_tags):
                            return
                founded_date = dd_tags[founded_index+1].get_text().strip()
            except:
                self.errors.append('founded_date')
                founded_date = ""
                print('Error collecting website')
        except:
            self.errors.append('company_website')
            self.errors.append('founded date')
            print('Error collecting website and founded date')
            company_website = ""
            founded_date = ""
            
        self.about_page_variables.append(company_website)
        self.about_page_variables.append(founded_date)
        results = self.about_page_variables

        return results