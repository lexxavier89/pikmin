import os
import tempfile
import time

from selenium import webdriver
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

# Open the browser
driver = webdriver.Edge()
driver.maximize_window()
wait = WebDriverWait(driver, 10)

# Open the website
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(1)

# Name
driver.find_element(By.ID, "name").send_keys("Louise Diaz")
time.sleep(1)
# Email
driver.find_element(By.ID, "email").send_keys("louise@example.com")
time.sleep(1)
# Phone
driver.find_element(By.ID, "phone").send_keys("09123456789")
time.sleep(1)
# Address
driver.find_element(By.ID, "textarea").send_keys("Cebu City, Philippines")
time.sleep(1)

# Gender
driver.find_element(By.ID, "female").click()
time.sleep(1)

# Days (Sunday to Saturday)
driver.find_element(By.ID, "sunday").click()
time.sleep(1)
driver.find_element(By.ID, "monday").click()
time.sleep(1)
driver.find_element(By.ID, "tuesday").click()
time.sleep(1)
driver.find_element(By.ID, "wednesday").click()
time.sleep(1)
driver.find_element(By.ID, "thursday").click()
time.sleep(1)
driver.find_element(By.ID, "friday").click()
time.sleep(1)
driver.find_element(By.ID, "saturday").click()
time.sleep(1)

# Country
driver.find_element(By.ID, "country").click()
time.sleep(1)
country_dropdown = Select(driver.find_element(By.ID, "country"))
country_dropdown.select_by_visible_text("Japan")
time.sleep(1)

# Colors
colors_dropdown = Select(driver.find_element(By.ID, "colors"))
colors_dropdown.select_by_visible_text("Blue")
time.sleep(1)
colors_dropdown.select_by_visible_text("Green")
time.sleep(1)

# Animals
animals_dropdown = Select(driver.find_element(By.ID, "animals"))
animals_dropdown.select_by_visible_text("Dog")
time.sleep(1)

# Date Picker 1
driver.find_element(By.ID, "datepicker").click()
time.sleep(1)
while driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text != "2026" or driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text != "August":
    driver.find_element(By.CLASS_NAME, "ui-datepicker-prev").click()
    time.sleep(0.05)
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div' and contains(@style,'display: block')]//a[text()='9']").click()
time.sleep(1)

# Date Picker 2
driver.find_element(By.ID, "txtDate").click()
time.sleep(1)
year_dropdown = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-year"))
year_dropdown.select_by_visible_text("2026")
time.sleep(1)
month_dropdown = Select(driver.find_element(By.CLASS_NAME, "ui-datepicker-month"))
month_dropdown.select_by_visible_text("Aug")
time.sleep(1)
driver.find_element(By.XPATH, "//div[@id='ui-datepicker-div' and contains(@style,'display: block')]//a[text()='9']").click()
time.sleep(1)

# Date Picker 3 (Date Range)
driver.find_element(By.ID, "start-date").send_keys("08/09/2026")
time.sleep(1)
driver.find_element(By.ID, "start-date").send_keys(Keys.ESCAPE)
time.sleep(1)
driver.find_element(By.ID, "end-date").send_keys("12/16/2026")
time.sleep(1)
driver.find_element(By.ID, "end-date").send_keys(Keys.ESCAPE)
time.sleep(1)

# Submit
driver.find_element(By.CLASS_NAME, "submit-btn").click()
time.sleep(1)

# Create the test files for upload
temp_folder = tempfile.gettempdir()
first_file_path = os.path.join(temp_folder, "test_file_1.txt")
second_file_path = os.path.join(temp_folder, "test_file_2.txt")

first_file = open(first_file_path, "w")
first_file.write("First test file")
first_file.close()

second_file = open(second_file_path, "w")
second_file.write("Second test file")
second_file.close()

# Upload Single File
driver.find_element(By.ID, "singleFileInput").send_keys(first_file_path)
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Upload Single File']").click()
time.sleep(1)

# Upload Multiple Files
driver.find_element(By.ID, "multipleFilesInput").send_keys(first_file_path + "\n" + second_file_path)
time.sleep(1)
driver.find_element(By.XPATH, "//button[text()='Upload Multiple Files']").click()
time.sleep(1)

# Static Web Table
table_rows = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr")
table_columns = driver.find_elements(By.XPATH, "//table[@name='BookTable']//tr[1]/th")
for row_number in range(2, len(table_rows) + 1):
    book_name = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row_number) + "]/td[1]").text
    author = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row_number) + "]/td[2]").text
    subject = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row_number) + "]/td[3]").text
    price = driver.find_element(By.XPATH, "//table[@name='BookTable']//tr[" + str(row_number) + "]/td[4]").text

# Pagination Web Table
page_buttons = driver.find_elements(By.XPATH, "//ul[@id='pagination']/li")
total_pages = len(page_buttons)
for page_number in range(1, total_pages + 1):
    driver.find_element(By.XPATH, "//ul[@id='pagination']/li[" + str(page_number) + "]/a").click()
    time.sleep(1)
    product_rows = driver.find_elements(By.XPATH, "//table[@id='productTable']/tbody/tr")
    for product_row in product_rows:
        product_id = product_row.find_element(By.XPATH, "./td[1]").text
        product_name = product_row.find_element(By.XPATH, "./td[2]").text
        product_price = product_row.find_element(By.XPATH, "./td[3]").text
        product_row.find_element(By.XPATH, "./td[4]/input").click()
        time.sleep(1)

