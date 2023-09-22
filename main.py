from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import write_file

# chrome_driver_path = "./chromedriver"
url = "https://carreiras.pucrs.br/Oportunidades"

navegador = webdriver.Chrome()
navegador.get(url)

# Espera pagina carregar
sleep(15)

# ======= SELECIONANDO CURSO E ENVIANDO

# Seleciona curso engenharia mecânica
curso_select = Select(navegador.find_element(By.ID, "CursoNome"))
curso_select.select_by_value("engenharia-de-software") #seleciona curso

sleep(1) # checa se o curso nao esta escolhido
if curso_select.first_selected_option.get_attribute("value") != "engenharia-de-software":
    curso_select.select_by_value("engenharia-de-software")

# envia
botao_enviar = navegador.find_element(By.CLASS_NAME, "vagas-enviar")
botao_enviar.click()


# espera pagina carregar
sleep(10)

# ======== PEGANDO AS VAGAS

a_elements = navegador.find_elements(By.XPATH, "//*[@id='lista']/a")
h3_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item h3")
p_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item p")




_vagas = [h3.text for h3 in h3_elements]
_descricao = [p.text for p in p_elements]
_hrefs = [a.get_attribute('href') for a in a_elements]
vagas = []

for i, vaga in enumerate(_vagas):
    dict = {'indice': i, 'vaga': vaga, 'descricao': _descricao[i], 'link': _hrefs[i] }
    vagas.append(dict)

print(f'Foram encontradas {len(_vagas)} vagas.')

for vaga in vagas:
    write_file.escrever_arquivo(vaga)
    # print(f'Vaga {i + 1} de {len(_vagas)}:')
    # print(f'Vaga: {vaga["vaga"]}')
    # print(f'Descricao: {vaga["descricao"]}')
    # print(f'Link: {vaga["link"]}')
    # print("")
    


navegador.quit()
