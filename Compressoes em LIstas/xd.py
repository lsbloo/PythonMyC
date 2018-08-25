#Compreensoes de lista

#Alimenta uma lista com numeros pares de uma a 10;
xd = [ x for x in range(10) if x %2 == 0 ]
print(xd)

se1t = { x: x * x for x in range(10)}
print(se1t)

import random

random_uniformes = [random.random() for _ in range(4)]

print(random_uniformes)

random_form = [ random.randrange(3,6) ]
print(random_form)
