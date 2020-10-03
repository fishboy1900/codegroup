class InvalidInput(Exception):
	pass

class InvalidPlay(Exception):
	pass

'''j_1 = input("Coordenadas: ")
if len(j_1) == 3 and int(j_1[0]) >= 0 and int(j_1[2]) <= 2:
      print("OK")
      print(int(j_1[0]))
else:
      print("bosta")'''

X = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(9):
      j_1 = input('Jogador 1 (x,y): ')
      try:
            if len(j_1) == 3 and int(j_1[0]) >= 0 and int(j_1[2]) <= 2:
                  print("Chegou aqui 1")
                  X[int(j_1[0])][int(j_1[2])] = 1
                  print(X)
            
            else:
                  raise InvalidInput 

      except:
            raise InvalidInput
      
