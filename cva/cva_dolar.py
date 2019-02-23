#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from selenium import webdriver
import base64
from pyvirtualdisplay import Display
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import fileinput
import re

import config

timeout=30

def login(url, driver):
	driver.get(url)
	keyData = base64.b64decode(config.key_cva).split(':')
	
	WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.ID, 'entrar')))

	user = driver.find_element_by_id('fUsuario')
	user.send_keys(keyData[0])
	
	passwd = driver.find_element_by_name('fContrasenia')
	passwd.send_keys(keyData[1])
	# driver.save_screenshot('login.png')
	
	button = driver.find_element_by_name('entrar')
	button.click()

def get_dolar(driver):
	WebDriverWait(driver, timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'label.res')))
	dolar=driver.find_element_by_css_selector('label.res')
	return dolar.text

def replace_dolar(dolar):
	f=fileinput.FileInput('config.py', inplace=True)
	for line in f:
		line = re.sub(r'dolar_cva=\d+\.*\d*','dolar_cva={0}'.format(dolar),line.strip("\r\n"))
		print line

def main():
	display = Display(visible=0, size=(1200, 720))
	display.start()

	driver = webdriver.Chrome()
	#driver = webdriver.Firefox()
	driver.set_window_size(1200, 720)
	
	login('ServiceURL', driver)
	dolar = get_dolar(driver)

	replace_dolar(dolar)

	driver.close()
	display.stop()

if __name__ == '__main__':
	main()

