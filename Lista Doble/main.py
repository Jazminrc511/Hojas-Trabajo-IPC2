from lista_doble import lista_doble
from receta import receta
class Main:
    r1 = receta("Gerson López","03-10-1990","Melvin Ortiz", 20156, "17-01-2023", "11:30", "Medicina general", "2 pildoras de acetaminofen cada 6 horas")
    r2 = receta("Karen Gómez", "08-05-2000", "Jorge Merida", 8567, "31-01-2023", "09:00", "Medicina interna", "Tylenol de 20 ml cada 4 horas")
    r3 = receta("Luis García", "17-09-1987", "Melvin Ortiz", 20157, "02-02-2023", "12:00", "Medicina general", "2 cucharadas de Pepto-Bismol cada hora hasta que la diarrea desaparezca")

    print("\n----------------------------Se imprimen los datos de la lista-----------------------------\n")
    lista_d = lista_doble()
    lista_d.insertar(r1)
    lista_d.insertar(r2)
    lista_d.insertar(r3)

    #Recorrer
    lista_d.recorrer()

    print("\n--------------------------Se eliminan los datos de la lista-------------------------------\n")

    #Eliminar el nodo del medio de la lista
    lista_d.eliminar(8567,"31-01-2023", "09:00")
    lista_d.recorrer()


    #Eliminar nodo a nodo de la lista
    lista_d.eliminar(20157,"02-02-2023","12:00")
    lista_d.recorrer()

    lista_d.eliminar( 8567,"31-01-2023", "09:00")
    lista_d.recorrer()

    lista_d.eliminar(20156, "17-01-2023", "11:30")
    lista_d.recorrer()

    print("\n------------------------Se modifican datos de la lista---------------------------------\n")
    print("\n------------------------------ Hoja de trabajo 5 ---------------------------------------\n")

    lista_d.modificar("Luis García","27-02-2023", "11:11")
    lista_d.recorrer()
