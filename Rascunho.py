import random as rd
import pandas as pd

X = [[7,0,0],[0,0,0],[0,0,0]]
# Lets make a list of coordinates to make things easier.
cor = ['(0,0)','(0,1)','(0,2)','(1,0)','(1,1)','(1,2)','(2,0)','(2,1)','(2,2)']
nX = []

# Turning the list of lists 'X' into one single list.
for sublist in X:
      for item in sublist:
            nX.append(item)

df = pd.DataFrame(columns = ['(0,0)','(0,1)','(0,2)','(1,0)','(1,1)','(1,2)','(2,0)','(2,1)','(2,2)', 'Winner'])

for i in range(1):
      for i in range(9):
            print('fodasse')


print(df)