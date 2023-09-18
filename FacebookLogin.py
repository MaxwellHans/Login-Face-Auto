#Importando bibliotecas necessárias
from getpass import getpass



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
#Biblioteca necessária para dar o tempo necessário para abertura da página
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()
#Necessário para rodar o drive no FireFox

driver.get('https://www.facebook.com')
time.sleep(5)
#Item a cima abre a pagina do facebook, deley de 5 segundos pra digitar automaticament
username = driver.find_element(
        By.ID,
        "email"
        )

password = driver.find_element(
    By.ID,
    "pass"
    )
#Busca no codigo HTML da página as referencias dos ids de login e senhas 
print('Login processing...')

username.send_keys('maxwell220686@hotmail.com')
#Envia o endereço de e-mail 
time.sleep(3)
#Da o tempo de 3 segundos para a pagina do facebook abrir
password.send_keys('Cp8!x6wsma')
#envia a senha necessária para acesso
login = driver.find_element(
    By.ID,
    "u_0_5_CR"
     )
login.click()
#Clica no botão de entrar na pagina após digitar login e senha, id variável, buscando solução de busca para finalizar automação