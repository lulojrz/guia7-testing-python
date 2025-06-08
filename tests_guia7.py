import unittest
from ejercicios import pertenece_1,pertenece_2,pertenece_3,divide_a_todos,suma_total, maximo,minimo,ordenados, pos_maximo,pos_minimo, long_mayoraSiete,esPalindroma,iguales_consecutivos, vocalesDistintas, cantidad_digitos_impares, ceroPosicionesPares2, sin_vocales,reemplazar_vocales,eliminar_repetidos,da_vuelta_str, inflacion_anual, pos_secuencia_ordenada_mas_larga, ceroPosicionesPares
class test_pertenece1(unittest.TestCase):
    def test_pertenece1(self):
        self.assertTrue(pertenece_1([3,1,2],1))
        
    def test_nopertenece1(self):
        self.assertFalse(pertenece_1([1,2,3],4))
    
    def test_listavacia1(self):
        self.assertFalse(pertenece_1([],1))

class test_pertenece2(unittest.TestCase):
    def test_pertenece2(self):
        self.assertTrue(pertenece_2([0,1,3],1))
        
    def test_nopertenece2(self):
        self.assertFalse(pertenece_2([1,2,3],4))
    
    def test_listavacia2(self):
        self.assertFalse(pertenece_2([],1))
        
class test_pertenece3(unittest.TestCase):
   def test_pertenece3(self):
        self.assertTrue(pertenece_3([-1,2,3],-1))
        
   def test_nopertenece3(self):
        self.assertFalse(pertenece_3([1,2,3],4))
    
   def test_listavacia3(self):
        self.assertFalse(pertenece_3([],1))
        
class test_divide(unittest.TestCase):
    def test_divideatodos(self):
        self.assertTrue(divide_a_todos([2,4,6],2))
        
    def test_nodivideatodos(self):
        self.assertFalse(divide_a_todos([2,4,6],3))
    
    def test_listavaciaendivide(self):
        self.assertFalse(divide_a_todos([],2))

class tests_suma(unittest.TestCase):
    def test_suma_esperada(self):
        resultado_esperado = 2
        self.assertEqual(suma_total([-2,2,2]),resultado_esperado)
    
    def test_sumaincorrecta(self):
        resultado_esperado = 6
        self.assertNotEqual(suma_total([1,1,1]),resultado_esperado)
    def test_suma_total_lista_vacia(self):
        self.assertEqual(suma_total([]),0)
        
class tests_maximo(unittest.TestCase):
    def test_maximo_esperado(self):
        resultado_esperado = 89
        self.assertEqual(maximo([5,89,2]),resultado_esperado)
        
    def test_maximo_vacio(self):
        resultado_esperado = None
        self.assertEqual(maximo([]),resultado_esperado)
        
    
class tests_minimo(unittest.TestCase):
    def test_minimo_esperado(self):
        resultado_esperado = 2
        self.assertEqual(minimo([3,2,20]),resultado_esperado)
        
    def test_minimo_vacio(self):
        resultado_esperado = None
        self.assertEqual(minimo([]),resultado_esperado)
        
class tests_ordenados(unittest.TestCase):
    def test_ordenados_true(self):
        self.assertTrue(ordenados([1,2,3]))
        
    def test_ordenados_false(self):
        self.assertFalse(ordenados([3,2,45]))
        
    def test_ordenados_iguales(self):
        self.assertTrue(ordenados([1,1,1]))
        
    def test_ordenados_vacio(self):
        self.assertFalse(ordenados([])) 
        
class tests_maximo_posicion(unittest.TestCase):
    def test_maximo_posicion_esperado_correcto(self):
        resultado_esperado = 2
        self.assertEqual(pos_maximo([1,2,3]), resultado_esperado)
        
    def test_maximo_posicion_vacio(self):
        resultado_esperado = -1
        self.assertEqual(pos_maximo([]),resultado_esperado)
        
    def test_maximo_posicion_iguales(self):
        resultado_esperado = 0
        self.assertEqual(pos_maximo([1,1,1]),resultado_esperado)
        
class tests_minimo_posicion(unittest.TestCase):
    def test_minimo_posicion_esperado_correcto(self):
      resultado_esperado = 2
      self.assertEqual(pos_minimo([3,2,1]), resultado_esperado)
      
    def test_minimo_posicion_vacio(self):
        resultado_esperado = -1
        self.assertEqual(pos_minimo([]),resultado_esperado)
        
    def test_minimo_posicion_iguales(self):
        resultado_esperado = 0
        self.assertEqual(pos_minimo([1,1,1]),resultado_esperado)
        
class tests_longitud(unittest.TestCase):
    def test_longitud_mayorSiete(self):
        self.assertTrue(long_mayoraSiete(["pepe","sebastian"]))
        
    def test_longitud_menorSiete(self):
        self.assertFalse(long_mayoraSiete(["pepe","gato"]))
        
    def test_longitud_vacio(self):
        self.assertFalse(long_mayoraSiete([])) 
        
