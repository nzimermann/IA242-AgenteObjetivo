# IA Orientada a objetivo

Um agente projetado para simular um aspirador de pó inteligente, seu objetivo é limpar completamente a matriz, aspirando todos os quadrados cinzas da forma mais eficiente possível. A eficiência é medida pelo número total de ações realizadas durante o processo de limpeza, um número menor indica um agente mais eficiente.

![IA242-ObjectiveOrientedAgentWorking](https://github.com/user-attachments/assets/426fb92a-7a4c-4f79-bb35-f94fa9e0ce3a)

## Rodando o projeto

É possível rodar o código utilizando uma plataforma web como [Jupyter Notebook](https://jupyter.org/) ou [Google Colab](https://colab.google/)

Caso queira rodar o código em sua própria máquina certifique-se antes de ter [python3](https://www.python.org/downloads/) e [git](https://git-scm.com/downloads) instalados.

1. Abra o terminal e faça o download do projeto com o comando:
```bash
git clone https://github.com/nzimermann/IA242-AgenteObjetivo.git
```

2. Vá para dentro da pasta do projeto.
```bash
cd IA242-AgenteObjetivo
```

3. Para isolar as dependências do projeto das da máquina é necessário criar antes um ambiente virtual para o python, para isso utilize o [módulo venv](https://docs.python.org/3/library/venv.html#creating-virtual-environments) do python.

```bash
python -m venv .venv
```

4. Ative o ambiente virtual.

Windows
```bash
.venv\Scripts\activate
```

Linux
```bash
source .venv/bin/activate
```

5. Instale as dependências do projeto utilizando o comando abaixo:

```bash
python -m pip install -r requirements.txt
```

Pronto! É possível fazer a execução do código normalmente utilizando `python main.py`.
