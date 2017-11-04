'''
PREPARATIONS:

1. Chrome driver (https://sites.google.com/a/chromium.org/chromedriver/downloads) should be
downloaded to current working directory ('c:\\users\\user' in my case) and started all the time.

WARNING: For Windows the latest version of Chromedriver does now work. Use 2.27 instead (https://chromedriver.storage.googleapis.com/index.html?path=2.27/)

2. File 'Testlist.xlsx' should be created in your current working directory.

'''


!pip install openpyxl
!pip install bs4
!pip install -U selenium

#Selenium 3.6.0. Use 'help (selenium)' to check

#Imports

import openpyxl
import os
import selenium
import stat
import bs4
import time
import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

os.chdir('c:\\users\\user')

##os.getcwd()
##Should returns only 'c:\\users\\user'

#Setting UP start line in xlsx file
i = 52

## Browser first force start
browser = webdriver.Chrome()
#Chrome with 'data:,' in adress line should start after that
browser.get('https://app.customergauge.com/index.php?m=AdminUsersManager&a=create')


##########################Login Break###############################


#r range means how many users should be created (by rows)
for r in range (4):

    #Checking that page is active
    browser.get('https://app.customergauge.com/index.php?m=AdminUsersManager&a=create')

    #Excel work
    workbook = openpyxl.load_workbook('Testlist.xlsx')
    sheet = workbook.get_sheet_by_name('Sheet1')
    Username1 = str(sheet['A'+str(i)].value)
    FirstName = str(sheet['B'+str(i)].value)
    Lastname = str(sheet['C'+str(i)].value)

    Email = str(sheet['D'+str(i)].value)
    Password = str(sheet['E'+str(i)].value)
    Division1XPATH = str(sheet['I'+str(i)].value)
    Division2XPATH = str(sheet['J'+str(i)].value)
    Division3XPATH = str(sheet['K'+str(i)].value)

    time.sleep(1)
    elem = browser.find_element_by_css_selector('#username_of_the_user_being_edited')
    elem.send_keys(Keys.PAGE_UP)


    # Selection of simple page elements

    Username1insert = browser.find_element_by_css_selector('#username_of_the_user_being_edited')
    FirstNameinsert = browser.find_element_by_css_selector('#first_name')
    Lastnameinsert = browser.find_element_by_css_selector('#last_name')
    Emailinsert = browser.find_element_by_css_selector('#email')
    Passwordinsert = browser.find_element_by_css_selector('#password')
    REPasswordinsert = browser.find_element_by_css_selector('#password_check')

    Username1insert.send_keys(Username1)
    FirstNameinsert.send_keys(FirstName)
    Lastnameinsert.send_keys(Lastname)
    Emailinsert.send_keys(Email)
    Passwordinsert.send_keys(Password)
    REPasswordinsert.send_keys(Password)


    #Selection on User in Role field
    selectrole = browser.find_element(By.XPATH, '/html/body/div[4]/section/section/div/form/table/tbody/tr[6]/td[2]/select/option[2]').click()

    #Pressing Tab
    selectroleTAB = browser.find_element(By.XPATH, '//*[@id="role"]')
    selectroleTAB.send_keys(Keys.TAB)
    time.sleep(0.4)

    #Input Radiobuttons Division
    #Level0 -- is a 'Global' (there is no such level in code here, that's default)
    #Level1 -- A, CorpComm, CEO office, etc.

    selectdivisionlevel1 = browser.find_element(By.XPATH, '/html/body/div[4]/section/section/div/form/table/tbody/tr[8]/td[1]/ul/li[1]/input').click()
    time.sleep(0.2)
    selectdivisionlevel2 = browser.find_element(By.XPATH, '/html/body/div[4]/section/section/div/form/table/tbody/tr[8]/td[1]/ul/li[1]/ul/li/input').click()
    time.sleep(0.2)
    selectdivisionlevel2 = browser.find_element(By.XPATH, '/html/body/div[4]/section/section/div/form/table/tbody/tr[8]/td[1]/ul/li[1]/ul/li/ul/li/input').click()


    #Scroll down

    elem = browser.find_element_by_css_selector('#username_of_the_user_being_edited')
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    #Input Radiobuttons STATUS
    SelectStatus2 = browser.find_element_by_css_selector('.summary > tbody:nth-child(1) > tr:nth-child(10) > td:nth-child(1) > input:nth-child(2)')
    SelectStatus2.click()

    #Pressing SAVE button

    ##pressingsave = browser.find_element(By.XPATH, '//*[@id="btn_save"]')
    #time.sleep(1)
    #pressingsave = browser.find_element(By.XPATH, '//*[@id="btn_save"]').click()

    #Another option:
    #browser.submit_selected(btnName="Submit order")

    PressingSaveCSS = browser.find_element_by_css_selector('#btn_save')
    PressingSaveCSS.click()

    #show me the result
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

    #Go to next persone
    i = i + 1


print(i)
