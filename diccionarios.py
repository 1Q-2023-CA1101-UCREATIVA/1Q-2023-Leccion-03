lista_hobbies = [
    "Leo, Motos", 
    "Nacho, Videojuegos", 
    "Allan, Gym", 
    "Cristian, Deporte Contacto", 
    "Carlos, Bici", 
    "Jose, Futbol", 
    "Ithamar, Comer"
]

diccionario = {
    "Leo": "Motos",
    "Nacho": "Videojuegos",
    "Allan": "Gym",
    "Cristian": "Deporte Contacto",
    "Carlos": "Bici",
    "Jose": "Fútbol",
    "Ithamar": "Comer"
}

#print(diccionario["Carlos"])


diccionario["Kevin"] = "Leer"

#print(diccionario)


menu = {
    "Hamburguesa": {
        "Ingredientes": ["Pan", "Tomate", "Carne", "Lechuga"],
        "Precio": 1500
    },
    "Tacos": {
        "Ingredientes": ["Repollo", "Carne", "Salsas"],
        "Precio": 700
    }
}

#print(menu["Hamburguesa"]["Ingredientes"][2])
print(menu.keys())