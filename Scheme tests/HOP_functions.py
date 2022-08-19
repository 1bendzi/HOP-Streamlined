from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
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