class tests_palindroma(unittest.TestCase):
    def test_palindromo_correcto(self):
        self.assertTrue(esPalindroma("oro"))
    
    def test_palindromo_incorrecto(self):
        self.assertFalse(esPalindroma("luca"))
        
    def test_palindromo_caracter(self):
        self.assertTrue(esPalindroma("a"))
     
    def test_palindromo_vacio(self):
        self.assertTrue(esPalindroma(""))
        
class tests_iguales_consecutivos(unittest.TestCase):
    def test_tres_consecutivos_correcto(self):
        self.assertTrue(iguales_consecutivos([2,3,1,1,1]))
        
    def test_ningun_consecutivo(self):
        self.assertFalse(iguales_consecutivos([2,4,5,6,7]))
        
    def test_consecutivos_lista_vacia(self):
        self.assertFalse(iguales_consecutivos([]))
    
    def test_todos_consecutivos_iguales(self):
        self.assertTrue(iguales_consecutivos([1,1,1]))
        
    def test_mas_detres_consecutivosiguales(self):
        self.assertFalse(iguales_consecutivos([1,1,1,1,1,1]))
        
        
class test_vocales_distintas(unittest.TestCase):
    def test_3_vocales(self):
        self.assertTrue(vocalesDistintas("fabrizio"))
    def test_sin_vocales(self):
        self.assertFalse(vocalesDistintas("kjjjj"))
    def test_masde3_vocales(self):
        self.assertTrue(vocalesDistintas("murcielago"))
        
    def test_menosde3vocales(self):
        self.assertFalse(vocalesDistintas("ivana"))
        
    def test_sinvocales_vacio(self):
        self.assertFalse(vocalesDistintas(""))
        
class tests_pos_secuencia_ord_mas_larga(unittest.TestCase):
    def test_pos_ejemplo(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga( [3, 2, 2, 3, 4, 1, 2, 3]),1)      
     
    def test_lista_vacia(self):
        self.assertEqual(pos_secuencia_ordenada_mas_larga([]),-1)   
        
        
class test_digitos_impares(unittest.TestCase):
    def test_digitosimpares_correcto(self):
        resultado_esperado = 3
        self.assertEqual(cantidad_digitos_impares([12,12,10]),resultado_esperado)
        
    def test_digitosimpares_vacio(self):
        resultado_esperado = 0
        self.assertEqual(cantidad_digitos_impares([]),resultado_esperado)
   
class test_cero_posiciones_pares1(unittest.TestCase):
    def test_cero_posiciones_pares_ejemplo(self):
        lista = [1,2,3,4] 
        ceroPosicionesPares(lista)
        self.assertEqual(lista,[0,2,0,4])

   
class test_cero_posiciones_pares2(unittest.TestCase):
    def test_cero_posiciones_pares2_esperado(self):
        resultado_esperado= [0,1,0,3,0]
        self.assertEqual(ceroPosicionesPares2([1,1,1,1,1]),resultado_esperado)

    def test_cero_posiciones_pares2_vacio(self):
        resultado_esperado = []
        self.assertEqual(ceroPosicionesPares2([]),resultado_esperado)


class test_sin_vocales(unittest.TestCase):
    def test_sinvocales_nuevapalabra(self):
        resultado_esperado="btmn"
        self.assertEqual(sin_vocales("batman"),resultado_esperado)

    def test_no_saca_vocales(self):
        resultado_esperado = "pyth"
        self.assertEqual(sin_vocales("pyth"),resultado_esperado)

    def test_sin_vocales_vacio(self):
        resultado_esperado = ""
        self.assertEqual(sin_vocales(""),resultado_esperado)
            
class test_reemplazar_vocales(unittest.TestCase):
    def test_reemplazarvocalesCorrecto(self):
        resultado_esperado = "m-rc--l-g-"
        self.assertEqual(reemplazar_vocales("murcielago"),resultado_esperado)

    def test_noreemplaza_vocales(self):
        resultado_esperado="pyth"
        self.assertEqual(reemplazar_vocales("pyth"),resultado_esperado)

    def test_reemplaza_vocales_vacio(self):
        resultado_esperado= ""
        self.assertEqual(reemplazar_vocales(""),resultado_esperado)

class test_dar_vuelta(unittest.TestCase):
    def test_dar_vuelta_palindroma(self):
        resultado_esperado="otto"
        self.assertEqual(da_vuelta_str("otto"),resultado_esperado)

    def test_dar_vuelta_nopalindroma(self):
        resultado_esperado="acul"
        self.assertEqual(da_vuelta_str("luca"),resultado_esperado)
        
    def test_dar_vuelta_vacio(self):
        resultado_esperado=""
        self.assertEqual(da_vuelta_str(""),resultado_esperado)

class test_eliminarRepetidos(unittest.TestCase):
    def test_eliminarrepetidos_correcto(self):
        resultado_esperado="luvia"
        self.assertEqual(eliminar_repetidos("lluvia"),resultado_esperado)

    def test_sineliminarrepetidos(self):
        resultado_esperado="resultado"
        self.assertEqual(eliminar_repetidos("resultado"),resultado_esperado)

    def test_eliminarRepetidos_vacio(self):
        resultado_esperado=""
        self.assertEqual(eliminar_repetidos(""),resultado_esperado)



 
 
 
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
