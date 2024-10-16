estado_actual = 'q0'
stack = ['Z']
rechazada = False

cadena = input("Ingrese la cadena a comprobar: ") + 'F'

for simbolo in cadena:
    if rechazada:
        break

    enestack = stack[-1]  # Ver la cima de la pila

    if estado_actual == 'q0':
        if simbolo == '0':
            if enestack == 'Z':
                stack.append('X')
                stack.append('X')
                stack.append('Z')
                stack.pop()  # Quitamos la 'Z'
            elif enestack == 'X':
                stack.append('X')
                stack.append('X')
                stack.pop()  # Quitamos la 'X'
            else:
                rechazada = True

        elif simbolo == '1':
            if enestack == 'X':
                estado_actual = 'q1'
                stack.pop()  # Quitamos la 'X'
            else:
                rechazada = True

    elif estado_actual == 'q1':
        if simbolo == '0':
            rechazada = True  # No se permiten '0' en q1

        elif simbolo == '1':
            if enestack == 'X':
                stack.pop()  # Quitamos la 'X'
            else:
                rechazada = True

        elif simbolo == 'F':
            if enestack == 'Z':
                estado_actual = 'q2'
                stack.pop()  # Quitamos la 'Z'
                break
            else:
                rechazada = True

# Resultado final
if not rechazada and estado_actual == 'q2':
    print("Cadena aceptada.")
else:
    print("Cadena rechazada.")
