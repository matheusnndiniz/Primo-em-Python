resultado = int(input ("Informe um número aleatório:"))
const1 = 1
const2 = 0

while const1 <= resultado:
    if resultado % const1 == 0:
        const2 += 1
    const1 += 1

if const2 == 2:
    print("Este número é primo")
elif resultado == 0: 
    print ("Esse número nem é número")
else:
    print("Este número não é primo")


    