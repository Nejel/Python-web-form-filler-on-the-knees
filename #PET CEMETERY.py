'''
PET CEMETERY



rl = "https://app.customergauge.com/index.php?m=AdminUsersManager&a=create"
data = ('TestInput')
r = requests.post(url, data)
r.text






with requests.Session() as c:
    url = "https://app.customergauge.com/index.php?m=AdminUsersManager&a=create"
    username_of_the_user_being_edited = 'testinput777'
    c.get(url)
    login_data = dict(username_of_the_user_being_edited = username_of_the_user_being_edited)
    c.post(url, data=login_data)





Keys:
https://seleniumhq.github.io/selenium/docs/api/java/org/openqa/selenium/Keys.html

_______________________________________________________________________________________

#Some Geckodriver bullshit to execute Firefox properly

#REPLACE FOR CHROMEDRIVER MAY BE?
#st = os.stat('C:\\Users\\User\\geckodriver.exe')
#os.chmod('C:\\Users\\User\\geckodriver.exe', st.st_mode | stat.S_IEXEC)
#print(st)

Stand Output for that part:
os.stat_result(st_mode=33279, st_ino=7318349394819137, st_dev=811390258, st_nlink=1, st_uid=0, st_gid=0, st_size=6048686, st_atime=1505548698, st_mtime=1509048965, st_ctime=1505548698)


_______________________________________________________________________________________
#REPLACE FOR CHROMEDRIVER MAY BE?

#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

#binary = FirefoxBinary('C:\\Users\\User\\AppData\\Local\\Mozilla Firefox\\firefox.exe')
#driver = webdriver.Firefox(firefox_binary=binary)
#WRONG VERSION #binary = FirefoxBinary('C:\\Users\\User\\Anaconda3\\Lib\\site-packages\\selenium\\webdriver\\firefox')


_______________________________________________________________________________________

help (selenium)

Help on package selenium:

NAME
    selenium

DESCRIPTION
    # Licensed to the Software Freedom Conservancy (SFC) under one
    # or more contributor license agreements.  See the NOTICE file
    # distributed with this work for additional information
    # regarding copyright ownership.  The SFC licenses this file
    # to you under the Apache License, Version 2.0 (the
    # "License"); you may not use this file except in compliance
    # with the License.  You may obtain a copy of the License at
    #
    #   http://www.apache.org/licenses/LICENSE-2.0
    #
    # Unless required by applicable law or agreed to in writing,
    # software distributed under the License is distributed on an
    # "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
    # KIND, either express or implied.  See the License for the
    # specific language governing permissions and limitations
    # under the License.

PACKAGE CONTENTS
    common (package)
    webdriver (package)

VERSION
    3.6.0

FILE
    c:\users\user\anaconda3\lib\site-packages\selenium\__init__.py




________________________________________________________________________________________

#WRONG VARIANTS OF BUTTON SELECTION
#Realization 1:

#user = browser.find_element_by_id("role")
#user.select_by_value("User")

#hidden_submenu = browser.find_element_by_css_selector(".nav #submenu1")


#Realization 2:

el = webdriver.find_element_by_id('role')
for option in el.find_elements_by_tag_name('User'):
    if option.text == 'User':
        option.click() # select() in earlier versions of webdriver
        break





#Realization 2:

el = webdriver.find_element_by_id('role')
for option in el.find_elements_by_tag_name('User'):
    if option.text == 'User':
        option.click() # select() in earlier versions of webdriver
        break



#Realization 4
#b.find_element_by_xpath(//*[@id="role"]).click();



#Realization 5
TestVariable = webdriver.findElement(By.CssSelector("#role")).Select()


#Realization 6

selectdropdown = select(driver.findElement(By.id("role")));
dropdown.selectByVisibleText("User");

#Realization 7
elem = browser.find_element_by_css_selector('#role > option:nth-child(3)')

#Realization 8

select = driver.find_element_by_css_selector("#role")
option = select.findElements(By.tagName("Male"));
user.select_by_visible_text("User")

b = webdriver.Firefox()

# navigate to the page
select = Select(b.find_element_by_id("role"))
#print select.options
#print [o.text for o in select.options] # these are string-s
select.select_by_visible_text("User")

'''
