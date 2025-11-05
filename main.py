# --- MENÚ INTERACTIVO PARA GESTIÓN DE INVENTARIO DE PRODUCTOS ---

# Lista vacía para almacenar los productos (Inventario inicializado vacío)
inventario = []

# Menú interactivo
while True:
    print("\n\tMenú de Gestión de Productos")
    print("\t1. Agregar producto al inventario")
    print("\t2. Mostrar productos registrados")
    print("\t3. Salir")
    print("")

    # Solicitar al usuario que elija una opción 
    opcion = input("\tIngresa una opción (1, 2 o 3): ")

    # Opción 1: Agregar producto al inventario
    if opcion == "1":
        nombre = input("\tIngresa el nombre del producto: ")

        # Validación de la cantidad: asegurar que sea un número positivo
        cantidad = -1
        while cantidad <= 0:
            cantidad_input = input("\tIngresa la cantidad de productos (debe ser mayor a 0): ")

            # Verificar si la entrada está vacía o no es un número positivo
            if not cantidad_input:
                print("\tNo ingresaste nada. Intenta de nuevo.")
            elif not cantidad_input.isdigit():
                print("\tLa cantidad debe ser un número entero positivo. Intenta de nuevo.")
            else:
                # Convertir la entrada (string) a entero y verificar si es positiva
                cantidad = int(cantidad_input)
                if cantidad <= 0:
                    print("\tLa cantidad no puede ser menor o igual a 0. Intenta de nuevo.")

        # Agregar el producto y su cantidad al inventario
        inventario.append([nombre, cantidad])
        print(f"\n\tEl producto '{nombre}' fue agregado con éxito con {cantidad} unidades.")

    # Opción 2: Mostrar inventario usando un índice manual
    elif opcion == "2":
        if inventario:
         print("\n\t---------Inventario Actual---------")
         print("\t Producto           \t Cantidad")
         print("\t------------------------------------")  # Línea para separar los encabezados de los datos
         indice = 0
         while indice < len(inventario):
             print(f"\n\t {inventario[indice][0]}                    \t {inventario[indice][1]}")
             indice += 1
        else:
            print("\n\tEl inventario está vacío.")

    # Opción 3: Salir del menú
    elif opcion == "3":
        print("\n\tSaliendo del programa. ¡Hasta luego!")
        break

    # Opción inválida
    else:
        print("")
        print("\tOpción inválida. Por favor, selecciona una opción válida (1, 2 o 3).")
        

        