from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        # Configurações para o Chrome
        print("Configurando o Chrome...")
        service = Service("C:/chromedriver-win64/chromedriver.exe")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--lang=pt-BR")  # Define o idioma para português
        chrome_options.add_argument("--disable-notifications")  # Desativa notificações
        print("Inicializando o WebDriver...")
        self.driver = webdriver.Chrome(service=service, options=chrome_options)


    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        # login_button = driver.find_element("xpath", "//a[@href='/accounts/login/?source=auth_switcher']")
        # login_button.click()
        # time.sleep(3)

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
        time.sleep(6)

        # self.comente_nas_fotos_com_a_hashtag("calisteniabrasil")  # Altere para sua hashtag
        # Chame o método para comentar em uma página específica
        self.comente_na_pagina("https://www.instagram.com/guarulhoshoje/reel/DD0KJP_J1IN/")

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ Simula a digitação como uma pessoa """
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def comente_na_pagina(self, url):
        driver = self.driver
        driver.get(url)  # Acessa a URL da postagem específica
        time.sleep(3)
        # Scroll até o final da página
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)
        # Voltar ao topo da página
        driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(3)

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

            # Envia o comentário
            comentario_campo.send_keys("Comentário automático de teste!")
            comentario_campo.send_keys(Keys.RETURN)

            print("Comentário feito com sucesso!")
        except Exception as e:
          print(f"Erro ao comentar: {e}")

# Agora instanciamos o bot aqui, fora da classe
bot = InstagramBot("diego.kr1994@gmail.com", "Cleiton_0708")
bot.login()

