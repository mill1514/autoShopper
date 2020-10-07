#!/usr/bin/python

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

browser = webdriver.Chrome()

def main():
	# Head on over to Walmart
	browser.get("https://www.walmart.com/ip/ICE-MOUNTAIN-Brand-100-Natural-Spring-Water-16-9-ounce-bottles-Pack-of-24/21943694")

	# Click the "add to cart" button
	addToCartButtonClass = "prod-product-cta-add-to-cart"
	addToCartButton = browser.find_element_by_class_name(addToCartButtonClass)

	addToCartAction = ActionChains(browser)
	addToCartAction.click(on_element=addToCartButton)
	addToCartAction.perform()

	time.sleep(5)

	checkoutButtonClass = "checkoutBtn"
	checkoutButton = browser.find_element_by_class_name(checkoutButtonClass)

	checkoutAction = ActionChains(browser)
	checkoutAction.click(on_element=checkoutButton)
	checkoutAction.perform()

main()