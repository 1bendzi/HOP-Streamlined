from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, datetime
from HOP_functions import *
import time
import logging
import os

logging.getLogger('WDM').setLevel(logging.NOTSET)
os.environ['WDM_LOG'] = "false"

# print("\n\033[1mScript has been started!\033[0m\n")
filename = "Scheme tests\Generated evidence\HOP_Corvidae_Evidence.txt"
os.makedirs(os.path.dirname(filename), exist_ok=True)

evidence_file = open("Scheme tests\Generated evidence\HOP_Corvidae_Evidence.txt","w")
evidence_file.close()
evidence_file = open("Scheme tests\Generated evidence\HOP_Corvidae_Evidence.txt","a", encoding="utf-8")

now = datetime.now()
today = str(date.today())
current_time = now.strftime("%H:%M:%S")
evidence_file.write(f"{today}\n{current_time}\n")
evidence_file.write('-' * 120)
evidence_file.write('\n')

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get("https://qaportal.hartlinkonline.co.uk/corvidae")
driver.maximize_window()
accept_cookies(driver)

# M E N U  H E A D E R S - T E S T

open_menu(driver)
evidence_file.write(f"\n*MENU HEADERS: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '//*[@id="globalTopMenu"]/div')

# H E A D E R  R I G H T  S I D E
evidence_file.write(f"*HEADER RIGHT SIDE ELEMENTS: *\n")
save_text_to_evidence_by_id(driver, evidence_file, 'staticBannerMenu')

# A A A  C H E C K
return_to_home(driver)
smallest_a = driver.find_element(By.XPATH, '//*[@id="textSmall"]')
middle_a = driver.find_element(By.XPATH, '//*[@id="textMedium"]')
biggest_a = driver.find_element(By.XPATH, '//*[@id="textLarge"]')
contact_us_button = driver.find_element(By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[1]/a')
biggest_a.click()
time.sleep(1)
evidence_file.write(f"Contact Us font-size when biggest A is selected (correct value is: 26px): {contact_us_button.value_of_css_property('font-size')}\n")
middle_a.click()
time.sleep(1)
evidence_file.write(f"Contact Us font-size when middle A is selected (correct value is: 23px): {contact_us_button.value_of_css_property('font-size')}\n")
smallest_a.click()
time.sleep(1)
evidence_file.write(f"Contact Us font-size when smallest A is selected (correct value is: 20px): {contact_us_button.value_of_css_property('font-size')}\n\n")

# P A G E  B O D Y  E L E M E N T S
evidence_file.write(f"*Page Body ELEMENTS: *\n")
save_text_to_evidence_by_id(driver, evidence_file, 'tilePageTiles')

# F O O T E R
evidence_file.write(f"*Footer ELEMENTS: *\n")
save_text_to_evidence_by_class(driver, evidence_file, 'hop-footer')

# C O N T A C T  U S
open_contact_us_demo(driver)
evidence_file.write(f"*Contact Us WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# L O G I N (ACCESSED FROM HEADER BUTTON)
open_login_header(driver)
evidence_file.write(f"*LOGIN WORDING (from header button): *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

evidence_file.write(f"*LOGIN WORDING (help icons text): *\n")
tooltips = driver.find_elements(By.CLASS_NAME, 'hop-tooltip-description')
for tooltip in tooltips:
    content = tooltip.get_attribute('innerText')
    evidence_file.write(content)

evidence_file.write(f"\n\n")

# # R E G I S T E R (ACCESSED FROM HEADER BUTTON)
open_register_header(driver)
evidence_file.write(f"*REGISTER WORDING (from header button): *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div[1]/div[2]/div[2]')

evidence_file.write(f"*REGISTER WORDING (help icons text): *\n")
tooltips = driver.find_elements(By.CLASS_NAME, 'hop-tooltip-description')
for tooltip in tooltips:
    content = tooltip.get_attribute('innerText')
    evidence_file.write(content)

# # L O G I N  N A M E  R E M I N D E R
open_login_name_reminder(driver)
evidence_file.write(f"*LOGIN NAME REMINDER WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]/main/form')

# # R E S E T  P A S S W O R D
open_reset_password(driver)
evidence_file.write(f"*RESET PASSWORD WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]/main/form')

# # R E S E T  P I N
open_reset_pin(driver)
evidence_file.write(f"*RESET PIN WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]/main/form')

# A P P L I C A T I O N  O P T I O N S
open_application_options(driver)
evidence_file.write(f"*Application Options page WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# P E N S I O N  C O M M U N I C A T I O N (LINK CHECK, EXTERNAL PAGE)

# S C H E M E  I N F O R M A T I O N
open_scheme_info(driver)
evidence_file.write(f"*Scheme Information WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# I N V E S T M E N T  O P T I O N S
open_inv_options(driver)
evidence_file.write(f"*Investment Options WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# C O N T A C T  U S (ACCESSED FROM MENU)
open_contact_us_menu(driver)

# U S E F U L  A D D R E S S E S
open_useful_addresses(driver)
evidence_file.write(f"*Useful Addresses WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# U S E F U L  T E R M S
open_useful_terms(driver)
evidence_file.write(f"*Useful Terms WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# L O G I N (ACCESSED FROM PAGE BODY BUTTON)
open_login_main(driver)
evidence_file.write(f"*LOGIN WORDING (from main page button): *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

# R E G I S T E R (ACCESSED FROM PAGE BODY BUTTON)
open_register_main(driver)
evidence_file.write(f"*REGISTER WORDING (from main page button): *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div[1]/div[2]/div[2]')

# C A P I T A  P L C  (LINK CHECK, EXTERNAL PAGE)

# C A P I T A (LINK CHECK, EXTERNAL PAGE)

# A C C E S S I B I L I T Y
open_accessibility(driver)
evidence_file.write(f"*Accessibility WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '//*[@id="accessibility"]')

# P R I V A C Y  &  C O O K I E  P O L I C Y
open_privacy(driver)
evidence_file.write(f"*Privacy & Cookie Policy WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '//*[@id="privacyPolicy"]')

evidence_file.write(f"*Privacy & Cookie Policy WORDING inside accordion headers: *\n")
open_privacy(driver)
headers_wording = driver.find_elements(By.CLASS_NAME, 'ui-accordion-content')
for header_wording in headers_wording:
    evidence_file.write(header_wording.get_attribute('innerText'))

evidence_file.write('\n')

# F A Q
open_faq(driver)
evidence_file.write(f"*FAQ WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '//*[@id="faq"]/section[2]/div')

evidence_file.write(f"*FAQ WORDING inside accordion headers: *\n")
open_faq(driver)
header_container = driver.find_element(By.CLASS_NAME, 'search-results-area')
for header in header_container.find_elements(By.CLASS_NAME, 'accordion.search-result'):
    content = header.find_element(By.CLASS_NAME, 'ui-accordion-content').get_attribute('innerText')
    evidence_file.write(content)

evidence_file.write('\n')

# T E R M S  &  C O N D I T I O N S
open_terms(driver)
evidence_file.write(f"*Terms & Conditions WORDING: *\n")
save_text_to_evidence_by_xpath(driver, evidence_file, '//*[@id="tncPage"]')


evidence_file.close()
# print('-' * 120)
# print("\n\033[1mEvidence file was successfully generated!\033[0m\n")

driver.quit()