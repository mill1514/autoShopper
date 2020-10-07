#!/usr/bin/python

import autoShopperUtil as asu

import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains 

browser = webdriver.Chrome()

def main():
	# Head on over to Walmart
	browser.get("https://www.walmart.com/ip/ICE-MOUNTAIN-Brand-100-Natural-Spring-Water-16-9-ounce-bottles-Pack-of-24/21943694")

	# Click the "add to cart" button
	asu.clickButtonOfClass("prod-product-cta-add-to-cart", browser)
	time.sleep(5)

	# Click the "checkout" button
	asu.clickButtonOfClass("checkoutBtn", browser)

main()