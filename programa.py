c = int(input("Ingrese el capital: "))

rta = 0
m = c*2

while c<=m :
    c = c*0.05+c
    rta = rta+1
    print ("para el mes "+ str(rta) + " el valor es: " +str(c))

print (rta)