import sqlite3
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Caminho do banco de dados
db_path = r"C:\Users\danie\trabalho_pratico_ia\tp_ia\db.sqlite3"

# Conectar ao banco de dados SQLite
conn = sqlite3.connect(db_path)

# Criar um cursor para executar consultas
cursor = conn.cursor()

# Consulta SQL para pegar os dados relevantes da tabela Laptop
query = """
    SELECT price_euros, ram, inches, cpu_freq, primary_storage, gpu_company, product
    FROM app_ia_laptop
    WHERE price_euros IS NOT NULL AND ram IS NOT NULL AND inches IS NOT NULL
    AND cpu_freq IS NOT NULL AND primary_storage IS NOT NULL AND gpu_company IS NOT NULL
    AND product IS NOT NULL;
"""
cursor.execute(query)

# Recuperar todos os dados e armazená-los em uma variável
rows = cursor.fetchall()

# Verificar se encontrou dados e carregar para um DataFrame
if rows:
    # Criar o DataFrame com os dados
    dataset = pd.DataFrame(rows, columns=['price_euros', 'ram', 'inches', 'cpu_freq', 'primary_storage', 'gpu_company', 'product'])

    # 4. Preparar os dados
    dataset = dataset.dropna()

    # Usar LabelEncoder para transformar as variáveis categóricas em numéricas
    label_encoder_gpu = LabelEncoder()
    label_encoder_product = LabelEncoder()

    dataset["gpu_company_encoded"] = label_encoder_gpu.fit_transform(dataset["gpu_company"])
    dataset["product_encoded"] = label_encoder_product.fit_transform(dataset["product"])

    # Definir as features e o target
    X = dataset[["price_euros", "ram", "inches", "cpu_freq", "primary_storage", "gpu_company_encoded"]]
    y = dataset["product_encoded"]

    # Dividir os dados em conjuntos de treino e teste
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Treinar a árvore de decisão
    tree_model = DecisionTreeClassifier(random_state=42)
    tree_model.fit(X_train, y_train)

    # Avaliar a acurácia
    accuracy = tree_model.score(X_test, y_test)
    print(f"Acurácia do modelo: {accuracy * 100:.2f}%")

    # 6. Salvar o modelo e os codificadores para reutilização
    joblib.dump(tree_model, r"C:\Users\danie\trabalho_pratico_ia\tp_ia\decision_tree_model.pkl")
    joblib.dump(label_encoder_gpu, r"C:\Users\danie\trabalho_pratico_ia\tp_ia\label_encoder_gpu.pkl")
    joblib.dump(label_encoder_product, r"C:\Users\danie\trabalho_pratico_ia\tp_ia\label_encoder_product.pkl")
else:
    print("Nenhum dado encontrado.")

# Fechar a conexão
conn.close()
