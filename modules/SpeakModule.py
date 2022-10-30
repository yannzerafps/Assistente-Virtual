import Marvin
import requests
import json

def buscar_dados(command_action):

    if command_action == "temperatura":
        request = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=26.48&lon=49.06&appid=af61412878cb4ea30ea24238578e5637&units=metric")

        data = json.loads(request.content)
        temp = data['main']['temp']
        Marvin.speak('A temperatura no momento é de '+ str(temp) + 'graus')
    if command_action == "dólar":
        
        request = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
        data = json.loads(request.content)
        cotacao = data['USDBRL']['bid']
        Marvin.speak('A cotação do Dólar esta em  '+ str(cotacao))