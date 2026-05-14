def perder_vida(vidas, motivo):
    vidas -= 1
    print(f"\n{motivo}")
    if vidas > 0:
        print(f"Pierdes 1 vida. Te quedan {vidas} vidas.")
    else:
        print("Pierdes tu ultima vida.")
    return vidas


def pedir_opcion(mensaje, opciones):
    opcion = input(mensaje).strip().lower()
    while opcion not in opciones:
        print(f"Opcion invalida. Debes elegir una de estas: {', '.join(opciones)}")
        opcion = input(mensaje).strip().lower()
    return opcion


def main():
    vidas = 3
    jugador = input("Como quieres llamarte, aventurero? ").strip()

    if not jugador:
        jugador = "Viajero"

    print(f"\nBienvenido, {jugador}.")
    print("Esta es una aventura por terminal.")
    print("Tu objetivo es encontrar el Corazon de la Montaña y salir con vida.")
    print("Solo hay una forma correcta de ganar.")
    print("Cada mala decision te quitara una vida.\n")

    print("Despiertas frente a una montaña antigua.")
    print("Ante ti hay dos caminos: uno entra al bosque y otro baja a una cueva humeda.")
    opcion_1 = pedir_opcion(
        "Elige tu camino ('bosque' o 'cueva'): ",
        ["bosque", "cueva"],
    )

    if opcion_1 != "bosque":
        vidas = perder_vida(vidas, "La cueva se derrumba y logras escapar por poco.")
        if vidas == 0:
            print("\nGAME OVER")
            return
        print("\nRegresas al inicio, herido pero con una ultima oportunidad.")
        opcion_1 = pedir_opcion(
            "Ahora elige correctamente ('bosque'): ",
            ["bosque"],
        )

    print("\nTe adentras en el bosque y la niebla cubre todo.")
    print("Encuentras una mochila con una cuerda y una linterna, pero solo puedes tomar una.")
    opcion_2 = pedir_opcion(
        "Que tomas? ('cuerda' o 'linterna'): ",
        ["cuerda", "linterna"],
    )

    if opcion_2 != "linterna":
        vidas = perder_vida(vidas, "Mas adelante la oscuridad te hace caer en unas ramas espinosas.")
        if vidas == 0:
            print("\nGAME OVER")
            return
        print("\nVuelves a la mochila y decides pensar mejor.")
        opcion_2 = pedir_opcion(
            "Elige de nuevo ('linterna'): ",
            ["linterna"],
        )

    print("\nLa linterna revela una puerta de piedra escondida entre los arboles.")
    print("Dentro hay un puente fragil sobre un abismo.")
    print("Puedes cruzarlo caminando rapido o avanzando despacio.")
    opcion_3 = pedir_opcion(
        "Como cruzas? ('rapido' o 'despacio'): ",
        ["rapido", "despacio"],
    )

    if opcion_3 != "despacio":
        vidas = perder_vida(vidas, "El puente se rompe bajo tus pasos y apenas logras sujetarte.")
        if vidas == 0:
            print("\nGAME OVER")
            return
        print("\nConsigues volver al borde y lo intentas otra vez con mas cuidado.")
        opcion_3 = pedir_opcion(
            "Elige de nuevo ('despacio'): ",
            ["despacio"],
        )

    print("\nLlegas a una sala ceremonial.")
    print("El Corazon de la Montaña flota sobre un pedestal.")
    print("Un guardian dormido protege la salida.")
    print("Puedes gritar, correr o moverte en silencio.")
    opcion_4 = pedir_opcion(
        "Que haces? ('gritar', 'correr' o 'silencio'): ",
        ["gritar", "correr", "silencio"],
    )

    if opcion_4 != "silencio":
        vidas = perder_vida(vidas, "El guardian despierta y te golpea antes de volver a dormirse.")
        if vidas == 0:
            print("\nGAME OVER")
            return
        print("\nRespiras hondo. Sabes que solo queda una manera de lograrlo.")
        opcion_4 = pedir_opcion(
            "Elige de nuevo ('silencio'): ",
            ["silencio"],
        )

    print("\nTomas el Corazon de la Montaña sin hacer ruido.")
    print("La salida se abre lentamente frente a ti.")
    print(f"\nFELICIDADES, {jugador}!")
    print(f"Has ganado la aventura con {vidas} vida(s) restante(s).")
    print("Descubriste la unica ruta correcta y escapaste de la montaña.\n")


main()
