from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurações do ChromeDriver para ficar mais humano
chrome_options = Options()
chrome_options.add_argument("--disable-blink-features=AutomationControlled")  # Remove marcações de automação
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Remove flag "automated"
chrome_options.add_experimental_option("useAutomationExtension", False)  # Remove extensão de automação
chrome_options.add_argument("--start-maximized")  # Abre o navegador maximizado
chrome_options.add_argument("--disable-infobars")  # Remove infobars
chrome_options.add_argument("--mute-audio")  # Silencia áudio (útil para vídeos no Instagram)

# Inicializando o ChromeDriver
service = Service("C:/Users/diego/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Previne a detecção por JavaScript
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
        Object.defineProperty(navigator, 'webdriver', {
            get: () => undefined
        });
        window.navigator.chrome = {
            runtime: {},
            loadTimes: () => {},
            offscreenBuffering: false
        };
        window.chrome = { ...window.chrome, ...navigator.chrome };
    """
})

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Configurações para o Chrome
        print("Configurando o Chrome...")
        service = Service("C:/Users/diego/chromedriver-win64/chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--lang=pt-BR")  # Define o idioma para português
        chrome_options.add_argument("--disable-notifications")  # Desativa notificações
        print("Inicializando o WebDriver...")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        user_element = driver.find_element("xpath", "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(1)

        password_element = driver.find_element("xpath", "//input[@name='password']")
        password_element.clear()
        time.sleep(2)
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(10)

        # Chama o método para comentar em uma página específica
        self.comente_na_pagina("https://www.instagram.com/p/DEkvy_4vWNi/")

    @staticmethod
    # métodos para digitação humanizada
    def type_like_a_person(sentence, single_input_field):
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(2, 6) / 30)

    def digitar_como_humano(elemento, texto):
        for char in texto:
            elemento.send_keys(char)
            time.sleep(random.uniform(0.1, 0.4))

    def scroll_suave(self, driver):
    # Realiza scroll até o final de maneira suave
        scroll_height = driver.execute_script("return document.body.scrollHeight")
        for i in range(0, scroll_height, 300):  # Scroll suave em intervalos
            driver.execute_script(f"window.scrollTo(0, {i});")
            time.sleep(random.uniform(1, 3))  # Pausa mais longa e aleatória
        # Rolando para o topo de forma suave
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(2)

    def comente_na_pagina(self, url):
        driver = self.driver
        time.sleep(3)
        driver.get(url)  # Acessa a URL da postagem específica
        time.sleep(3)
        # Scroll até o final da página
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # time.sleep(3)
        # # Voltar ao topo da página
        # driver.execute_script("window.scrollTo(0, 0);")
        # time.sleep(3)
        self.scroll_suave(driver)
        time.sleep(3)
        curtir_campo = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Curtir']"))
            )
        curtir_campo.click()

        try:
            # Aguarda o campo de comentário aparecer no DOM
            comentario_campo = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Adicione um comentário...']"))
            )

            # Clica no campo de comentário
            comentario_campo.click()

            # Recarrega o elemento caso ele fique "stale"
            comentario_campo = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, "//textarea[@aria-label='Adicione um comentário...']"))
            )

            # Envia o comentário de maneira robotica
            # comentario_campo.send_keys("Comentário automático de teste!")
            # comentario_campo.send_keys(Keys.RETURN)

            # Simula a digitação humana para o comentário
            comentario_texto = "excelente saber disso"
            self.type_like_a_person(comentario_texto, comentario_campo)

            print("Comentário feito com sucesso!")
        except Exception as e:
          print(f"Erro ao comentar: {e}")

# Agora instanciamos o bot aqui, fora da classe
bot = InstagramBot("diego@gmail.com", "diego")
bot.login()

