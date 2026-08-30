# --- MENÚ INTERACTIVO PARA GESTIÓN DE INVENTARIO DE PRODUCTOS ---

# Inventario inicializado vacío
inventario = []

# Menú principal
while True:
    print("\n" + "=" * 45)
    print("       MENÚ DE GESTIÓN DE PRODUCTOS")
    print("=" * 45)
    print("1. Agregar producto al inventario")
    print("2. Mostrar productos registrados")
    print("3. Salir")
    print("=" * 45)

    opcion = input("Ingresa una opción (1, 2 o 3): ").strip()

    # --------------------------------------------------
    # OPCIÓN 1: AGREGAR PRODUCTO
    # --------------------------------------------------
    if opcion == "1":

        # Validar nombre del producto
        while True:
            nombre = input("\nIngresa el nombre del producto: ").strip()

            if nombre:
                break

            print("⚠ El nombre no puede estar vacío.")

        # Validar cantidad
        while True:
            cantidad_input = input(
                "Ingresa la cantidad (mayor a 0): "
            ).strip()

            if not cantidad_input:
                print("⚠ No ingresaste ninguna cantidad.")

            elif not cantidad_input.isdigit():
                print("⚠ Debes ingresar un número entero positivo.")

            else:
                cantidad = int(cantidad_input)

                if cantidad > 0:
                    break

                print("⚠ La cantidad debe ser mayor a 0.")

        # Buscar si el producto ya existe
        producto_existente = False

        for producto in inventario:
            if producto[0].lower() == nombre.lower():
                producto[1] += cantidad
                producto_existente = True

                print(
                    f"\n✓ El producto '{producto[0]}' ya estaba registrado."
                    f"\n  Se agregaron {cantidad} unidades."
                    f"\n  Stock actual: {producto[1]} unidades."
                )
                break

        # Si no existe, agregarlo
        if not producto_existente:
            inventario.append([nombre, cantidad])

            print(
                f"\n✓ El producto '{nombre}' fue agregado correctamente."
                f"\n  Cantidad: {cantidad} unidades."
            )

    # --------------------------------------------------
    # OPCIÓN 2: MOSTRAR INVENTARIO
    # --------------------------------------------------
    elif opcion == "2":

        if inventario:

            print("\n" + "=" * 45)
            print("              INVENTARIO ACTUAL")
            print("=" * 45)
            print(f"{'Producto':<30}{'Cantidad':>10}")
            print("-" * 45)

            indice = 0

            while indice < len(inventario):
                nombre = inventario[indice][0]
                cantidad = inventario[indice][1]

                print(f"{nombre:<30}{cantidad:>10}")

                indice += 1

            print("=" * 45)
            print(f"Total de productos registrados: {len(inventario)}")

        else:
            print("\n⚠ El inventario está vacío.")

    # --------------------------------------------------
    # OPCIÓN 3: SALIR
    # --------------------------------------------------
    elif opcion == "3":

        print("\n✓ Saliendo del programa. ¡Hasta luego!")
        break

    # --------------------------------------------------
    # OPCIÓN INVÁLIDA
    # --------------------------------------------------
    else:
        print("\n⚠ Opción inválida. Selecciona 1, 2 o 3.")
        
