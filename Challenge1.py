from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
autocomplete_box = driver.find_element_by_id("autocomplete")
autocomplete_box.send_keys("Vene")
not_found = True
timeout = time.time() + 10

while (not_found and timeout > time.time()):
    try:
        driver.find_element_by_class_name("ui-menu-item-wrapper").click()
        not_found = False
    except:
        print("Waiting for autocomplete option")
        time.sleep(1)

if (autocomplete_box.get_attribute('value') == "Venezuela"):
    print("\nAutocomplete finished.\n")
else:
    print("\nSomething went wrong.\n")