#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Usage:
    synel_recorder enter --user=employeeID --password=PASSWORD --company=companyID>
    synel_recorder exit --user=employeeID --password=PASSWORD --company=companyID> 
    
    
Options:
    --password=PASSWORD User defined password
    --user=USER Employee ID, usually a number
    --company=COMPANY Company ID, usually a number
'''

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import logging
from docopt import docopt


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

def push_record(wd, username, password, company):
    wd.get("https://harmony.synel.co.il/eharmonynew")
    wd.implicitly_wait(3)
    wd.find_element_by_name("compInput").click()
    wd.find_element_by_name("compInput").clear()
    wd.find_element_by_name("compInput").send_keys(company)
    wd.find_element_by_name("loginBtn").click()
    wd.implicitly_wait(3)
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").click()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").clear()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").send_keys(username)
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys(password)
    wd.implicitly_wait(3)
    
    wd.find_element_by_xpath("//div[@class='controls']/input[1]").click()
    ActionChains(wd).double_click(wd.find_element_by_id("overlayReportingControlDiv")).perform()
    wd.find_element_by_id("btnOk").click()
    wd.implicitly_wait(3)
    wd.find_element_by_xpath("//div[@class='controls']/input[2]").click()
    ActionChains(wd).double_click(wd.find_element_by_id("overlayReportingControlDiv")).perform()
    wd.find_element_by_id("btnOk").click()
        
if __name__ == '__main__':
    arguments = docopt(__doc__, version='Synel recorder')
    logging.basicConfig()    
    logger = logging.getLogger('synel')
    logger.setLevel(logging.INFO)    

    is_enter = False
    if ("enter" in arguments):
        is_enter = True;
    company = arguments["--company"]
    password = arguments["--password"]
    user = arguments["--user"]
    
    logger.info("Record '{0}' for user '{1}, company '{2}'".format({True:"ENTER", False:"EXIT"}[is_enter], user, company))

    wd = WebDriver()
    wd.implicitly_wait(3)
    
    try:
        push_record(wd, username, password, company)
    finally:
        wd.quit()
        if not success:
            raise Exception("Test failed.")
