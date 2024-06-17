import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Obter credenciais dos segredos do GitHub
email = os.getenv('ALIEXPRESS_EMAIL')
password = os.getenv('ALIEXPRESS_PASSWORD')

# Configuração do Selenium WebDriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Login no AliExpress
driver.get("https://login.aliexpress.com")
sleep(3)  # Aguarde a página carregar
email_input = driver.find_element("name", "fm-login-id")
password_input = driver.find_element("name", "fm-login-password")
email_input.send_keys(email)
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
sleep(5)  # Aguarde o login

# Adicionar código para coletar moedas
# Exemplo:
driver.get("https://www.aliexpress.com/p/coin-pc-index")
sleep(3)  # Aguarde a página carregar
coletar_moedas_button = driver.find_element("ELEMENTO_DO_BOTAO_DE_COLETA")
coletar_moedas_button.click()

driver.quit()
