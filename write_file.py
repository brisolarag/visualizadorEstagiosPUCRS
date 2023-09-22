from datetime import datetime
import os
hoje = datetime.now().strftime('%d_%m_%Y')

def escrever_arquivo(dict):
    try:    
        file_name = f'{str(dict["indice"]).zfill(3)}.{dict["vaga"]}.txt'
        file_location = os.path.join('vagas/', file_name)


        f = open(file_location, 'x')
        
        linha0 = (f"Vaga {dict['indice']}:")
        linha1 = (f"Vaga: {dict['vaga']}")
        linha2 = (f"Descricao: {dict['descricao']}")
        linha3 = (f"Link: {dict['link']}")

        f.write(f"{linha0}\n{linha1}\n{linha2}\n{linha3}\n")
    except FileExistsError as fe:
        print(f'Ocorreu um erro: <{file_name}> já existe.')


if __name__ == "__main__":
    print("not in main")
    dict_teste = {'indice': 2, 'vaga': 'ESTÁGIO - APRIX - FULL STACK DEVELOPER', 'descricao': 'A Aprix é uma startup que desenvolve soluções de ciência de dados, principalmente voltadas para precificação. Somos focados no desenvolvimento de soluções de pricing baseadas em Inteligência Artificial, com case de repercussão nacional no setor de combustíveis. Nossa solução de precificação dinâmica e otimização de preços para postos de combustíveis é pioneira no mercado nacional e está em utilização no país inteiro. Mas é só o começo. Vamos alterar a forma como preços são formulados e executados em diferentes segmentos da indústria e varejo nos próximos anos. Nossa missão é construir soluções de Data Science que auxiliem agentes de diferentes portes e setores a alcançar ganhos de eficiência.', 'link': 'https://carreiras.pucrs.br/Oportunidades/estagio/26401/estagio---aprix---full-stack-developer'}
    escrever_arquivo(dict_teste)
    

def substituir_barras(string):
    return string.replace('/', '_')