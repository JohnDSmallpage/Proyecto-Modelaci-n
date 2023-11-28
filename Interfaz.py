import tkinter as tk
from tkinter import ttk
from main import main
from Grafo import Grafo
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Ejemplo de uso
pesos_javier = {
    (0, 6): 5, (0, 1): 5, (1, 2): 5, (2,3):5, (1, 7): 7,(2,8):7, (7,13):7, (13,19):7,(25,31):7, (19,25):7, (3, 4): 5, (3, 9): 7, (4, 5): 5, (4, 10): 5, (5, 11): 5, (6, 12): 5, (6,7):5,(7,8):5,(7,13):7,(8,9):5,(8,14):7,(9,10):5,(9,15):7,(10,11):5,(10,16):5,(11,17):5,(12,13):5,(12,18):5,(13,14):5,(13,19):7,(14,15):5,(14,20):7,(15,16):5,(15,21):7,(16,17):5,(16,22):5,(17,23):5,(18,19):5,(18,24):5,(19,20):5,(19,25):7,(20,21):5,(20,26):7,(21,22):5,(21,27):7,(22,23):5,(22,28):5,(23,29):5,(24,25):10,(24,30):5,(25,26):10,(25,31):7,(26,27):10,(26,32):7,(27,28):10,(27,33):7,(28,29):10,(28,34):5,(29,35):5,(30,31):5,(31,32):5,(32,33):5,(33,34):5,(34,35):5}

pesos_andreina = {
    (0, 6): 7, (0, 1): 7, (1, 2): 7,(2, 3): 7,(2,8): 9, (19, 25): 9, (20, 26): 9,(26, 32): 9,(10, 11): 7,(1, 7): 9, (3, 4): 7, (3, 9): 9, (4, 5): 7, (4, 10): 7, (5, 11): 7, (6, 12): 7, (6,7):7,(7,8):7,(7,13):9,(8,9):7,(8,14):9,(9,10):7,(9,15):9,(10,16):7,(11,17):7,(12,13):7,(12,18):7,(13,14):7,(13,19):9,(14,15):7,(14,20):9,(15,16):7,(15,21):9,(16,17):7,(16,22):7,(17,23):7,(18,19):7,(18,24):7,(19,20):7,(19,25):9,(20,21):7,(20,26):9,(21,22):7,(21,27):9,(22,23):7,(22,28):7,(23,29):7,(24,25):12,(24,30):7,(25,26):12,(25,31):9,(26,27):12,(26,32):9,(27,28):12,(27,33):9,(28,29):12,(28,34):7,(29,35):7,(30,31):7,(31,32):7,(32,33):7,(33,34):7,(34,35):7}



opciones = [
    ['Discoteca "The Darkness"', 31],
    ['Discoteca "La Pasión"', 10],
    ['Cervecería "Mi Rolita"', 33],
    ['Café "Sensación"', 35]
]

def mostrar_seleccion():
    nodos_coloreados_javier={}
    nodos_coloreados_andreina={}
    selec = -1
    seleccion = lista_desplegable.get()
    for i in range(len(opciones)):
        if seleccion == opciones[i][0]:
            selec = opciones[i][1]

    resultado_string, camino_javier, camino_andreina = main(selec)
    label_resultado.config(text=f"Seleccionado: {seleccion}\nResultado: {resultado_string}")
        # Crear grafos
    grafo_javier_imprimir = Grafo(36, pesos_javier)
    grafo_andreina_imprimir = Grafo(36, pesos_andreina)

    print(f"PRUEBA: f{camino_javier}")
    print(camino_andreina)

    #Nodos color verde

    for i in range(36):
        if i in camino_javier:
            nodos_coloreados_javier[i]='green'
        else:
            nodos_coloreados_javier[i]='red'

    for i in range(36):
        if i in camino_andreina:
            nodos_coloreados_andreina[i]='green'
        else:
            nodos_coloreados_andreina[i]='red'

    # Obtener gráficos y posiciones
    J, pos_j = grafo_javier_imprimir.graficar()
    A, pos_a = grafo_andreina_imprimir.graficar()

    labels_j = nx.get_edge_attributes(J, 'weight')
    labels_a = nx.get_edge_attributes(A, 'weight')

    labels_node_j = nx.get_node_attributes(J, 'label')
    labels_node_a = nx.get_node_attributes(A, 'label')
    node_size= 1200
    edge_width = 2.0

    # Configurar subgráficos en una fila
    fig, axs = plt.subplots(1, 2, figsize=(14, 7))

    # Dibujar gráficos en los subgráficos
    nx.draw(J, pos_j, with_labels=True, labels=labels_node_j, font_weight='bold', ax=axs[0], node_size=node_size, width=edge_width, node_color=[nodos_coloreados_javier.get(node, 'green') for node in J.nodes()])
    nx.draw_networkx_edge_labels(J, pos_j, edge_labels=labels_j, ax=axs[0])
    axs[0].set_title('Grafo Javier')

    nx.draw(A, pos_a, with_labels=True,  labels=labels_node_a, font_weight='bold', ax=axs[1], node_size=node_size, width=edge_width, node_color=[nodos_coloreados_andreina.get(node, 'green') for node in A.nodes()])
    nx.draw_networkx_edge_labels(A, pos_a, edge_labels=labels_a, ax=axs[1])
    axs[1].set_title('Grafo Andreina')
    
    # Añadir el lienzo de la figura a la ventana de Tkinter
    canvas = FigureCanvasTkAgg(fig, master=ventana)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=2, column=0, columnspan=2)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica con Lista Desplegable")

# Crear una lista de valores
valores = ['Discoteca "The Darkness"', 'Discoteca "La Pasión"', 'Cervecería "Mi Rolita"', 'Café "Sensación"']

# Crear una lista desplegable
lista_desplegable = ttk.Combobox(ventana, values=valores, state="readonly")
lista_desplegable.grid(row=0, column=0, padx=10, pady=10)
lista_desplegable.set(valores[0])

# Crear un botón para mostrar la selección
boton_mostrar = ttk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.grid(row=0, column=1, padx=10, pady=10)

# Crear una etiqueta para mostrar el resultado
label_resultado = ttk.Label(ventana, text="")
label_resultado.grid(row=1, column=0, columnspan=2, pady=10)




# Iniciar el bucle principal
ventana.mainloop()

