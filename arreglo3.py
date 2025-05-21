edades = [18, 17, 17, 16, 20, 27, 19, 21]
print(edades)

# ordenar
edades.sort()
print(edades)

# ordenar de mayor a menor
edades.sort(reverse=True)
print(edades)

import statistics as st

# mostrar la media
media = st.mean(edades)
print(f"Media: {media}")

# mostrar la moda 
moda = st.mode(edades)
print(f"Moda: {moda}")
