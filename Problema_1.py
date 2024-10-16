estado_actual = 'q0'
stack = ['Z']
rechazada = False

cadena = input("Ingrese la cadena a comprobar: ") + 'F'

for simbolo in cadena:  
    if rechazada:
        break

    enestack = stack[-1]  # Ver qué hay en la cima de la pila

    if estado_actual == 'q0':
        if simbolo == '0':
            if enestack == 'Z' or enestack == 'X':
                stack.extend(['X', 'X'])
                if enestack == 'Z':
                    stack.pop()  # Eliminar Z tras insertar
                else:
                    stack.pop()  # Si era X, igual se elimina una X
            else:
                rechazada = True

        elif simbolo == '1' and enestack == 'X':
            estado_actual = 'q1'
            stack.pop()  # Consumir una X
        else:
            rechazada = True

    elif estado_actual == 'q1':
        if simbolo == '0':
            rechazada = True  # No se permiten 0's en q1

        elif simbolo == '1':
            if enestack == 'X':
                stack.pop()  # Consumir una X
            else:
                rechazada = True

        elif simbolo == 'F' and enestack == 'Z':
            estado_actual = 'q2'
            stack.pop()  # Finalizar aceptando
            break

        else:
            rechazada = True

# Resultado final
if not rechazada and estado_actual == 'q2':
    print("Cadena aceptada.")
else:
    print("Cadena rechazada.")
