# pip install request 
import requests
import json

url = "https://juliencansell.pythonanywhere.com/api/GetPizzas" # Notre URL api
data =  requests.get(url)       # Capter notre URL dans une VAR

#print(data.text)                # Formater data avec .text

pizzas = json.loads(data.text)       # Deserialiser je JSON
#print(len(pizzas))

print("Liste des pizzas ")

for pizzaModel in pizzas :
    pizza = pizzaModel['fields']
    print(pizza['nom'] + " " + str(pizza['prix']) + "€")


