import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Digita el primer numero:")
etiqueta.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="El resultado es: ")
resultado.pack(pady=5)

def suma():
    val1 = entrada1.get()
    val2 = entrada2.get()
    val3 = val1 + val2
    resultado.config(text=f"el resultado es ,{val3}!")

def resta():
    entrada1.delete(0, tk.END)
    etiqueta.config(text="Escribe tu nombre:")
    pass
def multiplicacion():
    pass
def divicion():
    pass

boton_suma = tk.Button(ventana, text="Saludar", command=suma)
boton_suma.pack(pady=5)

    boton_resta = tk.Button(ventana, text="Limpiar", command=resta)
    boton_resta.pack(pady=5)

    boton_multiplicacion = tk.Button(ventana, text="Salir", command=multiplicacion)
    boton_multiplicacion.pack(pady=5)

    boton_divicion = tk.Button(ventana, text="Salir", command=divicion)
    boton_divicion.pack(pady=5)

    ventana.mainloop()
