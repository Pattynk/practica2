# 1. Crear una ventana con Tkinter o PyQt.
import tkinter as tk

# 1.1 Crear la ventana principal, usar el ventana.mainloop() al final
ventana = tk.Tk()
ventana.title("Ventana de eventos")
ventana.geometry("600x400")  
ventana.config(bg="lightpink")  

# 1.2 Escribir un título de bienvenida al programa
etiqueta = tk.Label(ventana, text="Bienvenido a la práctica de EVENTOS", font=("Arial", 12))
etiqueta.config(bg="lightpink")  
etiqueta.pack(pady=10)


# 2 Implementar eventos del mouse (clics, movimiento).
# 2.1-1 Función para mostrar las coordenadas del mouse en la etiqueta 4
def evento_mouse(event):
    etiqueta4.config(text=f"Mouse en coordenada: ({event.x}, {event.y})")

# 2.1-2  Etiqueta para las coordenadas
etiqueta4 = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta4.config(bg="lightpink")  
etiqueta4.pack(pady=10)

#2.2-1 Función para mostrar etiqueta de cambio de color y siguiente evento
def mostrar_mensaje():
    boton.config(bg="blue") 
    etiqueta3 = tk.Label(ventana, text="Da doble click a este mensaje cambiar el color de fondo", font=("Arial", 12))
    etiqueta3.config(bg="blue")  
    etiqueta3.pack(pady=9)
    etiqueta5.config(text="Si presionas una tecla, te digo cuál fue")
    
# 2.2-2 Crear un botón para el evento de clics
boton = tk.Button(ventana, text="Haz click aquí para cambiar el color del botón", command = mostrar_mensaje)
boton.pack(pady=9)


# 3 Implementar eventos del teclado (presionar teclas)
# 3.1-1  Etiqueta para las teclas
etiqueta5 = tk.Label(ventana, text="", font=("Arial", 12))
etiqueta5.pack(pady=6)

# 3.1-2 Función para detectar teclas presionadas
def tecla_presionada(event):
    etiqueta5.config(text=f"Tecla presionada: {event.keysym}")

#4 Es mostrar todo en pantalla, sin embargo todo queda documetado en el mismo seguimiento

# 5 Detectar eventos de doble clic y cambiar el color de la ventana.
# 5.1 Función para la línea anterior
def doble_clic(event):
    ventana.config(bg="blue") 
    etiqueta.config(bg="blue")  
    etiqueta4.config(bg="blue")  
 

# 6 Asociar el evento de presionar la barra espaciadora para limpiar el texto de la etiqueta.
# 6.1 Función para limpiar el texto de las etiquetas cuando se presiona la tecla espacio
def limpiar_etiqueta(event):
    etiqueta.config(text="¡Vaya! Ya has manejado varios eventos")
    etiqueta5.config(text="   ")
    etiqueta4.config(text="¡Texto limpiado!")


# 6.2-1 Función para salir de la aplicación
def salir_aplicacion():
    ventana.quit()

# 6.2-2 Botón para salir de la aplicación
boton_salir = tk.Button(ventana, text="Salir", command=salir_aplicacion)
boton_salir.pack(pady=5)


# Asociar eventos del mouse y teclado
ventana.bind("<Motion>", evento_mouse)         # Detectar movimiento del mouse
ventana.bind("<Double-Button-1>", doble_clic)  # Detectar doble clic izquierdo
ventana.bind("<KeyPress>", tecla_presionada)   # Detectar cualquier tecla presionada
ventana.bind("<space>", limpiar_etiqueta)      # Limpiar texto con barra espaciadora

ventana.mainloop()
