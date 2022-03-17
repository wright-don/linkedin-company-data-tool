# Linkedin Data Tool - Company Stats
![example results](https://github.com/wright-don/linkedin-company-data-tool/blob/main/images/example_results.png?raw=true)

## Overview
- Overview: This Python Script allows you to take a list of companies and generate data based upon that company's linkedin page. These variables include company taglines (short description), sector, hq location, number of followers, employee count, employee locations, company website, and founded date. 

## Instructions 
- Create Driver Folder and add chromedriver ( check chrome browser version on your device )
- Add linkedin credentials to .env file
- Import necessary packages
    - Virtual Env
        - pip install virtualenv 
        - virtualenv venv
        - source venv/bin/activate
    - Python-decouple ( for reading env ) *Use config.ini if error thrown.
        - pip install python-decouple
    - Selenium
        - pip install selenium 
    - Beautiful Soup
        - pip install beautifulsoup4

# Bug Fixes 
- Currently, when running the program for long lists, errors may occur as a result of incomplete requests. Additional scraping practicing can be added to improve the quality of this script - this includes random mouse movements, random sleeps, header changes to request, etc. 



