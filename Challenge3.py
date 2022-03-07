from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
rows = driver.find_elements_by_xpath("//*[@class = 'tableFixHead']/table/tbody/tr")
total_amount = 0
total_amount_collected = driver.find_element_by_class_name("totalAmount").text

for row in range(1, len(rows) + 1):
    amount = int(driver.find_element_by_xpath(f"//*[@class = 'tableFixHead']/table/tbody/tr[{row}]/td[4]").text)
    total_amount += amount

if (f"Total Amount Collected: {total_amount}" == total_amount_collected):
    print(f"\nTotal Amount Collected value is correct: {total_amount}\n")
else:
    print(f"\nValues are not the same.\nAt web page the {total_amount_collected}\nThe sum performed results in a Total Amount Collected of {total_amount}\n")
