
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

def clickButtonOfClass(targetButtonClass, browser):
	targetButton = browser.find_element_by_class_name(targetButtonClass)

	targetButtonAction = ActionChains(browser)
	targetButtonAction.click(on_element=targetButton)
	targetButtonAction.perform()