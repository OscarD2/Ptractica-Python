import random
print("Bienvenido!!")
numero_intentos = 0
minnumber = 1
maxnumber = 50
nombre = input("Dígame su nombre: ")
numero = random.randint( minnumber,maxnumber)

print("Comencemos a jugar, " + nombre + '. Estoy pensando en un numero entre ' + str(minnumber) + ' y '+ str(maxnumber))

while numero_intentos < 5:
    prediccion = input("Inserta tu numero: ")
    prediccion = int(prediccion)

    numero_intentos = numero_intentos + 1  
    
    if prediccion < numero:
        print("Tu numero es muy bajo")
    if prediccion > numero:
        print("Tu numero es muy alto")
    if prediccion == numero:
        break

if prediccion == numero:
    numero_intentos = str(numero_intentos)
    print("Felicidades " + nombre +  ', adivinaste el numero en ' + numero_intentos + " intentos")
if prediccion != numero:
    numero = str(numero)
    print("No. El numero que estaba pensando era " + numero)

