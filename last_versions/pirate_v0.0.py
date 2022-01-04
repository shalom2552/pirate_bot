from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys
import random



def main(argv):
	minute = 60
	# arfv[1]: login key
	# arfv[2]: gaiend yet
	#login_file_path = "login2.txt"
	login_file_path = argv[1]


	login_details = open(login_file_path, "r").read().split(",")
	print("Login user:", login_details[0])
	print("Starting...")

	DRIVER_PATH = "/home/marshall/bin/chromedriver"
	driver = webdriver.Chrome(DRIVER_PATH)

	url = "https://lobby.ikariam.gameforge.com/he_IL/?logout=1"
	driver.get(url)
	
	loginFunc(driver, login_details)
	driver.find_element_by_id("js_CityPosition17Link").click()

	run_number = 0
	while 1:
		print("round number:",run_number+1)
		try:
			print("trying pirate check...")
			gain = checkP(driver)
			print("gained: " + str(gain))
		except Exception as e:
			print("Exception:", e)
			excepts += 1
			#driver.quit()
		finally:
			print("time spend: " + str(run_number*2.5) + "m")
			print("waiting for next try...")
			run_number = run_number + 1 
			time.sleep(2.5*minute)
	



def loginFunc(driver, login_details):
	email = login_details[0]
	myPassword = login_details[1]

	# wait to load
	WebDriverWait(driver, 10).until(
        	EC.presence_of_element_located((By.ID, "registerTab")))
	print(driver.title)

	# click tab login
	items = driver.find_elements_by_tag_name("li")
	for item in items:
		if item.text == "התחברות":
			loginTab = item
	loginTab.click()

	#login
	driver.find_element_by_name("email").send_keys(email)
	driver.find_element_by_name("password").send_keys(myPassword)
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
	print("Loading page...")
	print(driver.title)
	WebDriverWait(driver, 10).until(
    	    EC.presence_of_element_located((By.ID, "js_CityPosition17Link")))


def checkP(driver):
	element = WebDriverWait(driver, 30).until(EC.visibility_of_element_located(
    (By.XPATH, "//*[@class='button capture']")))

	minute = random.randint(0,3) + 2
	print("waiting randomly: ",minute)
	time.sleep(minute)
	driver.find_element_by_class_name("capture").click()
	
	print("Button clicked.")
	print("capturring...")

	points = driver.find_element_by_class_name("value").text
	return points

 
if __name__ == '__main__':
	main(sys.argv)
