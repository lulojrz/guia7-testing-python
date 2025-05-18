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

