import requests

print("********   GENERACION DE TARJETAS6 **********")


num_tarjetas = int(input('Cuantas tarjetas quieres generar?:'))

try:
    response = requests.get(f'https://fakerapi.it/api/v1/credit_cards?_quantity={num_tarjetas}')

    data = response.json()["data"]

    for i in range(len(data)):
        print(f'//////// TARJETA {i + 1} ///////////')
        for key, value in data[i].items():
            
            print(f"{key} : {value}")

except Exception as e:
    print(f'Ocurrio el siguiente error:{e}')
