from Grafo import Grafo

def main():

    # Ejemplo de uso
    pesos_javier = {
        (0, 6): 5, (0, 1): 5, (1, 2): 5, (1, 7): 7, (3, 4): 5, (3, 8): 7, (4, 5): 5, (4, 9): 7, (5, 6): 5, (5, 10): 5, (6, 11): 5}

    grafo_javier = Grafo(36, pesos_javier)
    grafo_javier.imprimir_matriz() 

main()

