from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
	login_file_path = "login2.txt"
	login_details = open(login_file_path, "r").read().split(",")
	print("Login user:", login_details[0])
	print("Starting...")

	DRIVER_PATH = "/home/marshall/bin/chromedriver"
	driver = webdriver.Chrome(DRIVER_PATH)

	url = "https://lobby.ikariam.gameforge.com/he_IL/?logout=1"
	driver.get(url)
	
	print("Starting Seasion: ")
	time.sleep(1.5)
	try:
		loginFunc(driver, login_details)
	except Exception as e:
		print(e)
		print("Yall thing im a robot?")
		print("Lets try again...")
		pass
	else:
		print("No-Exc.")
		pass

	# work = True
	# while work:
	# 	driver.quit()
	# 	try:
			
	# 	except Exception as e:
	# 		driver.quit()
	# 		print("Retring...")
	# 	else:
	# 		work = False
	# 		print("succes!")
	# 	finally:
	# 		pass
	

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
    	    EC.presence_of_element_located((By.ID, "topnavi")))
	driver.find_element_by_id("js_islandLink").click()
	print("Island view.")

	driver.find_element_by_id("js_cityLocation13Link").click()
	print("Collecting data...")
	WebDriverWait(driver, 10).until(
    	    EC.presence_of_element_located((By.ID, "js_selectedCityScore")))


	scores = [
		driver.find_element_by_id("js_selectedCityScore").text, 
		driver.find_element_by_id("js_selectedCityScoreBuildings").text,
		driver.find_element_by_id("js_selectedCityScoreResearch").text,
		driver.find_element_by_id("js_selectedCityScoreArmy").text
	]
	
	print("Data collected:",scores)

	print("closing in 3 sec..")
	time.sleep(3)
	#driver.quit()




if __name__ == '__main__':
	main()
