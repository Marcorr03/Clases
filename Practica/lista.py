
lista=["Marco","Luis","Tamara"]
lista2=[1,2,7,2,4]

#Imprimir los nombres que contengan la letra s
for nombre in lista:
    for letra in nombre:
        #if(letra.lower()=="s"):
        if(letra=="s"or letra=="S"):
            print(nombre)

#Imprimir la primer letra de cada nombre
for nombre in lista:
    print(nombre[0])

#Contra cuantas letras minisculastiene cada nombre
for nombre in lista:
    cont=0
    for letra in nombre:
        if(letra.islower()):
            cont+=1
    print(cont)

#Verficar si son letras, 
nombre="2s"
if(nombre.isalpha()):
    print("Son letras")
elif(nombre.isdigit()):
    print("Son numeros")
elif(nombre.isalnum()):
    print("Son letras y numeros")


for nombre in lista:
    for letra in reversed(nombre):
        print(letra,end="")
    print()


#for numero in lista2:
#    print(numero)           