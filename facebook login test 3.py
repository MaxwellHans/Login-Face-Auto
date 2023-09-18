from selenium import webdriver
from selenium.webdriver.common.by import By
from Anaconda import time
print('Start Login.')  

driver = webdriver.Firefox()
driver.get('https://www.facebook.com')  
    
username = webdriver.find_element(By.ID,"email")
password = webdriver.find_element(By.ID,"pass")
 
   
print('https://www.facebook.com')
    
#username.send_keys('maxwell220686@hotmail.com')
    
#time.sleep(3)
    
#password.send_keys()
    
#login = webdriver.find_element(By.ID,"u_0_5_wb")