from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import write_file

nome_do_curso = "engenharia-de-software" #altere aqui

################################ NAVEGANDO ATÉ A PÁGINA #################################
url = "https://carreiras.pucrs.br/Oportunidades"

navegador = webdriver.Chrome()
navegador.get(url)

# Espera pagina carregar
sleep(10)


################################ SELECIONANDO CURSO E ENVIANDO #################################
# Seleciona curso engenharia mecânica
curso_select = Select(navegador.find_element(By.ID, "CursoNome"))
curso_select.select_by_value(nome_do_curso) #seleciona curso

# sleep(1)

# Checa se o curso esta realmente escolhido
# if curso_select.first_selected_option.get_attribute("value") != "engenharia-de-software":
#     curso_select.select_by_value("engenharia-de-software")

# Scrolla para botao ficar clicavel e depois envia
navegador.execute_script("window.scrollBy(0, 80);")
botao_enviar = navegador.find_element(By.CLASS_NAME, "vagas-enviar")
botao_enviar.click()


# Espera próxima pagina carregar
sleep(5)


################################ ITERANDO SOBRE AS VAGAS #################################
h3_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item h3") #   titulo das vagas            / elemento h3
p_elements = navegador.find_elements(By.CSS_SELECTOR, ".oportunidade-item p") #     descricao das vagas         / elemento p
a_elements = navegador.find_elements(By.XPATH, "//*[@id='lista']/a") #              link das vagas              / elemento a




_vagas = [h3.text for h3 in h3_elements] #                  pega todas as vagas
_descricao = [p.text for p in p_elements] #                 pega todas as descricoes
_hrefs = [a.get_attribute('href') for a in a_elements] #    pega todos links


vagas = []

################################ ATRIBUINDO AS VAGAS AO ARRAY #################################
for i, vaga in enumerate(_vagas):
    dict = {'indice': i, 'vaga': write_file.substituir_barras(vaga), 'descricao': _descricao[i], 'link': _hrefs[i] }
    vagas.append(dict)

print(f'Foram encontradas {len(_vagas)} vagas.')


################################ ESCREVENDO OS TXT DAS VAGAS #################################
for vaga in vagas:
    write_file.escrever_arquivo(vaga)
    


navegador.quit()
