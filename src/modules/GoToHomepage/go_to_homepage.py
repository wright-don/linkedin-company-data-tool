import time
from selenium.webdriver.common.by import By

class GoToHomepage():

    # Initialization
    def __init__(self, browser, company):
        self.browser = browser
        self.company = company

    def go_to_homepage(self):

        #  Every company search on linkedin will contain this url syntax or prefix
        linkedin_search_baseurl = "https://www.linkedin.com/search/results/companies/?keywords="

        # linkedin url's have a dynamic syntax, therefore in order to search for companies whose name contains more than one word, we will need to concatentate the individual words with linkedin's uniuqe syntax ('%20' is placed between each word)

        # split the company name so each word is given an index
        company_word_list = self.company.split()

        # we need to create a variable that will hold the dynamic suffix to our base linkedin company search url.
        url_ending = ""

        # if the company name is just one word, then the url_ending will simply be the name of the company
        if len(company_word_list) == 1:
            url_ending += company_word_list[0]

        # if the company name is longer than 1 word, the search url syntax will change - For this, we can run a loop over each word in the company name, and if the current word is not first, place '$20' before the word at that current word's index.
        else:
            url_ending = company_word_list[0]
            i = 1
            while i < len(company_word_list):
                # each time the loop is ran, a value with be added to url_ending variable we've created
                url_ending += "%20" + company_word_list[i]
                i += 1

        # Company Insights URL
        company_url = linkedin_search_baseurl + url_ending
        # Now that we've identified what the url ending should be for the unique company we're researching, we can now navigate to the corresponding LI search query results

        self.browser.get(company_url)
        self.browser.implicitly_wait(2)
        time.sleep(1)



