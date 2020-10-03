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
      print(X)
      j_1 = input('Jogador 1 (x,y): ')
      try:
            if len(j_1) == 3 and int(j_1[0]) >= 0 and int(j_1[2]) <= 2:
                  if X[int(j_1[0])][int(j_1[2])] == 0:
                        X[int(j_1[0])][int(j_1[2])] = 1
                        print(X)
                  
                  else:
                        raise InvalidPlay

            else:
                  raise InvalidInput 

      except:
            raise InvalidInput

      j_2 = input('Jogador 2 (x,y): ')

      try:
            if len(j_2) == 3 and int(j_2[0]) >= 0 and int(j_2[2]) <= 2:
                  if X[int(j_2[0])][int(j_2[2])] == 0:
                        X[int(j_2[0])][int(j_2[2])] = 2
                        print(X, "\n",'=================================')
                  
                  else:
                        raise InvalidPlay

            else:
                  raise InvalidInput 

      except:
            raise InvalidInput
      
