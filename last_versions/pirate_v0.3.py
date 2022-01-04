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

ROUND = 150
START = time.time()
LOGIN_DETAILS = [USER_EMAIL, USER_PASSWORD]

def main(argv):
	login_file_path = argv[1]
	LOGIN_DETAILS = open(login_file_path, "r").read().split(",")
	print("Welcome to pirate bot! version-0.3")
	print(" * Login in with user:", LOGIN_DETAILS[0])
	driver = webdriver.Chrome(DRIVER_PATH)
	url = "https://lobby.ikariam.gameforge.com/he_IL/?logout=1"
	driver.get(url)
	login_func(driver, LOGIN_DETAILS)
	city_view(driver)
	go_to_pirate(driver)
	run_number = 0
	while 1:
		try:
			print(" * Trying pirate check...")
			check_pirate(driver)
		except Exception as e:
			print(" ! Exception: something went wrong.")
			timer("Retrying in", 5)
			go_to_pirate(driver)
		else:
			print_time()
			points = driver.find_element_by_class_name("value").text
			run_number = run_number + 1 
			print("*******************************")
			print(" + Round:",run_number+1)
			print(" + Total score gained: " + str(points))
			timer("Waiting for next Round", ROUND )


def city_view(driver):
	print(" * Going to city_view...")
	try:
		WebDriverWait(driver, 10).until(
	    		EC.presence_of_element_located((By.ID, "js_cityLink")))
		driver.find_element_by_id("js_cityLink").click()
		print(" > City view")
		#time.sleep(3)
	except Exception as e:
		print(" ! ERROR: canot go to city_view.")

def print_time():
	now = time.time()
	passed = now - START
	if passed < 60:
		print(' + Working time: {:.2f}'.format(float(passed)) + 's')
	elif passed < 3600:
		print(' + Working time: {:.2f}'.format(float(passed/60)) + 'm')
	else:
		print(' + Working time: {:.2f}'.format(float(passed/3600)) + 'h')


def timer(string, amount):
	for remaining in range(amount, -1, -1):
		sys.stdout.write("\r")
		sys.stdout.write(" # "+string+": {:2d}s".format(remaining)) 
		sys.stdout.flush()
		time.sleep(1)
	print(" * Loading...")


def check_pirate(driver):
	# id(missionProgressBar)
	# if bar is not in the page then may be this is a robot check
	print(" * Looking for check button (20s)")
	try:
		WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
			(By.XPATH, "//*[@class='button capture']")))
	except Exception as e:
		print(" ! ERROR: canot find capture button.")
		go_to_pirate(driver)
		raise e
	
	wait_random = random.randint(1,3) + random.randint(1,2) 
	timer("waiting randomly", wait_random)
	try:
		driver.find_element_by_class_name("capture").click()
	except Exception as e:
		print(" ! ERROR: canot click button.")
		city_view(driver)
		raise e
	else:
		print(" + Button clicked, pirates are on there way!")


def go_to_pirate(driver):
	# pirat position at: (337, 454) 
	# TODO :: scrol to (337, 454)
	print(" * Going to pirates building...")
	try:
		WebDriverWait(driver, 20).until(
	    	EC.presence_of_element_located((By.ID, "js_CityPosition17Img")))
		print(" > Pirates building.")
		driver.find_element_by_id("js_CityPosition17Link").click()
		time.sleep(5)
	except Exception as e:
		city_view(driver)
		print(" ! ERROR: can't find pirates building!")
		raise e


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
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("password").send_keys(my_password)
	print(" * Login in...")

	# wait to load
	driver.find_elements_by_class_name("button-primary")[0].click()
	print(" * Joining Game...")
	WebDriverWait(driver, 5).until(
        	EC.presence_of_element_located((By.ID, "joinGame")))

	driver.find_element_by_class_name("button-primary").click()
	
	print(" * Loading dashboard...")
	WebDriverWait(driver, 15).until(
    	    EC.presence_of_element_located((By.ID, "dashboard")))
	driver.find_element_by_class_name("btn").click()
	driver.switch_to.window(driver.window_handles[-1])
	driver.execute_script("window.scrollTo(0,0)")
	print(driver.title)
	

# class EXCEPT_ROBOT_CHECK(object):
# 	"""docstring for EXCEPT_ROBOT_CHECK"""
# 	def __init__(self, arg):
# 		super(EXCEPT_ROBOT_CHECK, self).__init__()
# 		self.arg = arg


if __name__ == '__main__':
	main(sys.argv)