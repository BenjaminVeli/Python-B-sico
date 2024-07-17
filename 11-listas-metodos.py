lenguajes = ["Python","Ruby","Javascript","Java"]   # La lista comienza de 0 , 1 , 2 , 3
print(lenguajes)

lenguajes.insert(3, "Go")           # Se inserta Go en el tercer elemento
print(lenguajes)

lenguajes.remove("Ruby")            # Elimin a Ruby de la lista
print(lenguajes)

print("PHP" in lenguajes)           # Php se encuentra dentro de la lista de lenguajes ?

print(len(lenguajes))               # Cuantos elementos contiene el listado ?

