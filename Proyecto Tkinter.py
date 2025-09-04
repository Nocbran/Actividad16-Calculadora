import tkinter as tk

ventana = tk.Tk()
ventana.title("CALCULADORA")
ventana.geometry("500x400")

etiqueta = tk.Label(ventana, text="Digita los numeros en los espacios en blanco:")
etiqueta.pack(pady=5)

entrada1 = tk.Entry(ventana)
entrada1.pack(pady=5)
entrada2 = tk.Entry(ventana)
entrada2.pack(pady=5)

resultado = tk.Label(ventana, text="El resultado es: ")
resultado.pack(pady=5)

def suma():
    val3 = 0
    val1 = float(entrada1.get())
    val2 = float(entrada2.get())
    val3 = (val1 + val2)
    resultado.config(text=f"El resultado es ,{val3}!")

def resta():
    val3 = 0
    val1 = float(entrada1.get())
    val2 = float(entrada2.get())
    val3 = (val1 - val2)
    resultado.config(text=f"El resultado es ,{val3}!")

def multiplicacion():
    val3 = 0
    val1 = float(entrada1.get())
    val2 = float(entrada2.get())
    val3 = (val1 * val2)
    resultado.config(text=f"El resultado es ,{val3}!")
def divicion():
    val3 = 0
    val1 = float(entrada1.get())
    val2 = float(entrada2.get())
    val3 = (val1 / val2)
    resultado.config(text=f"El resultado es ,{val3}!")

def limpiar():
    entrada1.delete(0,tk.END)
    entrada2.delete(0,tk.END)
    resultado.config(text="El resultado es: ")

boton_suma = tk.Button(ventana, text="Sumar", command=suma)
boton_suma.pack(pady=5)

boton_resta = tk.Button(ventana, text="Restar", command=resta)
boton_resta.pack(pady=5)

boton_multiplicacion = tk.Button(ventana, text="Multiplicar", command=multiplicacion)
boton_multiplicacion.pack(pady=5)

boton_divicion = tk.Button(ventana, text="Dividir", command=divicion)
boton_divicion.pack(pady=5)

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
boton_limpiar.pack(pady=5)

ventana.mainloop()
