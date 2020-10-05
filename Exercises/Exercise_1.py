'''1 - Criar uma função que pergunta qual o valor de A, qual o valor de B. E printa A + B no terminal(A função deve 
verificar se A e B são números, caso contrário deverá printar a seguinte mensagem: "A ou B não é número").'''

def question_1():
      # Collecting the values of A and B from the user.
      A = input("Insira o valor de A: ")
      B = input("Insira o valor de B: ")

      # Checking if A or B is not a number using the 'try funcion'.
      try:
            A = float(A)
            B = float(B)

            # If they are both numbers, lets sum it.
            soma = A + B

            # Now let's print it out.
            print(soma)     

      # If they aren't numbers, it's gonna occur the following.
      except: 
            print("A ou B não é número")

# Uncomment the line below to call the function.
#question_1()

#========================================= X =========================================#

'''2 - Criar uma função usando o iterador 'For' que dado uma lista de n números inteiros retorna a soma dos números 
dessa lista(não use a função padrão sum()).'''

def question_2():
      # Creating a list of numbers.
      lst = [1, 5, 2, 6, 3, -10]

      # Defining the variable 'soma'.
      soma = 0

      # Adding the numbers to 'soma'. 
      for n in lst:
            soma = soma + n
            # Obs.: You can type 'soma += n' instead of 'soma = soma + n'.

      # We can return the 'soma' variable to make things more easy.
      return soma

# Uncomment the line below to call the function.
#question_2()

#========================================= X =========================================#

'''3 - Criar um dicionário com três carros, cujos nomes são: "carro1", "carro2" e "carro3".
 Onde cada carro possui uma cor e um preço. Você deverá criar uma função que retorne a soma do preço de 
 todos os carros.'''

 # Creating a dictionary of dictionaries.
dct = {
      'carro1': {'cor': 'azul', 'preço': 10000}, 
      'carro2': {'cor': 'vermelho', 'preço': 15000},
      'carro3': {'cor': 'verde', 'preço': 20000}
      }

def question_3():
      # Defining the 'soma' variable.
      soma = 0

      # Adding the price of the cars.
      for c in dct:
            # For each car in the dictionary we are going to add them up in 'soma' variable.
            soma += dct[c]['preço']

      # When the function question_3(), it is gonna return the variable 'soma'.
      return soma

# Uncomment the line below to call the function.
#question_3()