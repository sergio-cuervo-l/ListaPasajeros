
class Pasajero:
    #Se define constructor de la clase pasajero con sus atributos
    def __init__(self, nombre, edad, clase_puesto, responsable=None):
        self.nombre = nombre
        self.edad = edad
        self.clase_puesto = clase_puesto
        self.responsable = responsable
    
    #Se define el output de los pasajeros 
    def __repr__(self):
        return f"Pasajero({self.nombre}, {self.edad}, {self.clase_puesto}, {self.responsable})"

def crear_cola(lista_pasajeros):
    cola_business = []
    cola_economica = []

    #Se separa los pasajeros por la clase de puesto que compraron
    for pasajero in lista_pasajeros:
        if pasajero.clase_puesto == "Business":
            cola_business.append(pasajero)            
        else:
            cola_economica.append(pasajero)
            
    #Se define las llaves de ordenamiento para los pasajeros
    def key(pasajero):
        return (-pasajero.edad >= 65, -pasajero.edad)  

    #Se ordenan los pasajeros para segun las llaves definidas
    cola_business.sort(key=key)
    cola_economica.sort(key=key)

    #Se obtiene una lista completa de todos los pasajeros que son responsables de otro pasajero
    responsables = {pasajero.responsable for pasajero in lista_pasajeros if pasajero.responsable}
    
    #Se hace un join de los pasajeros separados por clase
    cola_final = cola_business + cola_economica

    #Se hace ciclo para buscar a los pasajeros responsables y poner detras a las personas a cargo
    for i, pasajero in enumerate(cola_final):
        if pasajero.responsable in responsables:
            #Se obtiene la información del usuario que va estar a cargo por un pasajero
            dato = cola_final.pop(i)
            for j in range(0, len(cola_final)):
                if cola_final[j].nombre == pasajero.responsable:
                    #Se inserta pasajero a cargo debajo del usuario responsable
                    cola_final.insert(j+1, dato)
  
    return cola_final
    

pasajero1 = Pasajero("Juan Perez", 35, "Business")
pasajero2 = Pasajero("Maria Lopez", 15, "Economica", "Sofia Martinez")
pasajero3 = Pasajero("Pedro Gomez", 28, "Business")
pasajero4 = Pasajero("Luis Cuervo", 70, "Business")
pasajero5 = Pasajero("Lucia Leon", 15, "Business", "Juan Perez")
pasajero6 = Pasajero("Sergio Cuervo", 26, "Business")
pasajero7 = Pasajero("Ana Garcia", 48, "Economica")
pasajero8 = Pasajero("Maria Guarda", 22, "Economica")
pasajero9 = Pasajero("Carlos Rodriguez", 45, "Business")
pasajero10 = Pasajero("Sofia Martinez", 28, "Economica")
pasajero11 = Pasajero("David Hernandez", 10, "Business", "Ana Garcia")

lista_pasajeros = [pasajero1, pasajero2, pasajero3, pasajero4, pasajero5, pasajero6, pasajero7, pasajero8, pasajero9, pasajero10, pasajero11]

cola_final = crear_cola(lista_pasajeros)

print(cola_final)