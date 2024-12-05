import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import joblib  # Para salvar o modelo treinado
import os

# Caminho do banco de dados SQLite
DB_PATH = r"C:\Users\danie\OneDrive\Área de Trabalho\trabalho_pratico_ia\tp_ia\tp_ia\tp_ia\db.sqlite3"
TABLE_NAME = "app_ia_laptop"  # Nome da tabela no banco de dados

if os.path.exists(DB_PATH):
    print("Banco de dados encontrado!")
else:
    print("Banco de dados NÃO encontrado!")

# **1. Carregar Dados do Banco**
conn = sqlite3.connect(DB_PATH) 
laptops = pd.read_sql_query(f"SELECT * FROM {TABLE_NAME}", conn)
conn.close()

# Preencher valores nulos
laptops.fillna({
    'price_euros': 0,
    'ram': 0,
    'inches': 0,
    'weight': 0,
    'screen_width': 0,
    'screen_height': 0,
    'company': 'Unknown',
    'os': 'Unknown',
    'gpu_company': 'Unknown'
}, inplace=True)

# **2. Pré-processamento dos Dados**
label_encoders = {}
categorical_columns = ['company', 'os', 'gpu_company']

#processamento de categorias de colunas 
#é da biblioteca 
#o processamento é feito antes 
for col in categorical_columns:
    le = preprocessing.LabelEncoder()
    laptops[col] = le.fit_transform(laptops[col])
    label_encoders[col] = le

# Definir features e target
features = ['price_euros', 'ram', 'inches', 'weight', 'screen_width', 'screen_height']
target = 'id' # o objetivo 

X = laptops[features] # onde é colocado as features
y = laptops[target] # recbe o id do produto 

# **3. Divisão dos Dados e Treinamento**
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# **4. Salvar o Modelo Treinado**
joblib.dump(clf, "trained_model.pkl")  # Salva o modelo
print("Modelo treinado e salvo como 'trained_model.pkl'")
