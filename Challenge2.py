from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
rows = driver.find_elements_by_xpath("//*[@class = 'table-display']/tbody/tr")

for row in range(2, len(rows) + 1):
    price = int(driver.find_element_by_xpath(f"//*[@class = 'table-display']/tbody/tr[{row}]/td[3]").text)
    
    if (price > 30):
        course = driver.find_element_by_xpath(f"//*[@class = 'table-display']/tbody/tr[{row}]/td[2]").text
        instructor = driver.find_element_by_xpath(f"//*[@class = 'table-display']/tbody/tr[{row}]/td[1]").text
        print(f"\n{course} by {instructor} costs ${price}.\n")