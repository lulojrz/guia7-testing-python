
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
#ejercicio 5
