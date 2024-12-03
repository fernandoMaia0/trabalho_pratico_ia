import requests
import json

# Dados de exemplo
data = {
    "age": 25,
    "mainUse": "Trabalho",
    "linuxFamiliarity": "Sim",
    "budget": "Médio",
    "portabilityVsPerformance": "Portátil",
    "batteryLife": "Alta",
    "brandPreference": "Dell",
    "screenSize": "15",
    "graphicsCard": "NVIDIA",
    "memoryNeed": "8GB"
}

# URL do endpoint
url = 'http://localhost:8000/recommend/'

# Enviar a requisição POST
response = requests.post(url, json=data)

# Exibir a resposta
print(response.json())
