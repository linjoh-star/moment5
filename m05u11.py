# Öppna filen "utskrift.txt" i ett skriv läge

with open('utskrift.txt', 'w') as fw:
  # Skriv en sträng med tre rader i filen
  fw.write('''1 2 3
4 5 6
7 8 9
''')
  # Skriv en till rad med denna text i filen
  fw.write('\nHär var det rutigt!')

# Öppna filen "utskrift.txt" i "read"-läge
# Detta innebär att vi kan läsa från filen
with open('utskrift.txt', 'r') as fr:
  # Skriv ut innehållet i filen
  print(fr.read())



#Det som skrivs är
# 1 2 3
# 4 5 6
# 7 8 9

#Här var det rutigt!