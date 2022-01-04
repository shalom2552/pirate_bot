import time
import sys
import random


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains


###########################################
# Fill your info here
USER_EMAIL = "mail@mail.com"
USER_PASSWORD = "YourPassword"
###########################################
DRIVER_PATH = "/home/marshall/bin/chromedriver"
###########################################


ROUND = 150
START = time.time()
LOGIN_DETAILS = [USER_EMAIL, USER_PASSWORD]
###########################################


# args[1] : login file path
# remove log in file open
def main(argv):
	login_file_path = argv[1]
	LOGIN_DETAILS = open(login_file_path, "r").read().split(",")
	
	driver = webdriver.Chrome(DRIVER_PATH)
	url = "https://lobby.ikariam.gameforge.com/he_IL/?logout=1"
	driver.get(url)
	
	print(" @ Welcome to pirate bot! version-0.4")
	print(" * Login in with user:", LOGIN_DETAILS[0])
	
	try:
		login_func(driver, LOGIN_DETAILS)
	except Exception as e:
		print(" ! ERROR: cannot log in. something is wrong. try again.")
		print(" ! Try again. make sure buttons are visible.")
		time.sleep(3)
		exit()
	else:
		print(" + Login successfully!")
	go_to_pirate(driver)
	
	run_number = 0
	while 1:
		try:
			# print(" * Trying pirate check...")
			# while in_progress(driver):
			# 	timer("Alerady on the go. Retrying in", 10)
			check_pirate(driver)
			if not in_progress(driver):
				print(" ! ERROR: Try Bot check")
				input("Press any key to continue:")
		except Exception as e:
			print(" ! Exception: something went wrong.")
			#print(" ! Message: ",e)
			timer("Retrying in", 10)
			go_to_pirate(driver)
		else:
			print_time()
			points = driver.find_element_by_class_name("value").text
			run_number = run_number + 1 
			print("*********************************************")
			print(" + Round:",run_number+1)
			print(" + Total score gained: " + str(points))
			timer("Waiting for next Round", ROUND )


# try to locate progress bar
def in_progress(driver):
	try:
		print(" * Testing operation...")
		WebDriverWait(driver, 10).until(
    			EC.presence_of_element_located((By.ID, "missionProgressBar")))
		print(" + Operation on the go.")
		return True
	except Exception as e:
		print(" ! ERROR: cannot find progress bar, check button did not worked.")		
		return False



# check if in pirate building
def in_pirates(driver):
	try:
		WebDriverWait(driver, 10).until(
			EC.presence_of_element_located(By.ID, "pirateHighscoreContainer"))
	except Exception as e:
		return False
	else:
		print(" * Alerady in pirate building.")
		return True


# print the time past since started
def print_time():
	now = time.time()
	passed = now - START
	if passed < 60:
		print(' + Working time: {:.2f}'.format(float(passed)) + 's')
	elif passed < 3600:
		print(' + Working time: {:.2f}'.format(float(passed/60)) + 'm')
	else:
		print(' + Working time: {:.2f}'.format(float(passed/3600)) + 'h')


# print a flushing timer in the terminal
def timer(string, amount):
	for remaining in range(amount, -1, -1):
		sys.stdout.write("\r")
		sys.stdout.write(" # "+string+"({}): {:2d}s".format(amount, remaining)) 
		sys.stdout.flush()
		time.sleep(1)
	print(" * Loading...")


# locate the check button and click it
def check_pirate(driver):
	# id(missionProgressBar)
	# if bar is not in the page then may be this is a robot check
	print(" * Looking for check button (20s)")
	try:
		WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
			(By.XPATH, "//*[@class='button capture']")))
	except Exception as e:
		print(" ! ERROR: canot find capture button.")
		raise
	
	wait_random = random.randint(1,3) + random.randint(1,2) 
	timer("waiting randomly", wait_random)
	try:
		driver.find_element_by_class_name("capture").click()
	except Exception as e:
		print(" ! ERROR: canot click button.")
		city_view(driver)

	else:
		print(" + Button clicked, pirates are on there way!")


# navigate to pirate building
def go_to_pirate(driver):
	# pirat position at: (337, 454) 
	# TODO :: scrol to (337, 454)
	if in_pirates(driver): return

	try:
		print(" * Going to city_view...")
		WebDriverWait(driver, 10).until(
	    		EC.presence_of_element_located((By.ID, "js_cityLink")))
		driver.find_element_by_id("js_cityLink").click()
		print(" > City view")
		#time.sleep(3)
	except Exception as e:
		print(" ! ERROR: canot go to city_view.")
		raise e
	try:
		print(" * Going to pirates building...")
		WebDriverWait(driver, 20).until(
	    	EC.presence_of_element_located((By.ID, "js_CityPosition17Link")))
		print(" > Pirates building.")
		driver.find_element_by_id("js_CityPosition17Link").click()
		time.sleep(5)
	except Exception as e:
		print(" ! ERROR: can't find pirates building!")
		



# init function to log into the game with the specified acount details
def login_func(driver, login_details):
	email = login_details[0]
	my_password = login_details[1]

	# wait to load
	WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "registerTab")))
	print(driver.title)
	# click tab login
	items = driver.find_elements_by_tag_name("li")
	for item in items:
		if item.text == "התחברות":
			item.click()
			break
	# login
	print(" * Login in...")
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("password").send_keys(my_password)
	#time.sleep(2)
	driver.find_elements_by_class_name("button-primary")[0].click()

	# wait to load
	print(" * Joining Game...")
	WebDriverWait(driver, 5).until(
        	EC.presence_of_element_located((By.ID, "joinGame")))
	#time.sleep(2)
	driver.find_element_by_class_name("button-primary").click()
	
	print(" * Loading dashboard...")
	WebDriverWait(driver, 15).until(
    	    EC.presence_of_element_located((By.ID, "dashboard")))
	driver.find_element_by_class_name("btn").click()
	driver.switch_to.window(driver.window_handles[-1])
	driver.execute_script("window.scrollTo(0,0)")
	print(driver.title)
	


if __name__ == '__main__':
	main(sys.argv)