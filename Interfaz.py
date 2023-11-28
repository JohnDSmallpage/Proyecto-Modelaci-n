import tkinter as tk
from tkinter import ttk
from main import main

opciones = [
            ['Discoteca "The Darkness"',31],
            ['Discoteca "La Pasión"',10],
            ['Cervecería "Mi Rolita"',33],
            ['Café "Sensación"',35]]
        
            

def mostrar_seleccion():
    selec = 0;
    seleccion = lista_desplegable.get()
    for i in range(len(opciones)):
        if seleccion == opciones[i][0]:
            selec=opciones[i][1]

    resultado_string = main(selec)
    label_resultado.config(text=f"Seleccionado: {seleccion}\nResultado: {resultado_string}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Interfaz Gráfica con Lista Desplegable")

# Crear una lista de valores
valores = ['Discoteca "The Darkness"', 'Discoteca "La Pasión"', 'Cervecería "Mi Rolita"', 'Café "Sensación"']

# Crear una lista desplegable
lista_desplegable = ttk.Combobox(ventana, values=valores)
lista_desplegable.grid(row=0, column=0, padx=10, pady=10)

# Crear un botón para mostrar la selección
boton_mostrar = ttk.Button(ventana, text="Mostrar Selección", command=mostrar_seleccion)
boton_mostrar.grid(row=0, column=1, padx=10, pady=10)

# Crear una etiqueta para mostrar el resultado
label_resultado = ttk.Label(ventana, text="")
label_resultado.grid(row=1, column=0, columnspan=2, pady=10)

# Iniciar el bucle principal
ventana.mainloop()
