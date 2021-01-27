import math
import re
from collections import OrderedDict
import numpy as np
import pickle

class InvalidWord(Exception):
      pass

''' ATENTION!!! If you don't have the pickle files or you decided to train it with another file,
 uncomment the secction below and run only one time, it will save the data in a pickle file'''

'''# Reading the file and creating a list with the lines:
file = list(open("Book Examples/bookOficial.txt", "r", encoding="utf8"))

# Saving file in a Pickle
with open('file.pkl', 'wb') as f:
      pickle.dump(file, f)
      
# Removing the whitespaces from that list:
Plist = [line.split() for line in Pfile]

# Flattening the list of lists, whitout whitespaces, in one single list:
Wlist = [item for lst in Plist for item in lst]

# Creating a Basis of words(removing repetitive words and non alpha-numeric symbols and numbers):
Wbasis = list(dict.fromkeys([re.sub(r'[^\w]|[0-9]', '', wrd) for wrd in Wlist]))

# Saving Wbasis in a pickle:
with open('wbasis.pkl', 'wb') as b:
      pickle.dump(Wbasis, b)

# Creating a Basis of letters:
Lbasis = list(dict.fromkeys([lttr for wrd in Wbasis for lttr in wrd]))

# Saving Lbasis in a pickle:
with open('lbasis.pkl', 'wb') as i:
      pickle.dump(Lbasis, i)

# Transforming every word of Wlist in normalized vectors in Lbasis and putting them out in a dictionary:
Wdict = {}
print('Aprendendo com livro...\n')
for wrd in Wbasis:
      Wvector = [0 for i in range(len(Lbasis))]
      for lttr in wrd:
            Wvector[Lbasis.index(lttr)] += 1
      # Here i am just normalizing the vectors and dealing with errors:
      try:
            AWvector = np.array(Wvector)
            Wvector = [n/(sum(np.multiply(AWvector, AWvector))**0.5) for n in Wvector]
            Wdict[wrd] = Wvector
      except:
            Wbasis.remove(wrd)

# Saving Wdict in a pickle:
with open('wdict.pkl', 'wb') as d:
      pickle.dump(Wdict, d)'''

# Accessing file from pickle:
with open('file.pkl', 'rb') as f:
      Pfile = pickle.load(f)

# Accessing Wdict from pickle:
with open('wdict.pkl', 'rb') as d:
      Wdict = pickle.load(d)

# Accessing Wbasis from pickle:
with open('wbasis.pkl', 'rb') as b:
      Wbasis = pickle.load(b)

# Accessing Lbasis from pickle:
with open('lbasis.pkl', 'rb') as i:
      Lbasis = pickle.load(i)

# Gathering a word from the user:
Wuser = input('Insira uma palavra que deseja verificar: \n')

# Validating the input:
if ' ' in Wuser or bool(re.search(r'\d', Wuser)):
      raise InvalidWord
else:
      pass

# Transforming the input word in a normalized vector:
Uvector = [0 for i in range(len(Lbasis))]
for lttr in Wuser:
      Uvector[Lbasis.index(lttr)] += 1

# Here i am just normalizing the vector:
try:
      AUvector = np.array(Uvector)
      Uvector = [n/(sum(np.multiply(AUvector, AUvector))**0.5) for n in Uvector]
except:
      print('Deu erro parceiro, tenta outra palavra :)')

# Comparing the similar words:
Sdict = {}
print('Comparando com palavra similares...\n\n')
flag = False
for wrd in Wbasis:
      if len(Wuser) == len(wrd):

            # Scoef is the cosine between the two vectors...
            Scoef = sum(np.multiply(np.array(Wdict[wrd]), np.array(Uvector)))
            Sdict[str(wrd)] = Scoef
            flag = True
      else:
            pass

# Showing the results:
if flag == True:
      print('A palavra mais similar a "' + str(Wuser) + '" encontrada foi "' + str(max(Sdict, key=Sdict.get)) + '", com '+ str(100*float(Sdict[str(max(Sdict, key=Sdict.get))])) + '% de confiança')
else:
      print('Desculpe mas não encontramos nenhuma palavra similar a esta, tente novamente!')