# Wikipedia Search
driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input").send_keys("Honkai")
time.sleep(1)
driver.find_element(By.CLASS_NAME, "wikipedia-search-button").click()
time.sleep(2)
# Open the Wikipedia result then go back to the site
wiki_main_window = driver.current_window_handle
driver.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div[4]/div[3]/div/aside/div/div[1]/div[1]/div[2]/div[1]/a").click()
time.sleep(3)
if len(driver.window_handles) > 1:
    for window in driver.window_handles:
        if window != wiki_main_window:
            driver.switch_to.window(window)
            time.sleep(2)
            driver.close()
    driver.switch_to.window(wiki_main_window)
else:
    driver.back()
time.sleep(2)

# Dynamic Button
start_button = driver.find_element(By.XPATH, "//button[text()='START']")
start_button.click()
time.sleep(1)
stop_button = driver.find_element(By.XPATH, "//button[text()='STOP']")
stop_button.click()
time.sleep(1)

# Simple Alert
driver.find_element(By.ID, "alertBtn").click()
time.sleep(1)
wait.until(expected_conditions.alert_is_present())
simple_alert = Alert(driver)
simple_alert.accept()
time.sleep(1)

# Confirmation Alert
driver.find_element(By.ID, "confirmBtn").click()
time.sleep(1)
wait.until(expected_conditions.alert_is_present())
confirm_alert = Alert(driver)
confirm_alert.dismiss()
time.sleep(1)

# Prompt Alert
driver.execute_script("var originalPrompt = window.prompt; window.prompt = function(message) { return originalPrompt(message, 'Can you blow my whistle baby'); };")
time.sleep(1)
driver.find_element(By.ID, "promptBtn").click()
time.sleep(1)
wait.until(expected_conditions.alert_is_present())
prompt_alert = Alert(driver)
time.sleep(2)
prompt_alert.accept()
time.sleep(1)

# New Tab
main_window = driver.current_window_handle

driver.find_element(By.XPATH, "//button[text()='New Tab']").click()
time.sleep(2)
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        time.sleep(1)
        driver.close()
        time.sleep(1)
driver.switch_to.window(main_window)
time.sleep(1)

# Popup Windows
driver.find_element(By.ID, "PopUp").click()
time.sleep(2)
for window in driver.window_handles:
    if window != main_window:
        driver.switch_to.window(window)
        time.sleep(1)
        driver.close()
        time.sleep(1)
driver.switch_to.window(main_window)
time.sleep(1)

# Mouse Hover
point_me_button = driver.find_element(By.CLASS_NAME, "dropbtn")
ActionChains(driver).move_to_element(point_me_button).perform()
time.sleep(1)
mobiles_link = driver.find_element(By.LINK_TEXT, "Mobiles")
laptops_link = driver.find_element(By.LINK_TEXT, "Laptops")

# Double Click
first_field = driver.find_element(By.ID, "field1")
first_field.clear()
time.sleep(1)
first_field.send_keys("Hello Selenium")
time.sleep(1)
copy_button = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
ActionChains(driver).double_click(copy_button).perform()
time.sleep(1)

# Drag and Drop
drag_element = driver.find_element(By.ID, "draggable")
drop_element = driver.find_element(By.ID, "droppable")
ActionChains(driver).drag_and_drop(drag_element, drop_element).perform()
time.sleep(1)

# Slider
slider_handles = driver.find_elements(By.XPATH, "//div[@id='slider-range']/span")
ActionChains(driver).click_and_hold(slider_handles[0]).move_by_offset(40, 0).release().perform()
time.sleep(1)
ActionChains(driver).click_and_hold(slider_handles[1]).move_by_offset(-40, 0).release().perform()
time.sleep(1)

# Scrolling Dropdown
driver.find_element(By.ID, "comboBox").click()
time.sleep(1)
dropdown_items = driver.find_elements(By.XPATH, "//div[@id='dropdown']/div")
if len(dropdown_items) > 0:
    last_item = dropdown_items[len(dropdown_items) - 1]
    driver.execute_script("arguments[0].scrollIntoView();", last_item)
    time.sleep(1)
    last_item.click()
    time.sleep(1)

# Labels and Links
laptop_link_names = ["Apple", "Lenovo", "Dell"]
for link_name in laptop_link_names:
    laptop_main_window = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, link_name).click()
    time.sleep(3)
    if len(driver.window_handles) > 1:
        for window in driver.window_handles:
            if window != laptop_main_window:
                driver.switch_to.window(window)
                driver.close()
        driver.switch_to.window(laptop_main_window)
    else:
        driver.back()
    time.sleep(2)

# Broken Links
error_codes = ["400", "401", "403", "404", "408", "500", "502", "503"]
for error_code in error_codes:
    error_main_window = driver.current_window_handle
    driver.find_element(By.LINK_TEXT, "Errorcode " + error_code).click()
    time.sleep(3)
    if len(driver.window_handles) > 1:
        for window in driver.window_handles:
            if window != error_main_window:
                driver.switch_to.window(window)
                driver.close()
        driver.switch_to.window(error_main_window)
    else:
        driver.back()
    time.sleep(2)

# Shadow DOM
shadow_host = driver.find_element(By.ID, "shadow_host")
shadow_root = shadow_host.shadow_root
shadow_input = shadow_root.find_element(By.CSS_SELECTOR, "input[type='text']")
shadow_input.send_keys("Inside shadow DOM")
time.sleep(1)

# Screenshot
driver.save_screenshot("final_page.png")

# Close the browser
time.sleep(2)
driver.quit()
