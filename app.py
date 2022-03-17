# Import Dependencies
# CSV
import csv
# Time
import time
#SELENIUM
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# BEAUTIFUL SOUP
from bs4 import BeautifulSoup
# CONNECT ENVIRONMENT VARIABLES
from decouple import config

# Local Modules
from src.modules.CollectPeoplepage import collect_people_page
from src.modules.GoToPeoplepage import go_to_people_page
from src.modules.CollectAboutpage import collect_about_page
from src.modules.GoToAboutpage import go_to_about_page
from src.modules.CollectHomepage import collect_homepage
from src.modules.GoToHomepage import go_to_homepage
from src.modules.Login import login

EMAIL = config('EMAIL')
KEY = config('KEY')


# IMPORT MODULES
# Login

# COLLECT HOMEPAGE
CollectHomepage = collect_homepage.CollectHomepage

# COLLECT ABOUTPAGE
CollectAbout = collect_about_page.CollectAboutPage

# COLLECT PEOPLEPAGE
CollectPeople = collect_about_page.CollectAboutPage



# GET COMPANIES
companies = []
file_path = "companies.txt"
with open(file_path, 'r') as companies_list:
    for i in companies_list.readlines():
        name= i.replace('\n', "")
        companies.append(name)



class App():

    # OPEN BROWSER
    driver = Service('driver/chromedriver')
    browser = webdriver.Chrome(service=driver)

    # LOGIN
    login.Login(browser, EMAIL, KEY).login()

    header = ["Name", "Tag", "Sector", "Location", "Followers",
              "Employee Count", "Employee Locations", "Company Website", "Founded Date"]

    # Save all variables to csv
    with open('results.csv', 'a') as f:
        object = csv.writer(f)
        object.writerow(header)
        f.close()

    # SEARCH_COMPANIES
    for company in companies:

        # Final Results
        data = []
        
        try: 
            go_to_homepage.GoToHomepage(browser, company).go_to_homepage()

            # Company Linkedin Page URL
            browser.implicitly_wait(2)
            # time.sleep(2)
            company_li_url = browser.find_element(
                By.XPATH, '//div[@class="entity-result__item"]//a').get_attribute('href')
            browser.get(company_li_url)
            time.sleep(1)
            browser.implicitly_wait(2)

            # Get Hompage Data
            homepage_variables = collect_homepage.CollectHomepage(
                browser).collect_home()

            for homepage_variable in homepage_variables:
                data.append(homepage_variable)

            # Go To People Page
            go_to_people_page.GoToPeoplePage(
                browser, company, company_li_url).go_to_people_page()
            time.sleep(2)

            # Collect People Page
            people_results = collect_people_page.CollectPeoplePage(
                browser).collectPeople()

            people_errors = people_results[0]
            people_variables = people_results[1]
            data.append(people_variables)

            # Go To About Page
            go_to_about_page.GoToAboutPage(
                browser, company, company_li_url).go_to_about_page()
            time.sleep(2)

            # Collect About Page
            about_results = collect_about_page.CollectAboutPage(
                browser).collectAbout()
            website = about_results[0].strip()
            founded_date = about_results[1]
            data.append(website)
            data.append(founded_date)
    
        # Handle cases where search query yeilds zero results
        except:
            data.append(company)

        # Save all variables to csv
        with open('results.csv', 'a') as f:
            object = csv.writer(f)
            object.writerow(data)
            f.close()

        browser.close


App()
