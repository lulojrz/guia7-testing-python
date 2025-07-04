import unittest
from ejercicios import resultado_materia,saldoActual, pertenece_a_cadauno_1,es_matriz,filas_ordenadas,columna,columnas_ordenadas,transponer,quien_gana_tateti
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


class tests_pertenece_a_cadauno1(unittest.TestCase):
    def test_pertenece_a_cadauno1(self):
        resultado_esperado = [True,True,False]
        self.assertEqual(pertenece_a_cadauno_1([[1,2],[1,3],[5,4]],1),resultado_esperado)

    def test_pertenece_a_cadauno_1_vacio(self):
        self.assertEqual(pertenece_a_cadauno_1([],1),[]) 

class test_es_matriz(unittest.TestCase):
    def test_es_matriz_listas_mismos_n_elementos(self):
        self.assertTrue(es_matriz([[1,2],[6,7],[98,0]]))
    def test_es_matriz_listas_distintos_n_elementos(self):
        self.assertFalse(es_matriz([[1,2],[1]]))
        
    def test_matriz_vacia(self):
        self.assertFalse(es_matriz([[]]))
        
class test_filas_ordenadas(unittest.TestCase):
    def test_filas_ordenadas_correcto(self):
        resultado_esperado= [True,False]
        self.assertEqual(filas_ordenadas([[1,2],[2,0]]),resultado_esperado)
        
    def test_filas_ordenadas_vacio(self):
        resultado_esperado = []
        self.assertEqual(filas_ordenadas([[]]),resultado_esperado)


class test_columna(unittest.TestCase):
    def test_columna_matriz_vacia(self):
        resultado_esperado = []
        self.assertEqual(columna([[]],1),resultado_esperado)
    def test_columna_esperado(self):
        resultado_esperado= [1,3,1]
        self.assertEqual(columna([[1,2],[3,4],[1,1]],0),resultado_esperado)
    def test_columna_parametro_mal(self):
        resultado_esperado = []
        self.assertEqual(columna([[1,2],[1,1]],6),resultado_esperado)
        
class test_columnas_ordenadas(unittest.TestCase):
    def test_columnas_correcto(self):
        resultado_esperado = [True,False]
        self.assertEqual(columnas_ordenadas([[1,2],[2,1]]),resultado_esperado)
        
    def test_columnas_vacio(self):
        resultado_esperado=[]
        self.assertEqual(columnas_ordenadas([[]]),resultado_esperado)
        
class test_transponer(unittest.TestCase):
    def test_traspueta_correcta(self):
        resultado_esperado=[[1,5,9],[2,6,10],[3,8,11]]
        self.assertEqual(transponer([[1,2,3],[5,6,8],[9,10,11]]),resultado_esperado)
        
    def test_traspuesta_matriz_incorrecta(self):
        resultado = []
        self.assertEqual(transponer([[1,2],[3,5,6]]),resultado)
        

        
class test_tateti(unittest.TestCase):
    def test_tateti_diagonal_1(self):
        resultado_esperado=0
        self.assertEqual(quien_gana_tateti([["X","X","O"],
                                            ["X","O","X"],
                                            ["O","O","X"]]),resultado_esperado)
        
    def test_tateti_diagonal_2(self):
        resultado_esperado = 1
        self.assertEqual(quien_gana_tateti([["X","X","O"],
                                            ["O","X","X"],
                                            ["O","O","X"]]),resultado_esperado)
        
    def test_tateti_vertical_X(self):
        resultado_esperado = 1
        self.assertEqual(quien_gana_tateti([["X","X","O"],
                                            ["O","X","X"],
                                            ["O","X","O"]]),resultado_esperado)
        
    def test_tateti_vertical_Y(self):
        resultado_esperado = 0
        self.assertEqual(quien_gana_tateti([["O","X","O"],
                                            ["O","X","X"],
                                            ["O","O","X"]]),resultado_esperado)
        
    def test_tateti_hor_X(self):
        resultado_esperado = 1
        self.assertEqual(quien_gana_tateti([["O","X","O"],
                                            ["X","X","X"],
                                            ["X","O","O"]]),resultado_esperado)
        
    def test_tateti_hor_Y(self):
        resultado_esperado = 0
        self.assertEqual(quien_gana_tateti([["O","X","X"],
                                            ["X","O","X"],
                                            ["O","O","O"]]),resultado_esperado)
    def test_tateti_ningunganador(self):
        resultado_esperado = 2
        self.assertEqual(quien_gana_tateti([["O","X","O"],
                                            ["X","O","X"],
                                            ["X","O","X"]]),resultado_esperado)
       


        
        
if __name__ == '__main__':
    unittest.main(verbosity=2)
