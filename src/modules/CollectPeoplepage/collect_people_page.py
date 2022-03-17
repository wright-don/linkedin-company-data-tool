from bs4 import BeautifulSoup

class CollectPeoplePage():

    def __init__(self, browser, people_page_errors=None, people_page_variables=None):
        self.browser = browser
        
        if people_page_errors is None:
            self.people_page_errors = []
        else:
            self.people_page_errors = people_page_errors
        
        if people_page_variables is None:
            self.people_page_variables = []
        else:
            self.peoplet_page_variables = people_page_variables

    def collectPeople(self):
        try:
            people_src = self.browser.page_source
            people_soup = BeautifulSoup(people_src)

            # Employee Location
            try:
                emp_container = people_soup.find(
                    'div', {'class': 'artdeco-card p4 m2 org-people-bar-graph-module__geo-region'})
                emp_tags = emp_container.find_all('button')
                employee_locations = []
                for emp_tag in emp_tags:
                    employee_locations.append(emp_tag.get_text().strip())
            except:
                self.people_page_errors.append('employee_locations')
                employee_locations = ""
        
        except:
            self.people_page_errors.append('employee_locations')
            employee_locations = ""

        self.people_page_variables.append(employee_locations)              
        
        results = [self.people_page_errors, self.people_page_variables]
        return results        