import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common import by
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.by import By
import os
chrome_options = Options()
import time



chrome_options.add_argument("--headless")
chrome_options.add_argument("--reduce-security-for-testing")
chrome_options.add_argument("--disable-web-security")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)
start_url = "https://127.0.0.1:8834/#/"
driver.get(start_url)
wait = ui.WebDriverWait(driver, 30)


def login():
    try:
    #time.sleep(4)
        login_username = wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/form/div[1]/input" )))
        login_pass = driver.find_element_by_xpath('/html/body/div[1]/form/div[2]/input')
        login_button = driver.find_element_by_xpath("/html/body/div[1]/form/button")
    except NoSuchElementException as e:
        print(e)
    login_username.send_keys("admin")
    login_pass.send_keys("admin")
    login_button.click()

def create_scan(scan_name, sshUsername):
    try:
        new_scan_button = driver.find_element_by_xpath("/html/body/section[3]/section[1]/a[1]")
        new_scan_button.click()
        time.sleep(2)
        scan_method = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/div[1]/div[2]/div[2]/a[7]")
        scan_method.click()
        time.sleep(4)
        new_scan_name = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[1]/div/input")
        new_scan_name.send_keys(scan_name)
        time.sleep(2)

        #read file of ips
        file = open("hosts_to_scan.txt", "r")
        content = file.read()
        targets_file = content.split(",")
        file.close()
        targets_file = list(map(lambda s: s.strip(), targets_file))
        print(targets_file)
        targets_hosts = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div[1]/div[5]/div/textarea")
        targets_hosts.click()
        time.sleep(2)
        for ip in targets_file:
            str = ip + ', ' + '\n'
            targets_hosts.send_keys(str)

#targets_file.send_keys(os.getcwd() + 'hosts_to_scan.txt')


        time.sleep(2)
        credential_tab = driver.find_element_by_xpath("/html/body/section[3]/section[2]/a[2]")
        credential_tab.click()
#save_scan_button = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[2]/span")
#save_scan_button.click()

        time.sleep(3)
        ssh_option_button = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[1]/div/div[2]/ul[3]/li[2]/div/span[2]")
        ssh_option_button.click()

        time.sleep(3)

        ssh_username = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[1]/div/input")
        ssh_username.send_keys(sshUsername)

        time.sleep(3)

        file = '/gkey'
        private_key_add_button = driver.find_element_by_xpath("/html/body/section[3]/section[3]/section/form/div[1]/div/div/div[1]/section/div[1]/div[2]/ul/li[2]/div[2]/div/div[6]/div[2]/div/a")
        private_key_add_button.send_keys(os.getcwd() + 'gkey')
        print(os.getcwd())

    except NoSuchElementException as e:
        print(e)
    


login()
time.sleep(3)

create_scan(sys.argv[1], sys.argv[2])

driver.quit()



