# visualizadorEstagiosPUCRS
Visualiza e me dita de forma automatizada as vagas presentes para minha área no PUCRS Carreiras.

Visualizador usando Selenium.



- Navegue até um local onde deseja utilizar o programa

- Clone este repositório:

```
git clone https://github.com/brisolarag/visualizadorEstagiosPUCRS.git
```

- Inicie uma virtualização dos arquivos e instale as dependências:
```
virtualenv venv
source /home/$User/.../estagio-visualizer/visualizadorEstagiosPUCRS/venv/bin/activate
pip install -r requirements.txt
```

Agora é importante que você verifique se está utilizando a virtualização no terminal, normalmente por (venv) ou o nome dado ao env.

- Altere nos arquivos do projeto, em main.py linha 7 (recomendo olhar no próprio site para verificar qual o ID do curso na seleção)
```python
nome_do_curso = "nome_do_curso" 
```

Depois de relizar tais alterções, você pode rodar o programa com:
```
python3 main.py
```



