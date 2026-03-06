partidos = int(input("Ingrese la cantidad de partidos a jugar: "))
pg = 0
pe = 0
pp = 0
gf = 0
gc = 0
pj = 0
puntosVictoria = 0
puntosEmpate = 0
puntosDerrota = 0
puntosTotal = 0

for i in range(1, partidos + 1):
    marcadorJunior = int(input(f"Fecha n{i}. Ingrese los goles del local (Junior): "))
    marcadorVisitante = int(input(f"Fecha n{i}. Ingrese los goles del visitante (Contrincante): "))
    print(f"Resultado fecha {i}: {marcadorJunior}-{marcadorVisitante}\n")
    gf += marcadorJunior
    gc += marcadorVisitante

    if marcadorJunior > marcadorVisitante:
        pj += 1
        pg += 1
        puntosVictoria += 3

    elif marcadorJunior == marcadorVisitante:
        pj += 1
        pe += 1
        puntosEmpate += 1

    else:
        pj += 1
        pp += 1
        puntosDerrota += 0

puntosTotal += puntosVictoria + puntosEmpate + puntosDerrota

print("_______________________________________________________________________")
print("Equipo   | PJ   |  PG  |  PE  |  PP  |  GF  |  GC  |  DG   |  Puntos |")
print(f"Junior   | {pj}    |  {pg}   |   {pe}  |   {pp}  |  {gf}   |   {gc}  |  {gf - gc}   |    {puntosTotal}    |")



















# texto = input("Ingrese un texto: ")

# texto_invertido = (texto).lower()

# if texto == texto_invertido[::-1]:
#     print("Es palindromo")
# else:
#     print("No es palindromo")































































































