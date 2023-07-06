import funciones as fn

while True:
    fn.mostrar_menu()
    opcion = fn.validar_opcion()
    if opcion ==1:
        fn.comprar_entradas()
    elif opcion ==2:
        fn.mostrar_ubicaciones_disponibles()
    elif opcion ==3:
        fn.lista_asistentes()
    elif opcion ==4:
        fn.total_ganancias()
    else:
        fn.salir()