from lista_enlazada import lista_enlazada
from receta import receta
class Main:


# Creación del ojeto Receta
    r1 = receta("Gerson López","03-10-1999", "Melvin Ortiz", 20156, "19-01-2023", "11:30", "Medicina general", "2 pildoras de acetaminofen cada 6 horas")
    r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023", "09:00", "Medicina interna", "Tylenol de 20 ml cada 4 horas")
    r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20156, "02-02-2023", "12:00", "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

# Inserción   
    lista_e=lista_enlazada()
    print("\n---------------------------Ubicación de lista en la memoria ------------------------------\n")
    print(lista_e)
    print("\n----------------------------Se imprimen los datos de la lista-----------------------------\n")
    lista_e.insertar(r1)
    lista_e.insertar(r2)
    lista_e.insertar(r3)

    #Recorrer
    lista_e.recorrer()
    print("\n--------------------------Se eliminan los datos de la lista-------------------------------\n")

    #Eliminar
    lista_e.eliminar(20156,"19-01-2023", "11:30")
    lista_e.recorrer()
    print("\n------------------------Se modifican datos de la lista---------------------------------\n")

    lista_e.modificar("Luis García","22-02-2023", "10:40")
    lista_e.recorrer()
    