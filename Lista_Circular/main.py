#Creación de objeto receta
from receta import receta
from lista_circular import lista_circular

class Main:
    r1 = receta("Gerson López", "03-10-1990", "Melvin Ortiz", 20156,
            "17-01-2023", "11:30", "Medicina general",
            "2 pildoras de acetaminofén cada 6 horas")

    r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567,
            "31-01-2023", "09:00", "Medicina interna",
            "Tylenol de 20 ml cada 4 horas")

    r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20156, 
            "02-02-2023", "12:00", "Medicina general",
            "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

    #inserción
    lista_c = lista_circular()
    lista_c.insertar(r1)
    lista_c.insertar(r2)
    lista_c.insertar(r3)

    #Recorrer lista
    print("\n----------------------------Se imprimen los datos de la lista-----------------------------\n")
    lista_c.recorrer()

    #Eliminar un nodo de la lista

    print("\n--------------------------Se eliminan los datos de la lista-------------------------------\n")
    lista_c.eliminar(8567, "31-01-2023", "09:00",)
     

    lista_c.recorrer()

    #Eliminando otro nodo

    print("\n--------------------------Se eliminan los datos de la lista-------------------------------\n")
    lista_c.eliminar(20156,"17-01-2023", "11:30")
    lista_c.recorrer()

    #Modificar un nodo
    #Hoja de trabajo 4
    print("\n--------------------------------- Función modificar ---------------------------------------\n")
    lista_c.modificar("Luis García","22-02-2023", "10:40")
    lista_c.recorrer()
     