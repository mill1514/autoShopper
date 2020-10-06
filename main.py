#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

browser = webdriver.Chrome()
action = ActionChains(browser)

def main():
	# Head on over to Walmart
	browser.get("https://www.walmart.com/ip/ICE-MOUNTAIN-Brand-100-Natural-Spring-Water-16-9-ounce-bottles-Pack-of-24/21943694")
	time.sleep(1)

	# Find the "add to cart" button
	targetClass = "prod-product-cta-add-to-cart"
	button = browser.find_element_by_class_name(targetClass)
	action.click(on_element=button)
	action.perform()
	time.sleep(5)

main()