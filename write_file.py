from datetime import datetime
hoje = datetime.now().strftime('%d_%m_%Y')

def escrever_arquivo(arr):
    _i = 1
    try:
        f = open(f'vagas - {_i}.txt')
        for vaga in arr:
            linha0 = (f'Vaga {_i}:')
            linha1 = (f'Vaga: {vaga["vaga"]}')
            linha2 = (f'Descricao: {vaga["descricao"]}')
            linha3 = (f'Link: {vaga["link"]}')

            f.write(f"{linha0}\n{linha1}\n{linha2}\n{linha3}\n")

    except Exception as e:
        while(e):
            _i += 1
        
        f = open(f'vagas - {_i}.txt')
        for vaga in arr:
            linha0 = (f'Vaga {_i}:')
            linha1 = (f'Vaga: {vaga["vaga"]}')
            linha2 = (f'Descricao: {vaga["descricao"]}')
            linha3 = (f'Link: {vaga["link"]}')

            f.write(f"{linha0}\n{linha1}\n{linha2}\n{linha3}\n")



if __name__ == "__main__":
    print("not in main")
    