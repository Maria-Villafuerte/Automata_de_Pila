estado_actual = 'q'
stack = ['Z']
rechazada = False

cadena = input("Ingrese la cadena a comprobar: ") + 'F'

for simbolo in cadena:
    if rechazada:
        break

    enestack = stack[-1]  # Ver la cima de la pila

    if estado_actual == 'q':
        if simbolo == 'a':
            if enestack == 'Z':
                stack.append('X')
            elif enestack == 'X':
                stack.append('X')
            else:
                rechazada = True

        elif simbolo == 'b':
            if enestack == 'X':
                estado_actual = 'p'
                stack.pop()  # Quitamos la 'X'
            else:
                rechazada = True

    elif estado_actual == 'p':
        if simbolo == 'a':
            rechazada = True  # No se permiten 'a' en p

        elif simbolo == 'b':
            if enestack == 'X':
                stack.pop()  # Quitamos la 'X'
            else:
                rechazada = True

        elif simbolo == 'c':
            if enestack == 'X':
                rechazada = True # No hay igual cantidad de a y b
            elif enestack == 'Z':
                estado_actual = 's'
                stack.append('Y')

    elif estado_actual == 's':
        if simbolo == 'c':
            if enestack == 'Y':
                stack.append('Y')
            else:
                rechazada = True
            
        elif simbolo == 'd':
            if enestack == 'Y':
                stack.pop()  # Quitamos la 'Y'
                estado_actual = 'r'
            else:
                rechazada = True
        

    elif estado_actual == 'r':
        if simbolo == 'd':
            if enestack == 'Y':
                stack.pop()  # Quitamos la 'Y'
            else:
                rechazada = True


        elif simbolo == 'F':
            if enestack == 'Z':
                estado_actual = 'f'
                stack.pop()  # Quitamos la 'Z'
                break
            else:
                rechazada = True

# Resultado final
if not rechazada and estado_actual == 'f':
    print("Cadena aceptada.")
else:
    print("Cadena rechazada.")
