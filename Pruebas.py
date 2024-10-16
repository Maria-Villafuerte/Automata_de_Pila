import unittest

def test_automata(cadena):
    estado_actual = 'q0'
    stack = ['Z']
    rechazada = False

    cadena = cadena + 'F'

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
    return not rechazada and estado_actual == 'q2'

class TestAutomata(unittest.TestCase):
    
    def test_011(self):
        resultado = test_automata('011')
        self.assertTrue(resultado, "La cadena '011' debería ser aceptada")
        print(f"Prueba '011': {'Aceptada' if resultado else 'Rechazada'}")
    
    def test_00111(self):
        resultado = test_automata('00111')
        self.assertTrue(resultado, "La cadena '00111' debería ser aceptada")
        print(f"Prueba '00111': {'Aceptada' if resultado else 'Rechazada'}")
    
    def test_0001111(self):
        resultado = test_automata('0001111')
        self.assertTrue(resultado, "La cadena '0001111' debería ser aceptada")
        print(f"Prueba '0001111': {'Aceptada' if resultado else 'Rechazada'}")
    
    def test_01(self):
        resultado = test_automata('01')
        self.assertFalse(resultado, "La cadena '01' debería ser rechazada")
        print(f"Prueba '01': {'Aceptada' if resultado else 'Rechazada'}")
    
    def test_0011(self):
        resultado = test_automata('0011')
        self.assertFalse(resultado, "La cadena '0011' debería ser rechazada")
        print(f"Prueba '0011': {'Aceptada' if resultado else 'Rechazada'}")
    
    def test_00011(self):
        resultado = test_automata('00011')
        self.assertFalse(resultado, "La cadena '00011' debería ser rechazada")
        print(f"Prueba '00011': {'Aceptada' if resultado else 'Rechazada'}")

if __name__ == '__main__':
    unittest.main(verbosity=2)