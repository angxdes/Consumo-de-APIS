import requests

print("********   GENERACION DE USUARIOS   **********")

cantidad_usr = int(input("Cuantos usuarios quieres generar?: "))

genero = str(input("Que genero? (male/female): "))

try:
    response = requests.get(f'https://fakerapi.it/api/v1/users?_quantity={cantidad_usr}&_gender={genero}')


    data = response.json()["data"]

    for i in range(len(data)): 
        print(f'//////// USUARIO {i + 1} ///////////')
        for key, value in data[i].items():
            print(f"{key} : {value}")

except Exception as e:
    print(f"Ocurrio el siguiente error: {e}")