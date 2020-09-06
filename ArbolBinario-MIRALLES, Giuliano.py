#             Matias
#            /      \  
#        Alfonso   Marcio
#         /        /   \
#      Mario  Eduardo   Francisco
#      /  \               /    \        
# Santiago Kevin      Franco   Agustin
#

class Nodo:                         
    def __init__(self,dato): 
        self.izquierda = None
        self.derecha = None
        self.val = dato 

def Arbol_inorden(raiz): 
    if raiz: 
        Arbol_inorden(raiz.izquierda) 
        print(raiz.val), 
        Arbol_inorden(raiz.derecha) 

def Arbol_preorden(raiz): 
    if raiz: 
        print(raiz.val), 
        Arbol_preorden(raiz.izquierda) 
        Arbol_preorden(raiz.derecha) 

def Arbol_postorden(raiz): 
    if raiz: 
        Arbol_postorden(raiz.izquierda) 
        Arbol_postorden(raiz.derecha)   
        print(raiz.val), 
        
raiz = Nodo('Matias')  #Nodo padre
raiz.izquierda = Nodo('Alfonso')  #Nodo hijo izquierdo
raiz.derecha = Nodo('Marcio')     #Nodo hijo Derecho
raiz.izquierda.izquierda = Nodo('Mario')  #Nodo nieto izquierdo
raiz.izquierda.izquierda.izquierda = Nodo('Santiago') # Todo viz nieto izquierdo
raiz.izquierda.izquierda.derecha = Nodo('Kevin')  # Nodo viz nieto Derecho
raiz.derecha.izquierda = Nodo('Eduardo')  # Nodo nieto izquierdo
raiz.derecha.derecha= Nodo('Francisco') # Nodo nieto derecho
raiz.derecha.derecha.derecha= Nodo('Agustin')  # Nodo viz nieto derecho
raiz.derecha.derecha.izquierda= Nodo('Franco') #Nodo viz nieto izquierdo


#Pinteo en consola
print ("..::Arbol ordenado en  forma Inorden::..")
Arbol_inorden(raiz)
print ("-------------------------")

print ("..::Arbol ordenado en forma  Preorden::..")
Arbol_preorden(raiz) 

print ("-------------------------")

print ("..::Arbol ordenado en forma Postorden::..")
Arbol_postorden(raiz) 

