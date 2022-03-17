# Both the 'Affiliated Companies Modal' and 'Similar Companies Modal' are given the same class name. We will run the same XPATH but change the index to alternate between the two.
dynamic_button = browser.find_elements(By.XPATH,
    "//button[@class='artdeco-button artdeco-button--muted artdeco-button--3 artdeco-button--full artdeco-button--tertiary ember-view']"
)

# Gather 'Affiliated' / 'Similar' Companies
try:
    dynamic_component = dynamic_button[0].text
    print(dynamic_component)
    if dynamic_component == 'See all similar pages':
        similar_companies_button = dynamic_button[0]
        similar_companies_button.send_keys(Keys.ENTER)
        browser.implicitly_wait(30)

        similar_companies_id = browser.find_elements(By.XPATH,
            "//div[@class='artdeco-modal__content ember-view']//child::div[@class='display-flex']"
        )
        # identify how many results are displayed - after finding run loop instead of try / except
        # ^^ above not solved so using try | except as work around
        try:                        
            print(similar_companies_id[1].text)
            print(similar_companies_id[2].text)
            print(similar_companies_id[3].text)
            print(similar_companies_id[4].text)
            print(similar_companies_id[5].text)
            print(similar_companies_id[6].text)
            print(similar_companies_id[7].text)
            print(similar_companies_id[8].text)
            print(similar_companies_id[9].text)
        except:
            print('End of list. Next task ✅')

    # For this else to run, the first displayed component must have been affilated page. For this instance we will store the values differently
    else:    
        affiliated_companies_button = dynamic_button[0]
        affiliated_companies_button.send_keys(Keys.ENTER)
        browser.implicitly_wait(30)
        # the modal with addtional companies should now be open. There are limited unique identifier
        affiliated_companies_id = browser.find_elements(By.XPATH,
            "//div[@class='artdeco-modal__content ember-view']//child::div[@class='display-flex']"
        )

    try:
        print(affiliated_companies_id[1].text)
        print(affiliated_companies_id[2].text)
        print(affiliated_companies_id[3].text)
        print(affiliated_companies_id[4].text)
        print(affiliated_companies_id[5].text)
        print(affiliated_companies_id[6].text)
        print(affiliated_companies_id[7].text)
        print(affiliated_companies_id[8].text)
        print(affiliated_companies_id[9].text)
    except:
        print('End of list. Next task ✅')

    # close the model before beginnning next step
    close_icon = browser.find_element(By.CSS_SELECTOR,
        'svg[class="mercado-match"]'
    )
    close_icon.click()

except:
    print('People also viewed companies not present, skipping...')

# Gather 'Affiliated' / 'Similar' Companies
try:
    dynamic_component = dynamic_button[1].text
    print(dynamic_component)
    if dynamic_component == 'See all similar pages':
        similar_companies_button = dynamic_button[1]
        similar_companies_button.send_keys(Keys.ENTER)
        browser.implicitly_wait(30)

        similar_companies_id = browser.find_elements(By.XPATH,
            "//div[@class='artdeco-modal__content ember-view']//child::div[@class='display-flex']"
        )
        # identify how many results are displayed - after finding run loop instead of try / except
        # ^^ above not solved so using try | except as work around
        try:                        
            print(similar_companies_id[1].text)
            print(similar_companies_id[2].text)
            print(similar_companies_id[3].text)
            print(similar_companies_id[4].text)
            print(similar_companies_id[5].text)
            print(similar_companies_id[6].text)
            print(similar_companies_id[7].text)
            print(similar_companies_id[8].text)
            print(similar_companies_id[9].text)
        except:
            print('End of list. Next task ✅')

    # For this else to run, the first displayed component must have been affilated page. For this instance we will store the values differently
    else:    
        affiliated_companies_button = dynamic_button[0]
        affiliated_companies_button.send_keys(Keys.ENTER)
        browser.implicitly_wait(30)
        # the modal with addtional companies should now be open. There are limited unique identifier
        affiliated_companies_id = browser.find_elements(By.XPATH,
            "//div[@class='artdeco-modal__content ember-view']//child::div[@class='display-flex']"
        )

    try:
        print(affiliated_companies_id[1].text)
        print(affiliated_companies_id[2].text)
        print(affiliated_companies_id[3].text)
        print(affiliated_companies_id[4].text)
        print(affiliated_companies_id[5].text)
        print(affiliated_companies_id[6].text)
        print(affiliated_companies_id[7].text)
        print(affiliated_companies_id[8].text)
        print(affiliated_companies_id[9].text)
    except:
        print('End of list. Next task ✅')

    # close the model before beginnning next step
    close_icon = browser.find_element(By.CSS_SELECTOR,
        'svg[class="mercado-match"]'
    )
    close_icon.click()          

except:
    print('People also viewed companies not present, skipping...')
