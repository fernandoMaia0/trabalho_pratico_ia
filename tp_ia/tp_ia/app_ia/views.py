from django.shortcuts import render
import json
import joblib
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Carregar o modelo e os encoders
tree_model = joblib.load("decision_tree_model.pkl")
label_encoder_gpu = joblib.load("label_encoder_gpu.pkl")
label_encoder_product = joblib.load("label_encoder_product.pkl")

# Exibição da página inicial
def index(request):
    return render(request, 'index.html')

@csrf_exempt
def recommend_notebook(request):
    if request.method == "POST":
        try:
            # Carregar os dados enviados
            data = json.loads(request.body)

            # Log para verificar os dados recebidos
            print(f"Dados recebidos: {data}")

            # Mapear as respostas para os inputs do modelo
            user_input = [
                float(data.get("budget", 1000)),              # Orçamento
                int(data.get("memoryNeed", 8)),               # Memória RAM
                float(data.get("screenSize", 15.6)),          # Tamanho da tela
                float(data.get("cpuFreq", 2.5)),              # Frequência da CPU
                int(data.get("primaryStorage", 512)),         # Armazenamento
                label_encoder_gpu.transform([data.get("gpuCompany", "Intel")])[0]  # GPU codificada
            ]

            # Log para verificar a entrada do modelo
            print(f"Entrada para o modelo: {user_input}")

            # Fazer a predição
            prediction_encoded = tree_model.predict([user_input])[0]
            prediction = label_encoder_product.inverse_transform([prediction_encoded])[0]

            # Retornar a recomendação
            return JsonResponse({"recommendation": prediction})

        except Exception as e:
            # Log de erro
            print(f"Erro: {str(e)}")
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Invalid method"}, status=405)
