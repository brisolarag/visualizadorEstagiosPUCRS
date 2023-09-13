from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chrome_driver_path = "./chromedriver"
url = "https://carreiras.pucrs.br/Oportunidades"

navegador = webdriver.Chrome()

navegador.get(url)

# Espera pagina carregar
wait = WebDriverWait(navegador, 10)
wait.until(EC.presence_of_element_located((By.ID, "CursoNome")))

curso_select = Select(navegador.find_element(By.ID, "CursoNome"))

curso_select.select_by_value("engenharia-de-software") #seleciona curso

botao_enviar = navegador.find_element(By.CLASS_NAME, "vagas-enviar")

if curso_select.first_selected_option.get_attribute("value") != "engenharia-de-software":
    curso_select.select_by_value("engenharia-de-software")

botao_enviar.click() #envia

# Espera pagina carregar
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oportunidade-item h3")))
wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".oportunidade-item p")))

h3_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item h3")
p_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item p")

# Espera pagina carregar

vagas = [h3.text for h3 in h3_elements]

for vaga in vagas:
    print(vaga)

navegador.quit()
