import networkx as nx
import matplotlib.pyplot as plt

class Grafo:
    def __init__(self, num_nodos, pesos):
        self.num_nodos = num_nodos
        self.pesos = pesos
        self.matriz_adyacencia = self.generar_matriz()
        self.grafo = self.crear_grafo()

    def generar_matriz(self):
        matriz = [[0] * self.num_nodos for _ in range(self.num_nodos)]
        for (i, j), peso in self.pesos.items():
            matriz[i][j] = peso
            matriz[j][i] = peso  # Si el grafo es no dirigido
        return matriz
    
    def dijkstra(self, punto_i, punto_y):
        visitados = [False] * self.num_nodos
        distancia = [float('inf')] * self.num_nodos
        distancia[punto_i] = 0
        camino = {nodo: [] for nodo in range(self.num_nodos)}
        camino[punto_i].append(punto_i)
        
        while not all(visitados):
            # Encuentra el nodo no visitado con la distancia mínima
            min_distancia = float('inf')
            min_nodo = -1
            for nodo in range(self.num_nodos):
                if not visitados[nodo] and distancia[nodo] < min_distancia:
                    min_distancia = distancia[nodo]
                    min_nodo = nodo

            # Marca el nodo como visitado
            visitados[min_nodo] = True
            
            # Actualiza las distancias de los nodos vecinos
            for vecino in range(self.num_nodos):
                if not visitados[vecino] and self.matriz_adyacencia[min_nodo][vecino] > 0:
                    nueva_distancia = distancia[min_nodo] + self.matriz_adyacencia[min_nodo][vecino]
                    if nueva_distancia < distancia[vecino]:
                        distancia[vecino] = nueva_distancia
                        camino[vecino] = camino[min_nodo] + [vecino]

        print(f"Distancias más cortas desde el nodo {punto_i}:")
        # for nodo, dist in enumerate(distancia):
        print(f"Nodo {punto_y}: {distancia[punto_y]}, Camino: {camino[punto_y]}")
        return camino[punto_y],distancia[punto_y]
    
    #Funcion que evalua por minuto donde se encuentra Javier y andreina, si nunca se encuentran define los caminos
    #de lo contrario se vuelve a llamar a la funcion en main quitando una ruta
    def tiempos(self,grafo_andreina, camino_javier, camino_andreina,distancia_javier,distancia_andreina):
        tiempo_javier = {} #diccionario para minuto-camino para javier
        tiempo_andreina = {}#diccionario para minuto-camino para andreina
        if distancia_andreina > distancia_javier: #si la distancia de andreina es mayor
            retraso = distancia_andreina-distancia_javier
            print(f"Javier debe salir {retraso} minutos tarde")
            tiempo = 0
            for y, i in enumerate(camino_andreina):
                if i != camino_andreina[-1]: #haya los caminos por los que pasa andreina cada minutos
                    while grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] > 0:
                        grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] =grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] -1
                        tiempo +=1
                        tiempo_andreina[tiempo]=(i,camino_andreina[y+1])
            tiempo = retraso
            for y, i in enumerate(camino_javier): #halla los caminos por los que pasa javier empezando por los min de retraso
                if i != camino_javier[-1]:
                    while self.matriz_adyacencia[i][camino_javier[y+1]] > 0:
                        self.matriz_adyacencia[i][camino_javier[y+1]] =self.matriz_adyacencia[i][camino_javier[y+1]] -1
                        tiempo +=1
                        tiempo_javier[tiempo]=(i,camino_javier[y+1])
            for i in tiempo_javier:
                if tiempo_javier[i] == tiempo_andreina[i] :
                    print(f"En el minuto {i} estan caminando juntos en la ruta {tiempo_javier[i]}")
                    return False,"javier",tiempo_javier[i]

                elif i == distancia_javier+retraso:
                    print("LLegaron sin ser vistos caminando juntos")
                    return True,"",tiempo_javier[i]
                
        else:
            #igual que arriba pero para cuando la distancia de javier es mayor
            retraso = distancia_javier-distancia_andreina
            print(f"Andreina debe salir {retraso} minutos tarde")
            tiempo = retraso
            for y, i in enumerate(camino_andreina):
                if i != camino_andreina[-1]:
                    while grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] > 0:
                        grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] =grafo_andreina.matriz_adyacencia[i][camino_andreina[y+1]] -1
                        tiempo +=1
                        tiempo_andreina[tiempo]=(i,camino_andreina[y+1])
            tiempo = 0
            for y, i in enumerate(camino_javier):
                if i != camino_javier[-1]:
                    while self.matriz_adyacencia[i][camino_javier[y+1]] > 0:
                        self.matriz_adyacencia[i][camino_javier[y+1]] =self.matriz_adyacencia[i][camino_javier[y+1]] -1
                        tiempo +=1
                        tiempo_javier[tiempo]=(i,camino_javier[y+1])
            for i in tiempo_andreina:
                if tiempo_andreina[i] == tiempo_javier[i]:
                    print(f"En el minuto {i} estan caminando juntos en la ruta {tiempo_andreina[i]}")
                    return False,"andreina",tiempo_andreina[i]
                elif i == distancia_andreina+retraso:
                    print("LLegaron sin ser vistos caminando juntos")
                    return True,"",tiempo_andreina[i]

    def crear_grafo(self):
        G = nx.Graph()
        for (i, j), peso in self.pesos.items():
            G.add_edge(i, j, weight=peso)
        return G
    
    def imprimir_matriz(self):
        for fila in self.matriz_adyacencia:
            print(fila)


    def imprimir_grafico(self):
        G = nx.Graph()
        for (i, j), peso in self.pesos.items():
            G.add_edge(i, j, weight=peso)
        pos = nx.spring_layout(G)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue', font_weight='bold', font_size=10)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        plt.show()

    #Codigo de pruebas!!
    # def camino_optimo(self, punto_i, punto_y):
    #     return nx.dijkstra_path(self.grafo, punto_i, punto_y)