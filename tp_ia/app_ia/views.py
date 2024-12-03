from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
import joblib

# Carregar os modelos
model = joblib.load('decision_tree_model.pkl')
label_encoder_gpu = joblib.load('label_encoder_gpu.pkl')
label_encoder_product = joblib.load('label_encoder_product.pkl')

@csrf_exempt  # Para permitir requisições POST sem token CSRF (apenas para testes)
def recommend(request):
    if request.method == 'POST':
        # Carregar os dados enviados pelo frontend
        data = json.loads(request.body)

        # Extrair as respostas do usuário e preparar os dados para o modelo
        features = [
            data.get('age'),
            data.get('mainUse'),
            data.get('linuxFamiliarity'),
            data.get('budget'),
            data.get('portabilityVsPerformance'),
            data.get('batteryLife'),
            data.get('brandPreference'),
            data.get('screenSize'),
            data.get('graphicsCard'),
            data.get('memoryNeed')
        ]
        
        # Pré-processar os dados, se necessário (exemplo: codificação de categorias)
        features = preprocess_features(features)

        # Usar o modelo para fazer a recomendação
        recommendation = model.predict([features])
        recommendation_label = label_encoder_product.inverse_transform(recommendation)

        # Retornar a recomendação ao frontend
        return JsonResponse({'recommendation': recommendation_label[0]})

def preprocess_features(features):
    # Exemplo de pré-processamento (ajuste conforme necessário)
    # Se houver valores categóricos, você pode precisar usar o label_encoder para transformá-los
    features[4] = label_encoder_gpu.transform([features[4]])  # Exemplo de codificação para 'portabilityVsPerformance'
    # Adicione mais transformações conforme necessário para outras variáveis categóricas
    return features

def index(request):
    return render(request, 'index.html')