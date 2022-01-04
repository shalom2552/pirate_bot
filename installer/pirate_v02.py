from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import random
MINUTES = 60


def main(argv):
	login_file_path = argv[1]
	login_details = open(login_file_path, "r").read().split(",")
	print("Welcome to pirate Robot!")
	print("Login in with user:", login_details[0])

	start_time = time.time()

	DRIVER_PATH = "/home/marshall/bin/chromedriver"
	driver = webdriver.Chrome(DRIVER_PATH)

	url = "https://lobby.ikariam.gameforge.com/he_IL/?logout=1"
	driver.get(url)
	
	login_func(driver, login_details)
	go_to_pirate(driver)
	print("*******************************")

	run_number = 0
	while 1:
		try:
			print("Trying pirate check...")
			check_pirate(driver)
		except Exception as e:
			print("Exception: something went wrong.")
			print(e)
			go_to_pirate(driver)
			print("Retrying in 10s ...")
			time.sleep(10)
		else:
			print("Round:",run_number+1)
			print("No Exception.")
			run_number = run_number + 1 
			points = driver.find_element_by_class_name("value").text
			print("*******************************")
			print("Total score gained: " + str(points))
			wait_to_next_round(start_time)


def wait_to_next_round(start_time):
	now = time.time()
	passed = now - start_time
	if passed < 60:
		print('Time past: {:.2f}'.format(float(passed)) + 's')
	elif passed < 3600:
		print('Time past: {:.2f}'.format(float(passed/60)) + 'm')
	else:
		print('Time past: {:.2f}'.format(float(passed/3600)) + 'h')
	print("Waiting for next Round...")
	time.sleep(2.5 * MINUTES)


def check_pirate(driver):
	print("Looking for check button (20s)...")
	WebDriverWait(driver, 20).until(EC.visibility_of_element_located(
	(By.XPATH, "//*[@class='button capture']")))
	wait_random = random.randint(2,4) + random.randint(0,1) 
	print("waiting randomly: "+ str(wait_random) + "s")
	time.sleep(wait_random)
	driver.find_element_by_class_name("capture").click()
	print("Button clicked, pirates are on there way!")



def go_to_pirate(driver):
	try:
		driver.find_element_by_id("js_cityLink").click()
		print("City view.")
		driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
		WebDriverWait(driver, 10).until(
	    	EC.presence_of_element_located((By.ID, "js_CityPosition17Link")))
		time.sleep(1)
		driver.find_element_by_id("js_CityPosition17Link").click()
		time.sleep(1)
	except Exception as e:
		#print(e)
		print("ERROR: can't find pirates building!")
		print("Try again and make it visible.")
		time.sleep(2)
		exit()
	

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

	#login
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("password").send_keys(my_password)
	print("Login in...")

	# wait to load
	driver.find_elements_by_class_name("button-primary")[0].click()
	print("Joining Game...")
	WebDriverWait(driver, 5).until(
        	EC.presence_of_element_located((By.ID, "joinGame")))

	driver.find_element_by_class_name("button-primary").click()
	
	print("Loading dashboard...")
	WebDriverWait(driver, 10).until(
    	    EC.presence_of_element_located((By.ID, "dashboard")))
	driver.find_element_by_class_name("btn").click()
	driver.switch_to.window(driver.window_handles[-1])
	print(driver.title)
	


if __name__ == '__main__':
	main(sys.argv)