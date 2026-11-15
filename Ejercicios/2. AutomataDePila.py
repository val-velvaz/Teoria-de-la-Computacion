# pruebas
test = [
    "aaaabbb",
    "ab",
    "ababa",
    "aaaabb",
    "bbbaaa",
    "aaabbb",
    "abab",
    "aabbab",
]  # 0, 1, 0, 0, 0, 1

c_aceptadas = []
c_rechazadas = []


def registrar(estado_actual: int, registro: list):
    # posibles estados de la pila
    estados = ["q0", "q1", "q2"]
    registro.append(estados[estado_actual])


for s in test:
    pila = []
    # registro de estados, empieza vacio
    registro = []
    # inicializacion de la pila
    pila.append("#")  # lambda, lambda; #
    registro.append(registrar(0, registro))

    aceptada = True

    for c in s:
        if c == "a":
            # a, lambda; x
            pila.append("x")
            registro.append(registrar(1, registro))
        elif c == "b":
            if pila[-1] == "#":
                aceptada = False
                break
            pila.pop()
            registro.append(registrar(1, registro))

    if aceptada and pila[-1] == "#":
        pila.pop()  # vaciar toda la pila
        # lambda, #; lambda
        registro.append(registrar(2, registro))
        c_aceptadas.append(s)
    else:
        c_rechazadas.append(s)

print("Cadenas aceptadas: ", c_aceptadas)
print("Cadenas rechazadas: ", c_rechazadas)
