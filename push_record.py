# -*- coding: utf-8 -*-
'''
Usage:
    synel enter --user=<employee ID> --password=<password>
    synel exit --user=<employee ID> --password=<password>
'''
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import docopt

success = True
wd = WebDriver()
wd.implicitly_wait(3)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://harmony.synel.co.il/eharmonynew")
    wd.implicitly_wait(3)
    wd.find_element_by_name("compInput").click()
    wd.find_element_by_name("compInput").clear()
    wd.find_element_by_name("compInput").send_keys("53782071")
    wd.find_element_by_name("loginBtn").click()
    wd.implicitly_wait(3)
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").click()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").clear()
    wd.find_element_by_xpath("//form[@id='loginHarmonyDB']/div[6]/input").send_keys("20")
    wd.find_element_by_name("password").click()
    wd.find_element_by_name("password").clear()
    wd.find_element_by_name("password").send_keys("arkadym")
    wd.implicitly_wait(3)
    
    wd.find_element_by_xpath("//div[@class='controls']/input[1]").click()
    ActionChains(wd).double_click(wd.find_element_by_id("overlayReportingControlDiv")).perform()
    wd.find_element_by_id("btnOk").click()
    wd.implicitly_wait(3)
    wd.find_element_by_xpath("//div[@class='controls']/input[2]").click()
    ActionChains(wd).double_click(wd.find_element_by_id("overlayReportingControlDiv")).perform()
    wd.find_element_by_id("btnOk").click()
    
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
