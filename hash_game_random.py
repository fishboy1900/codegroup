import random as rd
import pandas as pd
import numpy as np

# Function that receives the list of lists X and return the winner.
def winner(X):
      win = 'N'
      # Horizontal cases.
      for l in range(3):
            if X[l][0] == X[l][1] == X[l][2] == 1:
                  win = 'V1'

            elif X[l][0] == X[l][1] == X[l][2] == 2:
                  win = 'V2'

            else:
                  pass

      # Vertical cases.
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

      # Tie case.
      if (0 not in X[0] and 0 not in X[1] and 0 not in X[2]) and win == 'N':
            win = 'E0'

      else:
            pass

      return win

# Now we are going to generate some random games, check who is the winner and append it to a Pandas DataFrame.
X = [[0,0,0],[0,0,0],[0,0,0]]
nX = []

# Defining the structure of the Pandas Dataframe.
df = pd.DataFrame({'(0,0)': np.NaN,'(0,1)': np.NaN,'(0,2)': np.NaN,'(1,0)': np.NaN,'(1,1)': np.NaN,'(1,2)': np.NaN,'(2,0)': np.NaN,'(2,1)': np.NaN,'(2,2)': np.NaN, 'Winner': np.NaN}, columns = ['(0,0)','(0,1)','(0,2)','(1,0)','(1,1)','(1,2)','(2,0)','(2,1)','(2,2)', 'Winner'])

def main():
      global df

      X = [[0,0,0],[0,0,0],[0,0,0]]

      # Defining the players.
      j_1 = rd.randint(1,2)
      j_2 = 3-j_1
      # First player.
      while 0 in X[0] or 0 in X[1] or 0 in X[2]:
            a_1 = rd.randint(0,2)
            a_2 = rd.randint(0,2)
            # Checking if the random is open to receive a position.
            if X[a_1][a_2] == 0:
                  X[a_1][a_2] = j_1
                  
                  # Checking if the player won with this movement.
                  if winner(X)[0] == 'V':
                        break

                  # Checking if there is a tie.     
                  elif winner(X)[0] == 'E':
                        break
                  else:
                        pass
                  c = 0
                  # Second player.
                  while (0 in X[0] or 0 in X[1] or 0 in X[2]) and c == 0: 
                        b_1 = rd.randint(0,2)
                        b_2 = rd.randint(0,2)
                        # Checking if the random cell is zero.
                        if X[b_1][b_2] == 0:
                              X[b_1][b_2] = j_2

                              # 'c' is to identify that the second player has made a move.
                              c = 1
                              # Checking if the player won with this movement.
                              if winner(X)[0] == 'V':
                                    break

                              # Checking if there is a tie.      
                              elif winner(X)[0] == 'E':
                                    break
                                    
                              else: 
                                    pass
                        else:
                              pass
            else:
                  pass

      # Inserting the values into a new pandas dataframe row.
      df = df.append({'(0,0)': X[0][0],'(0,1)': X[0][1],'(0,2)': X[0][2],'(1,0)': X[1][0],'(1,1)': X[1][1],'(1,2)': X[1][2],'(2,0)': X[2][0],'(2,1)': X[2][1],'(2,2)': X[2][2], 'Winner': winner(X)[1]}, ignore_index=True)

j = 0
for i in range(5000):
      main()
      j = j + 1
      print(j)

df.to_csv('result.csv')