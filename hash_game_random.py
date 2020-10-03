class InvalidInput(Exception):
	pass

class InvalidPlay(Exception):
	pass

def winner(X):
      win = 'N'
      # Horizontal case.
      for l in range(3):
            if X[l][0] == X[l][1] == X[l][2] == 1:
                  win = 'V1'

            elif X[l][0] == X[l][1] == X[l][2] == 2:
                  win = 'V2'

            else:
                  pass

      # Vertical case.
      for c in range(3):
            if X[0][c] == X[1][c] == X[2][c] == 1:
                  win = 'V1'

            elif X[0][c] == X[1][c] == X[2][c] == 2:
                  win = 'V2'

            else:
                  pass

      # Diagonal cases.
      if X[0][0] == X[1][1] == X[2][2] == 1:
            win = 'V1'

      elif X[0][0] == X[1][1] == X[2][2] == 2:
            win = 'V2'

      elif X[2][0] == X[1][1] == X[0][2] == 1:
            win = 'V1'

      elif X[2][0] == X[1][1] == X[0][2] == 2:
            win = 'V2'

      else:
            pass

      return win

def main():

      X = [[0,0,0],[0,0,0],[0,0,0]]
      p = 0
      while p<=8:
            for line in X:
                  print(line)
            j_1 = input('Jogador 1 (x,y): ')
            try:
                  # Validating the input.
                  if len(j_1) == 3 and int(j_1[0]) >= 0 and int(j_1[2]) <= 2:
                        # Checking if the place is already filled.
                        if X[int(j_1[0])][int(j_1[2])] == 0:
                              # Marking the place for the player 1.
                              X[int(j_1[0])][int(j_1[2])] = 1
                              p += 1
                              print("p: ",p)
                              for line in X:
                                    print(line)
                              if p == 9:
                                    print("Empate")
                                    break
                              else:
                                    # Checking if there is a winner.
                                    if winner(X)[0] == 'V':
                                          print(winner(X)[1])
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
                              p += 1
                              print("p: ",p)
                              for line in X:
                                    print(line)
                              # Checking if there is a winner.
                              if winner(X)[0] == 'V':
                                    print(winner(X)[1])
                                    break
                              else: 
                                    pass
                              print("\n", '=================================', "\n")
                        
                        else:
                              raise InvalidPlay

                  else:
                        raise InvalidInput 

            except:
                  raise InvalidInput
main()