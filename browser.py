#initializam driverul pe care il vom folosi
from selenium import webdriver

class Browser:
    driver = webdriver.Chrome() #webdriver tip Chrome
    driver.maximize_window() #maximizez fereastra
    driver.implicitly_wait(5)
    driver.set_page_load_timeout(10) #asteapta timp de 10 secunde pana cand se incarca pagina

#metoda/functie pentru a inchide browserul - de obicei la tearDown
    def close(self):
        self.driver.quit()