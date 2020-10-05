#!/usr/bin/python

import requests

def main():
	targetUrl = "https://www.walmart.com/ip/ICE-MOUNTAIN-Brand-100-Natural-Spring-Water-16-9-ounce-bottles-Pack-of-24/21943694"
	response = requests.get(targetUrl)
	print(response.status_code)
	print(response.text)

main()
