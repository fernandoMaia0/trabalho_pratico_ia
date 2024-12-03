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
        # Carregar os dados enviados pelo frontend usando request.POST
        age = request.POST.get('age')
        main_use = request.POST.get('mainUse')
        linux_familiarity = request.POST.get('linuxFamiliarity')
        budget = request.POST.get('budget')
        portability_vs_performance = request.POST.get('portabilityVsPerformance')
        battery_life = request.POST.get('batteryLife')
        brand_preference = request.POST.get('brandPreference')
        screen_size = request.POST.get('screenSize')
        graphics_card = request.POST.get('graphicsCard')
        memory_need = request.POST.get('memoryNeed')

        # Preparar os dados para o modelo
        features = [
            age,
            main_use,
            linux_familiarity,
            budget,
            portability_vs_performance,
            battery_life,
            brand_preference,
            screen_size,
            graphics_card,
            memory_need
        ]

        # Pré-processar os dados, se necessário (exemplo: codificação de categorias)
        features = preprocess_features(features)

        # Usar o modelo para fazer a recomendação
        recommendation = model.predict([features])
        recommendation_label = label_encoder_product.inverse_transform(recommendation)
        
        context = {
            'recommendation': recommendation_label[0],
            'features': features,
        }

        # Retornar a recomendação ao frontend
        return render(request,'resposta.html',context)


def preprocess_features(features):
    # Exemplo de pré-processamento (ajuste conforme necessário)
    # Se houver valores categóricos, você pode precisar usar o label_encoder para transformá-los
    features[4] = label_encoder_gpu.transform([features[4]])  # Exemplo de codificação para 'portabilityVsPerformance'
    # Adicione mais transformações conforme necessário para outras variáveis categóricas
    return features

def index(request):
    return render(request, 'index.html')