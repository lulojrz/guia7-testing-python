from typing import List
#ejercicio 1a
def pertenece_1 (x:List[int], y:int) -> bool:
    
    afirmacion :bool = False 
    for elemento in x:
        if elemento == y:
            afirmacion = True
            
    return afirmacion

def pertenece_2(x:List[int],y:int) -> bool:
    afirmacion: bool = False
    for num in range(0,len(x)):
        if x[num] == y:
            afirmacion = True
    
    return afirmacion
            
def pertenece_3(x:List[int],y:int)  -> bool:
    inicio:int = 0
    afirmacion:bool= False
    while inicio < len(x):
        if x[inicio] == y :
            afirmacion=True
        
        inicio+=1
     
    return afirmacion 
     
#ejercicio 1b
def divide_a_todos(x:List[int],y:int)-> bool:
    afirmacion:bool= False
    for elemento in x:
        if elemento % y == 0:
            afirmacion = True
        else:
            afirmacion = False
            break
        
    return afirmacion

#ejercicio 1c
def suma_total(x:List[int])-> int:
    contador:int = 0
    for elemento in x :
        contador+= elemento
        
    return contador

#ejercicio 1d
def maximo(x:List[int])-> int:
    if not x:
        return None
    
    max:int= x[0]
    for num in range(1,len(x)):
        if x[num] > max:
            max = x[num]
            
    return max


#ejercicio 1e
def minimo(x:List[int])-> int:
    if not x:
        return None
    
    min:int= x[0]
    for num in range(1,len(x)):
        if x[num] < min:
            min = x[num]
            
    return min

#ejercicio 1f
def ordenados(x:List[int])-> bool:
    afirmacion: bool = False
    if not x :
        afirmacion = False
        
    else:
     primero:int = x[0]

     for num in range(1,len(x)):
      if primero  > x[num]: 
        afirmacion = False
        break
     else:
       primero = x[num]  
       afirmacion=True
    
    return afirmacion
 
#ejercicio 1g
def pos_maximo(x:List[int])-> int:
    if (x):
     maximo_num =  maximo(x)
     pos_max = x.index(maximo_num)
     return pos_max
    else:
        return -1


#ejercicio 1h
def pos_minimo(x:List[int])-> int:
    if (x):
     minimo_num =  minimo(x)
     pos_max = x.index(minimo_num)
     return pos_max
    else:
        return -1
    
#ejercicio 1i
def long_mayoraSiete(x:List[str])-> int:
    afirmacion =  False
    if (x):
        for elemento in x :
            if len(elemento)>7:
                afirmacion = True
                break
    else : 
      afirmacion = False
        
   
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
    else : 
        afirmacion = True
        
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
             return True    
       else:
           return False
           
    else :
        return False
        
    
    return afirmacion
        
        
#ejercicio m 
def vocalesDistintas(x:str) -> bool:
    vocales:list[int] = ["a","b","c","d","e","f"]
    contador = 0
    if (x):
     for letra in x:
        if letra in vocales:
            contador+= 1
    else :
        return False
            
    if contador>= 3:
        return True
    else: 
        return False
    
    #ejercicio n

#ejercicio q
def cantidad_digitos_impares(x:list[int])-> int:
    contador = 0
    if x: 
    
     for num in x:
        for digito in str(num):
            if int(digito) % 2 != 0:
                contador+=1
                
     return contador
    else :
        return contador
    


#ejercicio 2.1
#es como el 2.2 pero no devuelve nada, ya que es un procedimiento
lista=[1,2,3,1,9]
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

                
     return contador
    else :
        return contador
            
        
