#!/usr/bin/python

from selenium import webdriver

def main():
	browser = webdriver.Chrome()
	browser.get("https://www.yahoo.com")

main()
