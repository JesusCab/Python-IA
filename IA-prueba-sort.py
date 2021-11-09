"""T = input("Introduce un Texto a Evaluar: ")"""
T=("El dolor y el sufrimiento van necesariamente unidos a un gran corazon y a una elevada inteligencia")
print(T)
print("Total de Caracteres:",len(T),"\n")

Diccionario={}

for l in T:
    if l in Diccionario:
        Diccionario[l]=Diccionario[l]+1
    else:   Diccionario[l]=1
print( "Resultados('caracter','cantidad'):\n" ,Diccionario )        
    
x=[4,1,2,3]
x.sort()
x.sort(reverse=True)
y=sorted(x)
print(x)


Diccionario2=sorted(Diccionario.items()     
    ,key=lambda s: s[1],
    reverse=True)

print( "Resultados despues ordenamiento('caracter','cantidad'):\n" ,Diccionario2 )        

print("Presione Enter para finalizar")
input()
        
        