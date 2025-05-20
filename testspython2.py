import unittest
from python2 import resultado_materia,saldoActual,esMatriz, pertenece_a_cadauno_1,filas_ordenadas
class test_resultado_materia(unittest.TestCase):
    def test_todo_desaprobado(self):
        resultado_esperado =3 
        self.assertEqual(resultado_materia([3,3,3]),resultado_esperado)
        
    def test_promedio_entre4y7_parciales_aprobados(self):
        resultado_esperado = 2
        self.assertEqual(resultado_materia([5,5,5]),resultado_esperado)
        
    def test_promedio_entre4y7_parcial_desaprobado(self):
        resultado_esperado = 3
        self.assertEqual(resultado_materia([7,7,1]),resultado_esperado)
        
    def test_promedio_mayora7(self):
        resultado_esperado = 1
        self.assertEqual(resultado_materia([8,8,8]),resultado_esperado)
    
    def test_promedio_mayora7_parcial_desaprobado(self):
        resultado_esperado = 3
        self.assertEqual(resultado_materia([10,10,1]),resultado_esperado)
        
class test_saldo_actual(unittest.TestCase):
    def test_saldo_actual(self):
        resultado_esperado= 1280
        self.assertEqual(saldoActual([("I",2000), ("R", 20),("R", 1000),("I", 300)] ),resultado_esperado)
        
    def test_saldo_actual_vacio(self):
        resultado_esperado=0
        self.assertEqual(saldoActual([]),resultado_esperado)
        

class test_matriz(unittest.TestCase):
    def test_matriz(self):
        resultado_esperado = True
        self.assertEqual(esMatriz([[1,2],[21,2]]),resultado_esperado)
        
    def test_matriz_sin_listas(self):
        resultado_esperado = False
        self.assertEqual(esMatriz([]),resultado_esperado)


class test_pertenece_a_cada_uno(unittest.TestCase):
    def test_pertenece_matriz_True(self):
        resultado_esperado = [True,True]
        self.assertEqual(pertenece_a_cadauno_1([[1,2],[2,1]],1),resultado_esperado)
        
    def test_pertenece_a1matriz(self):
        resultado_esperado = [True,False]
        self.assertEqual(pertenece_a_cadauno_1([[21,10],[2,1]],21),resultado_esperado)
        
        
    def test_pertenece_a_ninguna_matriz(self):
        resultado_esperado = [False,False]
        self.assertEqual(pertenece_a_cadauno_1([[10,10],[21,45]],1),resultado_esperado)
        
    def test_pertenece_a_matriz_lista_vacia(self):
        resultado_esperado = []
        self.assertEqual(pertenece_a_cadauno_1([],10),resultado_esperado)
        
        
class test_filas_ordenadas(unittest.TestCase):
    def test_fila_ordenadas_true(self):
        resultado_esperado = [True,True]
        self.assertEqual(filas_ordenadas([[1,2],[7,8]]),resultado_esperado)
        
    def test_fila_ordenadas_trueandfalse(self):
        resultado_esperado= [True,False]
        self.assertEqual(filas_ordenadas([[1,2],[10,5]]),resultado_esperado)
        
    def test_fila_ordenadas_false(self):
        resultado_esperado = [False,False,False,False]
        self.assertEqual(filas_ordenadas([[2,1],[9,0],[5,2],[79,34]]),resultado_esperado)
        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
