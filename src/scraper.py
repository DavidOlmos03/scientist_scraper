from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

def search_scientist(scientist_name):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Para ejecutar en segundo plano
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(scientist_name + " científico área biografía")
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)  # Esperar carga de resultados

    soup = BeautifulSoup(driver.page_source, "html.parser")
    
    # Extraer el área y la biografía
    area = None
    bio = None
    for snippet in soup.select(".VwiC3b"):
        text = snippet.get_text()
        if "físico" in text or "matemático" in text or "biólogo" in text:
            area = text
        if "nació" in text or "científico" in text:
            bio = text
        if area and bio:
            break

    driver.quit()
    return {"name": scientist_name, "area": area, "bio": bio}

