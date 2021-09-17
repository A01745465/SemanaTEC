import random#Paqueteria usada para dar soluciones aleatorias al acertijo 

Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz']
#variable A con la lista de los nombres de los personajes
#Las listas sirven para almacenar los datos 
Lado_B = []
#variable b con lista vacia 
Path = []
#variable path con lista vacia  

def seleccion(L):
  #primera funcion de codigo que se encanga de la seleccion de un numero aleatoreo entero, con parametro L
    op = random.randint(0,len(L)-1)#Devuelve un entero aleatorio N tal que a <= N <= b. Alias ​​de rango aleatorio (a, b + 1).
    return (L[op]) #regresa L

def Viaje(F, D):
  #funcion viaje con los paramentros F y D que se encargara de remover algunos elementos de la lista principal 
    p1 = seleccion(F)
    #print ('Selección -> ', p1)
    if p1 != 'Granjero':
      #ciclo if para el mejor manejo de remove 
        F.remove(p1) #busca entre los elementos para eliminar el elemento del granjero en la lista 
        D.append(p1) #añade al final de la lista lo que se desea 

    F.remove('Granjero')
    D.append('Granjero')
    #print (F)
    #print (D)
    return ('Granjero',p1) #Regresa en la variable Granjero

def valida_estado(L):  #Funcion con parametro L en donde se encuenta el ciclo if 
    if 'Maiz' in L and 'Ganzo' in L and len(L) == 2: #Ciclo if que busca un elemnto en el rango L 
        return False #sino se cumple se vuelve a correr el ciclo 
    elif 'Zorro' in L and 'Ganzo' in L and len(L) == 2:
      #segunda alternativa del codigo ahora con los elemnetos de la lista restantes 
        return False#sino se cumple se vuelve a correr el ciclo 
    return True#si alguno se cumple se cierra ciclo 
  
def reiniciar_sistema():
  #funcion de reiniciar sistema 
    global Lado_A, Lado_B, Path #Se utiliza para declarar variables como variables globales, a las que se puede acceder desde cualquier parte del programa. 
    Lado_A = ['Granjero', 'Zorro', 'Ganzo', 'Maiz'] #Lista A
    Lado_B = []#lista b
    Path = []#lista path
    
def HCR(): #
    F = Lado_A
    D = Lado_B
    while len(Lado_B) != 4:
        p1, p2 = Viaje(F, D)
        if valida_estado (F) and valida_estado (D):
            #print ('Estado valido, continuamos')
            if F == Lado_A:
                Path.append('A->B :')
            else:
                Path.append('B->A :')
            Path.append(p1)
            Path.append(p2)
            
            Temp = F
            F = D
            D = Temp      
        else:
            #print ('Estado inválido, REINICIO DEL SISTE;A')
            reiniciar_sistema()
            F = Lado_A
            D = Lado_B
    return (Path)

def main():
    P = HCR()
    while len(P) > 22:
        reiniciar_sistema()
        print ('\nBuscando una mejor solución, Longitud del Path', len(P))
        P = HCR()
    print (P)
    print (len(P))
            
main()
