import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib
import os
import django
from app_ia.models import Laptop

# Definir corretamente o módulo de configurações
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tp_ia.settings")

# Inicializar o Django
django.setup()

# 3. Extrair os dados relevantes para treinamento usando Django ORM
laptops = Laptop.objects.filter(
    price_euros__isnull=False,
    ram__isnull=False,
    inches__isnull=False,
    cpu_freq__isnull=False,
    primary_storage__isnull=False,
    gpu_company__isnull=False,
    product__isnull=False
).values(
    'price_euros', 'ram', 'inches', 'cpu_freq', 'primary_storage', 'gpu_company', 'product'
)

# Converter os dados para um DataFrame do Pandas
dataset = pd.DataFrame(laptops)

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
