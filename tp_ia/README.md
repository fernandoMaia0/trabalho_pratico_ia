# Recomendador de Notebooks por IA  

Este projeto é uma aplicação de Inteligência Artificial que recomenda notebooks ideais para os usuários com base em suas preferências e condições iniciais. Ele utiliza **machine learning** com a biblioteca **scikit-learn** e um banco de dados **SQLite3** importado de uma base de dados pronta disponível no Kaggle.

---

## 🛠️ Funcionalidades  

- **Interação com o Usuário:**  
  O sistema faz perguntas para identificar as necessidades do usuário, como:  
  - Faixa de preço.  
  - Propósito do uso (jogos, trabalho, estudo, etc.).  
  - Portabilidade e outros requisitos importantes.  

- **Treinamento de IA:**  
  Foi treinado com um modelo de machine learning utilizando dados previamente processados.  

- **Recomendações Precisas:**  
  Ao final, o sistema retorna o notebook ideal com base nas respostas do usuário.

---

## 🚀 Tecnologias Utilizadas  

- **Python 3.8+**  
- **scikit-learn:** Para o treinamento e predição do modelo de machine learning.  
- **SQLite3:** Para armazenamento e manipulação do banco de dados.  
- **Base de Dados:** Importada do [Kaggle](https://www.kaggle.com/) com informações sobre notebooks.

---

## 📂 Como Executar  

1. **Clonar o Repositório:**  
   ```bash
   git clone https://github.com/fernandoMaia0/trabalho_pratico_ia.git
   cd trabalho_pratico_ia
   
2. **Instalar Dependências:**
    Certifique-se de que você tenha o Python instalado e, em seguida, instale os pacotes necessários:
    - **pip install -r requirements.txt**

3. **Configurar o Banco de Dados:**
Certifique-se de que o arquivo do banco de dados (notebooks.db) está na pasta principal do projeto. Caso contrário, mova-o ou ajuste as configurações de caminho no código.


## 📊 Estrutura do Projeto
- main.py: Arquivo principal para executar o programa.
- model_training.py: Contém o código de treinamento do modelo de machine learning.
- database_handler.py: Gerencia a conexão e as operações no banco de dados SQLite.
- requirements.txt: Lista de dependências para instalação.
- tp_ia\db.sqlite3

# 📋 Lista de Membros  

Este documento apresenta a equipe de membros associados ao projeto. Cada membro desempenha um papel fundamental no desenvolvimento e sucesso do trabalho.


## 🧑‍💻 Membros da Equipe  

- **Daniel Rodrigues**  
  - E-mail: [daniel.pereira@ufvjm.edu.br](mailto:daniel.pereira@ufvjm.edu.br)

- **Arthur Abreu Patricio de Sousa**  
  - E-mail: [arthur.patricio@ufvjm.edu.br](mailto:arthur.patricio@ufvjm.edu.br)

- **Thais Daniela da Silva Rosa**  
  - E-mail: [thais.daniela@ufvjm.edu.br](mailto:thais.daniela@ufvjm.edu.br)

- **Fernando Maia**  
  - E-mail: [maia.fernando@ufvjm.edu.br](mailto:maia.fernando@ufvjm.edu.br)

- **Osiel Junior Martins Bicalho**  
  - E-mail: [osiel.junior@ufvjm.edu.br](mailto:osiel.junior@ufvjm.edu.br)

- **Raul Rodrigues de Souza Santos**  
  - E-mail: [santos.raul@ufvjm.edu.br](mailto:santos.raul@ufvjm.edu.br)

---

## 📧 Contato  

Caso deseje entrar em contato com algum membro da equipe, utilize os e-mails listados acima. 
