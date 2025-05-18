import unittest
from guia7 import pertenece_1,pertenece_2,pertenece_3,divide_a_todos,suma_total

class test_pertenece1(unittest.TestCase):
    def test_pertenece1(self):
        resultado_esperado = True
        self.assertTrue(pertenece_1([1,2,3],1),resultado_esperado)
        
    def test_nopertenece1(self):
        resultado_esperado = False
        self.assertFalse(pertenece_1([1,2,3],4),resultado_esperado)
    
    def test_listavacia1(self):
        resultado_esperado = False
        self.assertFalse(pertenece_1([],1),resultado_esperado)

class test_pertenece2(unittest.TestCase):
    def test_pertenece2(self):
        resultado_esperado = True
        self.assertTrue(pertenece_2([1,2,3],1),resultado_esperado)
        
    def test_nopertenece2(self):
        resultado_esperado = False
        self.assertFalse(pertenece_2([1,2,3],4),resultado_esperado)
    
    def test_listavacia2(self):
        resultado_esperado = False
        self.assertFalse(pertenece_2([],1),resultado_esperado)
        
class test_pertenece3(unittest.TestCase):
   def test_pertenece3(self):
        resultado_esperado = True
        self.assertTrue(pertenece_3([-1,2,3],-1),resultado_esperado)
        
   def test_nopertenece3(self):
        resultado_esperado = False
        self.assertFalse(pertenece_3([1,2,3],4),resultado_esperado)
    
   def test_listavacia3(self):
        resultado_esperado = False
        self.assertFalse(pertenece_3([],1),resultado_esperado)
        
class divide(unittest.TestCase):
    def test_divideatodos(self):
        resultado_esperado= True
        self.assertTrue(divide_a_todos([2,4,6],2),resultado_esperado)
        
    def test_nodivideatodos(self):
        resultado_esperado = False
        self.assertFalse(divide_a_todos([2,4,6],3),resultado_esperado)
    
    def test_listavaciaendivide(self):
        resultado_esperado= False
        self.assertFalse(divide_a_todos([],2),resultado_esperado)


class suma(unittest.TestCase):
    def test_suma_esperada(self):
        resultado_esperado = 2
        self.assertEqual(suma_total([-2,2,2]),resultado_esperado)
    
    def test_sumaincorrecta(self):
        resultado_esperado = 6
        self.assertNotEqual(suma_total([1,1,1]),resultado_esperado)

if __name__ == '__main__':
    unittest.main(verbosity=2)