import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from urllib3 import disable_warnings
from time import sleep

disable_warnings()

Service(ChromeDriverManager().install())

nopecha_key = ''

options = Options()
# options.add_argument('--no-sandbox')
options.add_argument('--disable-infobars')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)

with open('ext.crx', 'wb') as f:
    f.write(requests.get('https://nopecha.com/f/ext.crx').content)
options.add_extension('ext.crx')

driver = webdriver.Chrome(options=options)
driver.set_window_size(1280, 1024)

driver.get(f"https://nopecha.com/setup#{nopecha_key}")
sleep(2)

# driver.get('https://nopecha.com/demo/recaptcha')
driver.get('https://www.coingecko.com/')
sleep(7)
login = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[1]/div/div[3]/button[1]')
login.click()
sleep(3)
botao_logar = driver.find_element(By.XPATH, '/html/body/div[7]/div/div[2]/div[3]/div/div/div[1]/div[5]/div[1]/button')
botao_logar.click()
sleep(3)
usuario = driver.find_element(By.XPATH, '//*[@id="user_email"]')
usuario.send_keys('')
senha = driver.find_element(By.XPATH, '//*[@id="user_password"]')
senha.send_keys(r'')
sleep(3)
logar = driver.find_element(By.CSS_SELECTOR, 'form.new_user:nth-child(1) > div:nth-child(5) > button:nth-child(1) > div:nth-child(1)')
logar.click()
sleep(7)
definicoes_close = driver.find_element(By.XPATH, '//*[@id="onboarding-preferences"]/div[4]/div[2]/button')
definicoes_close.click()
sleep(5)
candy = driver.find_element(By.XPATH, '/html/body/header/div[2]/div[3]/div/div[3]/div[7]/a/div[2]')
candy.click()
sleep(5)
coletar = driver.find_element(By.XPATH, '//*[@id="collectButton"]')
coletar.click()
sleep(10)
driver.quit()