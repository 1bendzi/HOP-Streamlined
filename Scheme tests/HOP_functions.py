from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from datetime import date, datetime
import logging
import os
import time


def accept_cookies(driver):
    try:
        cookies_window = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="btnReject"]')))
        cookies_window.click()

        cookies_slider = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cookieManagement"]/form/div/div/div/label/span')))
        cookies_slider.click()
    except:
        driver.quit()

def open_menu(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()
    except:
        driver.quit()

def return_to_home(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()
    except:
        driver.quit()

def open_contact_us_demo(driver):
    try:
        contac_us_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[1]/a')))
        contac_us_link.click()

        digital_transformation_auto_enrolment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/a[1]')))
        digital_transformation_auto_enrolment_button.click()
    except:
        driver.quit()

def open_contact_us_scheme(driver):
    try:
        contac_us_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[1]/a')))
        contac_us_link.click()
    except:
        driver.quit()

def open_login_header(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()
        
        login_button_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[3]/a')))
        login_button_header.click()
    except:
        driver.quit()

def open_register_header(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        register_button_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[4]/a')))
        register_button_header.click()
    except:
        driver.quit()

def open_register_header_demo(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        register_button_header = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[4]/a')))
        register_button_header.click()

        digital_transformation_auto_enrolment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/a[1]')))
        digital_transformation_auto_enrolment_button.click()
    except:
        driver.quit()

def open_login_name_reminder(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()
        
        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()
        
        login_name_reminder_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/nav[1]/div/div[1]/ul/li[1]/a')))
        login_name_reminder_link.click()
    except:
        driver.quit()

def open_reset_password(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()
        
        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()
        
        reset_password_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/nav[1]/div/div[1]/ul/li[2]/a')))
        reset_password_link.click()
    except:
        driver.quit()    

def open_reset_pin(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()
        
        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()
        
        reset_pin_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/nav/div/div[1]/ul/li[3]/a')))
        reset_pin_link.click()
    except:
        driver.quit()

def open_application_options(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        application_options_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[2]/ul/li/a')))
        application_options_link.click()
    except:
        driver.quit()

def open_scheme_info(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        scheme_info_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/nav/div/div[3]/ul/li[2]/a')))
        scheme_info_link.click()
    except:
        driver.quit()
        
def open_scheme_info_demo(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        scheme_info_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div/div/div[2]/nav/div/div[3]/ul/li[2]/a')))
        scheme_info_link.click()

        digital_transformation_auto_enrolment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/a[1]')))
        digital_transformation_auto_enrolment_button.click()
    except:
        driver.quit()        

def open_inv_options(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        inv_options_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[4]/ul/li/a')))
        inv_options_link.click()
    except:
        driver.quit()

def open_inv_options_demo(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        inv_options_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[4]/ul/li/a')))
        inv_options_link.click()

        digital_transformation_auto_enrolment_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div[2]/main/div/a[1]')))
        digital_transformation_auto_enrolment_button.click()
    except:
        driver.quit()

def open_contact_us_menu(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        contact_us_menu_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[5]/ul/li[1]/a')))
        contact_us_menu_link.click()
    except:
        driver.quit()

def open_useful_addresses(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        useful_addresses_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[5]/ul/li[2]/a')))
        useful_addresses_link.click()
    except:
        driver.quit()

def open_useful_terms(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        menu_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-menu-btn"]/div/div')))
        menu_button.click()

        useful_terms_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="globalTopMenu"]/div/div[5]/ul/li[3]/a')))
        useful_terms_link.click()
    except:
        driver.quit()

def open_login_main(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        time.sleep(3)

        login_button_main = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tilePageTiles"]/div[2]/div/div[2]/a[1]')))
        login_button_main.click()
    except:
        driver.quit()

def open_register_main(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        register_button_main = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@id="tilePageTiles"]/div[2]/div/div[2]/a[2]')))
        register_button_main.click()
    except:
        driver.quit()

def open_accessibility(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        accessibility_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//html/body/div/footer/div/div[1]/div[2]/div/ul/li[1]/a')))
        accessibility_link.click()
    except:
        driver.quit()

def open_privacy(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        privacy_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/footer/div/div[1]/div[2]/div/ul/li[2]/a')))
        privacy_link.click()
    except:
        driver.quit()

def open_faq(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        faq_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/footer/div/div[1]/div[2]/div/ul/li[3]/a')))
        faq_link.click()
    except:
        driver.quit()

def open_terms(driver):
    try:
        home_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="staticBannerMenu"]/div[2]/div[2]/a')))
        home_link.click()

        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(3)

        terms_link = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/footer/div/div[1]/div[2]/div/ul/li[4]/a')))
        terms_link.click()
    except:
        driver.quit()


def save_text_to_evidence_by_xpath(driver, evidence_file, path):
    elements_on_the_page = driver.find_elements(By.XPATH, path)
    for element_on_the_page in elements_on_the_page:
        evidence_file.write(element_on_the_page.text + "\n")

    evidence_file.write("\n")

def save_text_to_evidence_by_class(driver, evidence_file, class_name):
    elements_on_the_page = driver.find_elements(By.CLASS_NAME, class_name)
    for element_on_the_page in elements_on_the_page:
        evidence_file.write(element_on_the_page.text + "\n")

    evidence_file.write("\n")

def save_text_to_evidence_by_id(driver, evidence_file, id_name):
    elements_on_the_page = driver.find_elements(By.ID, id_name)
    for element_on_the_page in elements_on_the_page:
        evidence_file.write(element_on_the_page.text + "\n")

    evidence_file.write("\n")

def scrape_demo():
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

def scrape_scheme (url, scheme_name):
    logging.getLogger('WDM').setLevel(logging.NOTSET)
    os.environ['WDM_LOG'] = "false"

    filename = "Scheme tests\Generated evidence\HOP_{scheme_name}_Evidence.txt"
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    evidence_file = open(f"Scheme tests\Generated evidence\HOP_{scheme_name}_Evidence.txt","w")
    evidence_file.close()
    evidence_file = open(f"Scheme tests\Generated evidence\HOP_{scheme_name}_Evidence.txt","a", encoding="utf-8")

    now = datetime.now()
    today = str(date.today())
    current_time = now.strftime("%H:%M:%S")
    evidence_file.write(f"{today}\n{current_time}\n")
    evidence_file.write('-' * 120)
    evidence_file.write('\n')

    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(f"{url}")
    driver.maximize_window()
    accept_cookies(driver)

    # M E N U  H E A D E R S

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
    open_contact_us_scheme(driver)
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

    # P E N S I O N  C O M M U N I C A T I O N (EXTERNAL PAGE)

    # S C H E M E  I N F O R M A T I O N
    open_scheme_info(driver)
    evidence_file.write(f"*Scheme Information WORDING: *\n")
    save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

    # I N V E S T M E N T  O P T I O N S
    open_inv_options(driver)
    evidence_file.write(f"*Investment Options WORDING: *\n")
    save_text_to_evidence_by_xpath(driver, evidence_file, '/html/body/div/div[2]/div[2]')

    # C O N T A C T  U S (ACCESSED FROM MENU)
    open_contact_us_scheme(driver)

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

    # C A P I T A  P L C  (EXTERNAL PAGE)

    # C A P I T A (EXTERNAL PAGE)

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
    driver.quit()