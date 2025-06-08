#ejercicio 1a
def pertenece_1 (x:list[int], y:int) -> bool:
    
    afirmacion :bool = False 
    for elemento in x:
        if elemento == y:
            afirmacion = True
            
    return afirmacion

def pertenece_2(x:list[int],y:int) -> bool:
    afirmacion: bool = False
    for num in range(0,len(x)):
        if x[num] == y:
            afirmacion = True
    
    return afirmacion
            
def pertenece_3(x:list[int],y:int)  -> bool:
    inicio:int = 0
    afirmacion:bool= False
    while inicio < len(x):
        if x[inicio] == y :
            afirmacion=True
        
        inicio+=1
     
    return afirmacion 
     
#ejercicio 1b
def divide_a_todos(x:list[int],y:int)-> bool:
    afirmacion:bool= True
    if x : 
     for elemento in x:
        if elemento % y != 0:
            afirmacion = False
            
    else : 
      return False
       
        
    return afirmacion

#ejercicio 1c
def suma_total(x:list[int])-> int:
    contador:int = 0
    for elemento in x :
        contador+= elemento
        
    return contador

#ejercicio 1d
def maximo(x:list[int])-> int:
    if not x:
      return None
    else :
      
    
     max:int= x[0]
     for num in range(1,len(x)):
        if x[num] > max:
            max = x[num]
            
    return max


#ejercicio 1e
def minimo(x:list[int])-> int:
    if not x:
        return None
    else:
    
     min:int= x[0]
     for num in range(1,len(x)):
        if x[num] < min:
            min = x[num]
            
    return min

#ejercicio 1f
def ordenados(x:list[int])-> bool:
    afirmacion: bool = True
    if not x :
      afirmacion = False
      return afirmacion    
    else:
     primero:int = x[0]
     for num in range(1,len(x)):
      if primero  <= x[num]: 
        primero = x[num]
        afirmacion = True
      else : 
        return  False
    
    return afirmacion
 
#ejercicio 1g
def pos_maximo(x:list[int])-> int:
    if x:
     maximo_num =  maximo(x)
     pos_max = x.index(maximo_num)
     return pos_max
    else:
      return -1


#ejercicio 1h
def pos_minimo(x:list[int])-> int:
    if x:
     minimo_num =  minimo(x)
     pos_max = x.index(minimo_num)
     return pos_max
    else:
       return -1
    
#ejercicio 1i
def long_mayoraSiete(x:list[str])-> int:
    afirmacion =  False
    if (x):
        for elemento in x :
            if len(elemento)>7:
                afirmacion = True
                return afirmacion
                
        
   
    return afirmacion 

#ejericio 1k
def esPalindroma(x:str)-> bool:
    afirmacion = True
    if x:
        reverso = ""
        for num in range(len(x)-1,-1,-1):
            reverso+= x[num]
            
        if x == reverso:
           afirmacion = True
        else:
            afirmacion = False
        
    return afirmacion


#ejercicio 1l
def  iguales_consecutivos(x:list[int])-> bool:
    afirmacion = False
    contador = 1
    if x  and (len(x)>= 3):
       for i in range (1,len(x)):
           if x[i] == x[i-1]:
               contador+=1
     
       if contador ==3 :
          afirmacion = True   

        
    return afirmacion
        
        
#ejercicio m 
def vocalesDistintas(x:str) -> bool:
  vocales:list[int] = ["a","e","i","o","u" ]
  contador = 0
  afirmacion = False
  vocales_usadas=[]
  if x:
     for letra in x:
        if letra in vocales and letra not in vocales_usadas:
            vocales_usadas.append(letra)
            contador+= 1
   
     if contador>= 3 :
      afirmacion = True


  return afirmacion


#ejercicio n
def pos_secuencia_ordenada_mas_larga(x: list[int]) -> int:
    if len(x) == 0:
        return -1  # O manejar error

    inicio_maximo = 0
    longitud_maxima = 1

    inicio_actual = 0
    longitud_actual = 1

    for i in range(1, len(x)):
        if x[i] >= x[i - 1]:
            longitud_actual += 1
        else:
            if longitud_actual > longitud_maxima:
                longitud_maxima = longitud_actual
                inicio_maximo = inicio_actual
            inicio_actual = i
            longitud_actual = 1

    # Verificar si la última subsecuencia fue la más larga
    if longitud_actual > longitud_maxima:
        inicio_maximo = inicio_actual

    return inicio_maximo





#ejercicio q
def cantidad_digitos_impares(x:list[int])-> int:
    contador = 0
    if x: 
    
     for num in x:
        for digito in str(num):
            if int(digito) % 2 != 0:
                contador+=1
                
    return contador

    


#ejercicio 2.1
#es como el 2.2 pero no devuelve nada, ya que es un procedimiento
def ceroPosicionesPares(lista:list[int]):
    for num in range(0,len(lista)):
        if num%2==0:
            lista[num]=0


#ejercicio 2.2

def ceroPosicionesPares2(x:list[int])-> list[int]:
    nueva_lista=[]
    for num in range(0,len(x)):
        if num%2==0:
            nueva_lista.append(0)

        else :
            nueva_lista.append(num)

    return nueva_lista





# ejercicio 2.3
def sin_vocales(x:str) -> str:
    vocales = ["a","e","i","o","u"]
    nueva_cadena= ""
    for letra in x:
        if letra not in vocales:
            nueva_cadena+=letra

    return nueva_cadena

#ejercicio 2.4
def reemplazar_vocales(x:str) -> str:
    vocales = ["a","e","i","o","u"]
    nueva_cadena= ""
    for letra in x:
        if letra in vocales :
            nueva_cadena+="-"
        else:
            nueva_cadena+=letra

    return nueva_cadena


#ejercicio 2.5
def da_vuelta_str(x:str)-> str:
    nueva_cadena=""
    if esPalindroma(x)==True:
       nueva_cadena=x

    else:
        for num in range(len(x)-1,-1,-1):
            nueva_cadena+=x[num]


    return nueva_cadena



#ejercicio 2.6
def eliminar_repetidos(x:str)-> str:
    nueva_cadena=""
    for letra in x:
        if letra not in nueva_cadena:
            nueva_cadena+=letra

    return nueva_cadena



#ejercicio inflacion anual
def inflacion_anual(x:list[float])-> float:
    acumulador:float= 1
    for mes in x:
        acumulador*= 1+ (mes/100)


    return (acumulador-1)*100

                
 
