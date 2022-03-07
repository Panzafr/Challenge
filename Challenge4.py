from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
items = driver.find_elements_by_xpath("/html/body/app-root/div[1]/header/div[2]/div[1]/div[1]/div[2]/nav/div[2]/ul/li")
header_items = []

for item in range(1, len(items) + 1):
     name = driver.find_element_by_xpath(f"/html/body/app-root/div[1]/header/div[2]/div[1]/div[1]/div[2]/nav/div[2]/ul/li[{item}]/a").text
     header_items.append(name)

print(header_items)