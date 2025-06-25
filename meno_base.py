def datos_ronald():
 print("Mi nombre es Ronald Silva y tengo 22 años!")

def datos_alexander():
 print("Mi nombre es alexander y tengo 18 años")

def datos_Francisco():
 print("Mi nombre es Francisco y tengo 19 años")




while True:
 print("\n--- MENÚ PRINCIPAL ---")
 print("1. Función de integrante 1")
 print("2. Función de integrante 2")
 print("3. Función de integrante 3")
 print("0. Salir")
 op = input("Seleccione opción: ")
 if op == "0":
    print("Programa finalizado.")
    break
 elif op == "1":
    datos_ronald()
 elif op == "2":
    datos_alexander()
 elif op == "3":
    datos_francisco()
 else:
    print(" Opción inválida.")
