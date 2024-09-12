def multi (a,b):
    return a*b

#print("El resultado es de: ",multi(3,2))

def Contra(pas):
    mayus=0
    for letra in pas:
        if(letra.isupper()):
            mayus+=1
    return mayus

usuario=input("Ingrese su Usuario: ")
while True:
    contra=input("Ingrese su Contraseña: ")

    if(Contra(contra)>=2):
        print("La contraseña es valida")
        break
    else:
        print("La contraseña es invalida")

print(usuario,contra)