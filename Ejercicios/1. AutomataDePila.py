pila = []
registro = []
test = "())))((("  # cadena de prueba


def registrar(estado: int, registro: list):
    estados = ["q0", "q1", "q2"]
    registro.append(estados[estado])


registrar(0, registro)
pila.append("#")  # lambda, lambda; #
registrar(1, registro)

aceptada = True
for c in test:  # c de character
    if c == "(":
        # "x" caracter provisional
        pila.append("x")  # ( , lambda ; x
        registrar(1, registro)
    elif c == ")":
        if pila[-1] == "#":
            aceptada = False  # lambda, # ; lambda
            break
        pila.pop()  # ) , x; lambda
        registrar(1, registro)

if aceptada and pila[-1] == "#":
    pila.pop()  # lambda, #;  lambda
    registrar(2, registro)
    print("Aceptada", registro)
else:
    print("Rechazada", registro)
