# leer x cantidad numeros y decir cuantos son pares y cuantos son impares

suma_pares = 0
suma_impares = 0
numeros = []

while True:
    numero = int(input("Dime un número: "))
    numeros.append(numero)
    
    resp = input("¿Desea agregar otro? [S] si, [N] no: ").upper().strip()
    if resp.upper == 'N':
        False
        break

print(numeros)

cont = 0
while cont < len(numeros):
    numero = numeros[cont]
    if numero % 2 == 0:
        suma_pares += numero
    else:
        suma_impares += numero

print(f"Suma de pares: {suma_pares}")
print(f"Suma de impares: {suma_impares}")