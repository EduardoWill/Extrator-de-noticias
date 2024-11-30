from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


#a_noticia = input("Qual notícia deseja olhar?: ")

class noticia:
    def __init__(self):
        service = Service('C:/Users/eduar/Desktop/Extração notícia/chromedriver.exe')
        options = Options()
        self.webdriver = webdriver.Chrome(service = service, options = options)
        

    def pesquisa(self, busca):
        self.webdriver.get('https://www.cnnbrasil.com.br/politica/')
        div_action = self.webdriver.find_element(By.XPATH, "//div[@class='header__actions']")
        action = div_action.find_element(By.XPATH, ".//input[@type='text']")
        action.send_keys(busca + Keys.RETURN)
    def noticias(self):
        botoes = self.webdriver.find_elements(By.XPATH, "//a[contains(@class,'home__list__tag')]")
        reportagens = []
        
        
        for botao in botoes[:5]:
            botao_link = botao.get_attribute("href")
            self.webdriver.get(botao_link)
            time.sleep(5)
            titulo_element = self.webdriver.find_element(By.XPATH,"//h1[@class='single-header__title']")
            #pega o texto que está dentro da tag <a> a , é importante
            autor_element = self.webdriver.find_element(By.XPATH, "//span[contains(@class, 'author__group')]//a")
            data_element = self.webdriver.find_element(By.XPATH, "//time[@class='single-header__time']") 
            
            autor = autor_element.text
            titulo = titulo_element.text
            data = data_element.text

            reportagens.append(titulo)
            reportagens.append(autor)
            print(f'{titulo}\n Autor(a) {autor} \n {data}\n')
            self.webdriver.back()
            time.sleep(2)
        
            
            

            



noticia_obj = noticia()
noticia_obj.pesquisa("bolsonaro")
noticia_obj.noticias()
input("Enter")

