import unittest
from python2 import resultado_materia,saldoActual, pertenece_a_cadauno_1
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
        

        
        

        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
