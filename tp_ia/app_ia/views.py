from django.shortcuts import render
from django.http import JsonResponse
import pandas as pd
import joblib
import sqlite3

# Caminho para o modelo treinado
MODEL_PATH = r"C:\Users\Osiel Junior\trabalho_pratico_ia\tp_ia\app_ia\trained_model.pkl"
# Caminho do banco de dados SQLite
DB_PATH = r"C:\Users\Osiel Junior\trabalho_pratico_ia\tp_ia\db.sqlite3"
TABLE_NAME = "app_ia_laptop"  # Ajuste conforme o nome da tabela no SQLite

# Carregar o modelo treinado
clf = joblib.load(MODEL_PATH)

def recommend(request):
    if request.method == "POST":
        try:
            # **1. Obter Dados do Usuário**
            user_input = {
                "price_euros": float(request.POST.get("price_euros")),
                "ram": int(request.POST.get("ram",)),
                "inches": float(request.POST.get("inches")),
                "weight": float(request.POST.get("weight",)),
                "screen_width": int(request.POST.get("screen_width")),
                "screen_height": int(request.POST.get("screen_height",))
            }

            # **2. Converter os Dados do Usuário em DataFrame**
            user_input_df = pd.DataFrame([user_input])

            # **3. Fazer a Predição**
            recommended_laptop_id = clf.predict(user_input_df)[0]
            print(f"ID previsto pelo modelo: {recommended_laptop_id}")

            # **4. Buscar Informações Detalhadas do Banco**
            conn = sqlite3.connect(DB_PATH)
            query = f"SELECT * FROM {TABLE_NAME} WHERE id = ?"
            recommended_laptop = pd.read_sql_query(query, conn, params=(int(recommended_laptop_id),))
            conn.close()

            if not recommended_laptop.empty:
                response = recommended_laptop.iloc[0].to_dict()
                return render(request, 'resultados.html', {
                    'features': user_input,
                    'recommendation': response
                })
            else:
                return render(request, 'resultados.html', {
                    'features': user_input,
                    'recommendation': "Nenhum notebook encontrado."
                })

        except Exception as e:
            return render(request, 'resultados.html', {
                'features': {},
                'recommendation': f"Erro ao fazer a recomendação: {str(e)}"
            })

    return render(request, 'resultados.html', {
        'features': {},
        'recommendation': "Método não permitido."
    })


def index(request):
    return render(request, 'index.html')
