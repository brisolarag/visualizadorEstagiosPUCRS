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
wait = WebDriverWait(navegador, 20)
wait.until(EC.presence_of_element_located((By.ID, "CursoNome")))

curso_select = Select(navegador.find_element(By.ID, "CursoNome"))

curso_select.select_by_value("engenharia-de-software") #seleciona curso


if curso_select.first_selected_option.get_attribute("value") != "engenharia-de-software":
    curso_select.select_by_value("engenharia-de-software")

wait2 = WebDriverWait(navegador, 10)
wait2.until(EC.presence_of_element_located((By.CLASS_NAME, "vagas-enviar")))

botao_enviar = navegador.find_element(By.CLASS_NAME, "vagas-enviar")
botao_enviar.click()

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
