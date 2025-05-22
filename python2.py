def pertenece_1 (x:list[int], y:int) -> bool:
    
    afirmacion :bool = False 
    for elemento in x:
        if elemento == y:
            afirmacion = True
            
    return afirmacion

def ordenados(x:list[int])-> bool:
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



#ejercicio 3

def suma_total(x:list[int])-> int:
    contador:int = 0
    for elemento in x :
        contador+= elemento
        
    return contador

def resultado_materia(x:list[int])-> int:
    
    tamanio:int = len(x)
    resul:int = 0
    promedio:int = int(suma_total(x)/tamanio)
    desaprobados:int = 0
    notas_mayor_a_4:int = 0
    
    for nota in x :
        if nota >= 4:
            notas_mayor_a_4+=1
        else:
            desaprobados+=1
            
    if desaprobados==0 and notas_mayor_a_4 == tamanio:
        if promedio >= 7:
            resul = 1
        
        if promedio in range(4,7):
            resul = 2
    else :
        resul = 3
        
    return resul 
         
         

#ejercicio 4
def saldoActual(movimientos:list[(str,int)])->int:
    saldo = 0
    for movimiento in movimientos:
        if movimiento[0] =="R" or movimiento[0] =="r":
            saldo-=movimiento[1]
        else:
            saldo+=0
        
        if movimiento[0]=="I" or movimiento[0]=="i":
         saldo+= movimiento[1]
        else:
            saldo+= 0
         
    return saldo
        
#MATRICES
#ejercicio 5.1

def pertenece_a_cadauno_1(x:list[list[int]],y:int)->list[bool]:
    res: list[bool] = []
    for lista in x :
        if pertenece_1(lista,y) == True:
            res.append(True)
        else:
            res.append(False)
        
    return res
          

    


#ejercicio 6.1
def es_matriz(x:list[list[int]])-> bool:
   res:bool = False
   tamaño:int = len(x[0])
   for num in range(1,len(x)):
      if len(x[num])==tamaño:
         res=True
      else:
         res=False
         break
      
   return res




#ejercicio 6.2
def filas_ordenadas(x:list[list[int]]) ->[bool]:
    res:[bool] = []
    if es_matriz(x)==True:
     for lista in x:
        if ordenados(lista)==True:
            res.append(True)
        else:
            res.append(False)
    
            
    return res



#ejercicio 6.3
def columna(m:list[list[int]],c:int)-> list[int]:
   columna_c:list[int] = []
   tamaño:int= len(m[0])-1

   if c<= tamaño and es_matriz(m)==True:
      for lista in m:
         columna_c.append(lista[c])

   return columna_c


#ejercicio 6.4
def columnas_ordenadas(m:list[list[int]])-> list[bool]:
   res:list[bool] = []
   for columnita in range(len(m[0])):
      una_columna:list[int] = columna(m,columnita)
      esta_ordenada:bool = ordenados(una_columna)
      res.append(esta_ordenada)

   return res

      
#ejercicio 6.5
def transponer(m:list[list[int]])-> list[list[int]]:
    res: list[list[int]] = []
    tamaño:int = len(m[0])
    if es_matriz(m):
     for num in range(tamaño):
        fila = columna(m,num)
        res.append(fila)
        
    return res 
        
        
print(transponer([[1,2,3]
                ,[5,6,8],
                [9,10]]))



#funciones comodines
def es_matriz(x:list[list[int]])-> bool:
   res:bool = False
   tamaño:int = len(x[0])
   for num in range(1,len(x)):
      if len(x[num])==tamaño:
         res=True
      else:
         res=False
         break
      
   return res

def columna(m:list[list[int]],c:int)-> list[int]:
   columna_c:list[int] = []
   tamaño:int= len(m[0])-1

   if c<= tamaño and es_matriz(m)==True:
      for lista in m:
         columna_c.append(lista[c])

   return columna_c

def transponer(m:list[list[int]])-> list[list[int]]:
    res: list[list[int]] = []
    tamaño:int = len(m[0])
    if es_matriz(m):
     for num in range(tamaño):
        fila = columna(m,num)
        res.append(fila)
        
    return res 

#ejercicio 6.6

def analizarFilas(x:list[str])->int:
    resultado:int = 2
    if x == ["X","X","X"]:
        resultado = 1
    elif x == ["O","O","O"]:
        resultado = 0
    else :
        resultado =  2
        
    
    
    return resultado

def analizo_diagonal(x:list[list[str]])->int:
    
    resultado = 2
    primera_diagonal = [x[0][0],x[1][1],x[2][2]]
    segunda_diagonal = [x[0][2],x[1][1],x[2][0]]
    
    if primera_diagonal == ["X","X","X"] or segunda_diagonal ==["X","X","X"]:
        resultado = 1
    elif primera_diagonal == ["O","O","O"] or segunda_diagonal ==["O","O","O"]:
        resultado =0
    else: 
        resultado = 2
    
    return resultado
        

 

def quien_gana_tateti(x:list[list[str]])->int:
    res:int = 2
    if es_matriz(x):
        columnas = transponer(x)
        if analizo_diagonal(x) == 1 :
            res = 1
        elif analizo_diagonal(x) == 0:
            res = 0
        else: 
 
         for fila in x:
           res_hor = analizarFilas(fila)
           if res_hor == 1 or res_hor==0:
            res = res_hor
           else:
               
             for fila in columnas:
              res_ver= analizarFilas(fila)
              if res_ver == 1 or res_ver==0:
               res=res_ver
               break
               
         
       
       
      
   
       
    return res
        
        



