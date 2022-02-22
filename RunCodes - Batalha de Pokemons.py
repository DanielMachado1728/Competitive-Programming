dpok = {}
while True:
  pokemon = input().replace("\n","").replace("\r","")
  if pokemon == 'fimlista':
    break
  pokemon = pokemon.split(':')
  pokemon[1] = int(pokemon[1])
  dpok[pokemon[0]] = pokemon[1]
while True:
  nomes = input().replace("\n","").replace("\r","")
  if nomes == 'fimbatalhas':
    break
  nomes = nomes.split('X')
  poder1 = dpok[nomes[0]]
  poder2 = dpok[nomes[1]]
  if poder1 > poder2:
    print(nomes[0])
  elif poder1 < poder2:
    print(nomes[1])
  else:
    print("empate")
