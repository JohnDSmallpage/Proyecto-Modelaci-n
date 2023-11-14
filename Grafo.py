class Grafo:
    def __init__(self, num_nodos, pesos):
        self.num_nodos = num_nodos
        self.pesos = pesos
        self.matriz_adyacencia = self.generar_matriz()

    def generar_matriz(self):
        matriz = [[0] * self.num_nodos for _ in range(self.num_nodos)]
        for (i, j), peso in self.pesos.items():
            matriz[i][j] = peso
            matriz[j][i] = peso  # Si el grafo es no dirigido
        return matriz
    
    def imprimir_matriz(self):
        for fila in self.matriz_adyacencia:
            print(fila)
