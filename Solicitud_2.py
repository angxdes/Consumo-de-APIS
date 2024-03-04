import requests

print("********   GENERACION DE TEXTOS **********")


cantidad = int(input("Cuantos textos quieres generar?: "))

cantidad_palabras = int(input("De cuantos caracteres?: "))

try:
    response = requests.get(f'https://fakerapi.it/api/v1/texts?_quantity={cantidad}&_characters={cantidad_palabras}')

    data = response.json()["data"]

    for i in range(len(data)):
        print(f'//////// TEXTO {i + 1} ///////////')
        for key, value in data[i].items():
            
            print(f"{key} : {value}")

except Exception as e:
    print(f'Ocurrio el siguiente error:{e}')
