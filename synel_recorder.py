#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Usage:
    synel_recorder.py enter --user=employeeID --password=PASSWORD --company=companyID
    synel_recorder.py exit --user=employeeID --password=PASSWORD --company=companyID 
    
    
Options:
    --password=PASSWORD User defined password
    --user=USER Employee ID, usually a number
    --company=COMPANY Company ID, usually a number
'''

try:
    from selenium.webdriver.firefox.webdriver import WebDriver
    from selenium.webdriver.common.action_chains import ActionChains
except:
    print "Try 'pip install -U selenium'. Do not forget to install firefox"    
import time
import logging

try:
    from docopt import docopt
except:
    print "Try 'pip install -U docopt'"    

success=True

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

def push_record(wd, username, password, company, is_enter):
    wd.get("https://harmony.synel.co.il/eharmonynew")
    wd.implicitly_wait(60)
    wd.find_element_by_name("compInput").click()
    wd.find_element_by_name("compInput").clear()
    wd.find_element_by_name("compInput").send_keys(company)
    wd.find_element_by_name("loginBtn").click()
    wd.implicitly_wait(60)
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").click()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").clear()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']//button[.='LOGIN']").click()
    wd.implicitly_wait(60)

    buttons = {True: "//div[@class='controls']/input[1]", False: "//div[@class='controls']/input[2]"}    
    wd.find_element_by_xpath(buttons[is_enter]).click()
    wd.implicitly_wait(5)
    wd.find_element_by_id("btnOk").click()
    wd.implicitly_wait(5)
    #wd.find_element_by_xpath("//form[@id='loginHarmonyDB']//button[.='LOGIN']").click()
    wd.find_element_by_link_text("(Logout)").click()
    wd.implicitly_wait(5)
        
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Synel recorder')
    logging.basicConfig()    
    logger = logging.getLogger('synel')
    logger.setLevel(logging.INFO)    

    is_enter = arguments["enter"]
    company = arguments["--company"]
    password = arguments["--password"]
    username = arguments["--user"]
    
    logger.info("Record '{0}' for user '{1}', company '{2}'".format(
        {True:"ENTER", False:"EXIT"}[is_enter], 
        username, company))

    wd = WebDriver()
    wd.implicitly_wait(60)
    
    try:
        push_record(wd, username, password, company, is_enter)
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")
