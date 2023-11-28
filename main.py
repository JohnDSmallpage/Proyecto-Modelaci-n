from Grafo import Grafo

def main(destino):

    # Ejemplo de uso
    pesos_javier = {
        (0, 6): 5, (0, 1): 5, (1, 2): 5, (2,3):5, (1, 7): 7,(2,8):7, (7,13):7, (13,19):7,(25,31):7, (19,25):7, (3, 4): 5, (3, 9): 7, (4, 5): 5, (4, 10): 5, (5, 11): 5, (6, 12): 5, (6,7):5,(7,8):5,(7,13):7,(8,9):5,(8,14):7,(9,10):5,(9,15):7,(10,11):5,(10,16):5,(11,17):5,(12,13):5,(12,18):5,(13,14):5,(13,19):7,(14,15):5,(14,20):7,(15,16):5,(15,21):7,(16,17):5,(16,22):5,(17,23):5,(18,19):5,(18,24):5,(19,20):5,(19,25):7,(20,21):5,(20,26):7,(21,22):5,(21,27):7,(22,23):5,(22,28):5,(23,29):5,(24,25):10,(24,30):5,(25,26):10,(25,31):7,(26,27):10,(26,32):7,(27,28):10,(27,33):7,(28,29):10,(28,34):5,(29,35):5,(30,31):5,(31,32):5,(32,33):5,(33,34):5,(34,35):5}

    pesos_andreina = {
        (0, 6): 7, (0, 1): 7, (1, 2): 7,(2, 3): 7,(2,8): 9, (19, 25): 9, (20, 26): 9,(26, 32): 9,(10, 11): 7,(1, 7): 9, (3, 4): 7, (3, 9): 9, (4, 5): 7, (4, 10): 7, (5, 11): 7, (6, 12): 7, (6,7):7,(7,8):7,(7,13):9,(8,9):7,(8,14):9,(9,10):7,(9,15):9,(10,16):7,(11,17):7,(12,13):7,(12,18):7,(13,14):7,(13,19):9,(14,15):7,(14,20):9,(15,16):7,(15,21):9,(16,17):7,(16,22):7,(17,23):7,(18,19):7,(18,24):7,(19,20):7,(19,25):9,(20,21):7,(20,26):9,(21,22):7,(21,27):9,(22,23):7,(22,28):7,(23,29):7,(24,25):12,(24,30):7,(25,26):12,(25,31):9,(26,27):12,(26,32):9,(27,28):12,(27,33):9,(28,29):12,(28,34):7,(29,35):7,(30,31):7,(31,32):7,(32,33):7,(33,34):7,(34,35):7}
    
    intersecciones= {
            0: "Calle 55 con Carrera 15",
            1: "Calle 55 con Carrera 14",
            2: "Calle 55 con Carrera 13",
            3: "Calle 55 con Carrera 12",
            4: "Calle 55 con Carrera 11",
            5: "Calle 55 con Carrera 10",
            6: "Calle 54 con Carrera 15",
            7: "Calle 54 con Carrera 14",
            8: "Calle 54 con Carrera 13",
            9: "Calle 54 con Carrera 12",
            10: "Calle 54 con Carrera 11",
            11: "Calle 54 con Carrera 10",
            12: "Calle 53 con Carrera 15",
            13: "Calle 53 con Carrera 14",
            14: "Calle 53 con Carrera 13",
            15: "Calle 53 con Carrera 12",
            16: "Calle 53 con Carrera 11",
            17: "Calle 53 con Carrera 10",
            18: "Calle 52 con Carrera 15",
            19: "Calle 52 con Carrera 14",
            20: "Calle 52 con Carrera 13",
            21: "Calle 52 con Carrera 12",
            22: "Calle 52 con Carrera 11",
            23: "Calle 52 con Carrera 10",
            24: "Calle 51 con Carrera 15",
            25: "Calle 51 con Carrera 14",
            26: "Calle 51 con Carrera 13",
            27: "Calle 51 con Carrera 12",
            28: "Calle 51 con Carrera 11",
            29: "Calle 51 con Carrera 10",
            30: "Calle 50 con Carrera 15",
            31: "Calle 50 con Carrera 14",
            32: "Calle 50 con Carrera 13",
            33: "Calle 50 con Carrera 12",
            34: "Calle 50 con Carrera 11",
            35: "Calle 50 con Carrera 10"
        }


    #grafo_javier.imprimir_matriz() 
    # grafo_javier.imprimir_grafico()
    Casa_javier = 7
    Final = destino
    Casa_andreina = 20
    resultado_string= ""
    

    encontrado = False
    while not encontrado: #evalua que no se haya encontrado unas rutas donde no se encuentran
        #regresa si encontro camino, la persona con la distancia mas corta y el camino donde se encuentran
        grafo_javier = Grafo(36, pesos_javier) 
        grafo_andreina = Grafo(36, pesos_andreina)
        camino_javier,distancia_javier = grafo_javier.dijkstra(Casa_javier,Final)
        camino_andreina,distancia_andreina = grafo_andreina.dijkstra(Casa_andreina,Final)
        camino_javier_copia= camino_javier.copy()
        camino_andreina_copia= camino_andreina.copy()
        encontrado,nombre,camino, retraso, minuto = grafo_javier.tiempos(grafo_andreina,camino_javier,camino_andreina,distancia_javier,distancia_andreina)
        # print(encontrado,nombre,camino)
        if nombre == "andreina": #elimina el camino donde se encuentran
            pesos_andreina[camino] = 0 
            for nodo in range(len(camino_andreina)):
                camino_andreina[nodo]= intersecciones[camino_andreina[nodo]]
            for nodo in range(len(camino_javier)):
                camino_javier[nodo]= intersecciones[camino_javier[nodo]]

        if nombre == "javier":
            pesos_javier[camino] = 0 
            for nodo in range(len(camino_andreina)):
                camino_andreina[nodo]= intersecciones[camino_andreina[nodo]]
            for nodo in range(len(camino_javier)):
                camino_javier[nodo]= intersecciones[camino_javier[nodo]]
        
        camino= list(camino)
        camino= intersecciones[camino[0]] + " - " + intersecciones[camino[1]]
            

        

        resultado_string+= f"""
        El camino de Javier es: {camino_javier} con un tiempo de {distancia_javier} minutos
        El camino de Andreína es: {camino_andreina} con un tiempo de {distancia_andreina} minutos
"""
        if nombre == "andreina": #elimina el camino donde se encuentran
            resultado_string+= f"""
        Javier tiene que salir {retraso} minutos antes que Andreina
"""
        if nombre == "javier":
            resultado_string+= f"""
        Andreina tiene que salir {retraso} minutos antes que Javier
""" 
        if encontrado== False:
            resultado_string+= f"""
        Los encontraron caminando juntos en el minuto {minuto} en el camino {camino}, por lo que se calcula otra ruta
"""
        else:
            resultado_string+= f"""
        No fueron encontrados caminando juntos, por lo que esta es la solucion
"""
    

    return resultado_string, camino_javier_copia, camino_andreina_copia
   
        # if encontrado == False: #si no se encontro camino vuelve a inicializar las variables para la siguiente evaluacion
            # grafo_javier = Grafo(36, pesos_javier)
            # grafo_andreina = Grafo(36, pesos_andreina)
            # camino_javier,distancia_javier = grafo_javier.dijkstra(Casa_javier,Final)
            # camino_andreina,distancia_andreina = grafo_andreina.dijkstra(Casa_andreina,Final)

