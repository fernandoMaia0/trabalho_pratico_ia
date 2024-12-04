import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics import accuracy_score

# Caminho do banco de dados
db_path = r"trabalho_pratico_ia\tp_ia\db.sqlite3"

conn = sqlite3.connect(db_path)


table_name = "app_ia_laptop"  


laptops = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

# Fechar a conexão
conn.close()

# **2. Pré-processamento dos Dados**
# Converter valores categóricos em valores numéricos
label_encoders = {}

# Colunas categóricas a serem transformadas
categorical_columns = ['company', 'os', 'gpu_company']

for col in categorical_columns:
    le = preprocessing.LabelEncoder()
    laptops[col] = le.fit_transform(laptops[col])
    label_encoders[col] = le


features = ['price_euros', 'ram', 'inches', 'weight', 'screen_width', 'screen_height']
target = 'id'  # Coluna que queremos prever

X = laptops[features]
y = laptops[target]

# **4. Divisão dos Dados em Treino e Teste**
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# **5. Treinamento do Modelo**
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# **6. Avaliação do Modelo**
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Acurácia do modelo: {accuracy:.2f}")

# **7. Fazer uma Recomendação com Base em Novos Dados**
# Simulação de entrada do usuário
user_input = {
    "price_euros": 800,
    "ram": 16,
    "inches": 15.6,
    "weight": 2.5,
    "screen_width": 1920,
    "screen_height": 1080
}

# Converter os dados de entrada em um DataFrame
user_input_df = pd.DataFrame([user_input])

# Fazer a predição
recommended_laptop_id = clf.predict(user_input_df)
print(f"ID do notebook recomendado: {recommended_laptop_id[0]}")

# **8. Opcional: Mapear o ID para Dados Detalhados do Notebook**
# Para encontrar o notebook correspondente ao ID previsto
recommended_laptop = laptops[laptops['id'] == recommended_laptop_id[0]]
print("Notebook recomendado:")
print(recommended_laptop)
