class InvalidInput(Exception):
	pass

class InvalidPlay(Exception):
	pass

def winner(X):
      win = ''
      # Horizontal case.
      for l in range(3):
            if X[l][0] == X[l][1] == X[l][2] == 1:
                  win = 'Vencedor: Jogador 1'

            elif X[l][0] == X[l][1] == X[l][2] == 2:
                  win = 'Vencedor: Jogador 2'

            else:
                  pass

      # Vertical case.
      for c in range(3):
            if X[0][c] == X[1][c] == X[2][c] == 1:
                  win = 'Vencedor: Jogador 1'

            elif X[0][c] == X[1][c] == X[2][c] == 2:
                  win = 'Vencedor: Jogador 2'

            else:
                  pass

      # Diagonal case.
      if X[0][0] == X[1][1] == X[2][2] == 1:
            win = 'Vencedor: Jogador 1'

      elif X[0][0] == X[1][1] == X[2][2] == 2:
            win = 'Vencedor: Jogador 2'

      else:
            pass

      return win

def main():

      X = [[0,0,0],[0,0,0],[0,0,0]]
      print(winner(X))
      for i in range(9):
            print(X)
            j_1 = input('Jogador 1 (x,y): ')
            try:
                  # Validating the input.
                  if len(j_1) == 3 and int(j_1[0]) >= 0 and int(j_1[2]) <= 2:
                        # Checking if the place is already filled.
                        if X[int(j_1[0])][int(j_1[2])] == 0:
                              # Marking the place for the player 1.
                              X[int(j_1[0])][int(j_1[2])] = 1
                              print(X)
                              # Checking if there is a winner.
                              if winner(X)[:8] == 'Vencedor':
                                    print(winner(X))
                                    break
                              else: 
                                    pass
                        
                        else:
                              raise InvalidPlay

                  else:
                        raise InvalidInput 

            except:
                  raise InvalidInput

            # Now, its second's player time.
            j_2 = input('Jogador 2 (x,y): ')

            try:
                  # Validating the input.
                  if len(j_2) == 3 and int(j_2[0]) >= 0 and int(j_2[2]) <= 2:
                        # Checking if the place is already filled.
                        if X[int(j_2[0])][int(j_2[2])] == 0:
                              # Marking the place for the player 2.
                              X[int(j_2[0])][int(j_2[2])] = 2
                              print(X)
                              # Checking if there is a winner.
                              if winner(X)[:8] == 'Vencedor':
                                    print(winner(X))
                                    break
                              else: 
                                    pass
                              print("\n", '=================================')
                        
                        else:
                              raise InvalidPlay

                  else:
                        raise InvalidInput 

            except:
                  raise InvalidInput
main()