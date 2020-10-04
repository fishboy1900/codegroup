class InvalidInput(Exception):
	pass

class InvalidPlay(Exception):
	pass

def hash_board(X):
    
    tabuleiro =  '''
{} | {} | {}
------------
{} | {} | {}
------------
{} | {} | {}
'''.format(*X[0], *X[1], *X[2])

    return tabuleiro
    
def winner(X):
  # Horizontal case.
    for l in range(3):
        if X[l][0] == X[l][1] == X[l][2] != 0:
            return True

  # Vertical case.
    for c in range(3):
        if X[0][c] == X[1][c] == X[2][c] != 0:
            return True

  # Diagonal cases.
    if X[0][0] == X[1][1] == X[2][2] != 0:
        return True

    elif X[2][0] == X[1][1] == X[0][2] != 0:
        return True


def main():

    X = [[0,0,0],[0,0,0],[0,0,0]]
    valid_input = (0, 1, 2)
    
    # infinite loop
    while True:
        # looping to change player
        for player in (1,2):
            # printing the hash board
            print(hash_board(X))
            
            move = input('Por favor Jogador {}, faça sua jogada (x,y): '.format(player))
            # built in function to cut the input in two pair tuple
            move_tuple = move.split(",")
            move_tuple = [int(num) for num in move_tuple] # compact for to change strings to in

            try:
            # Validating the input.
                if move_tuple[0] in valid_input and move_tuple[1] in valid_input and X[move_tuple[0]][move_tuple[1]] == 0:
                    # Marking the place for the player 1 or 2.
                    X[move_tuple[0]][move_tuple[1]] = player
                    if winner(X):
                        print("Parabéns, o Jogador {} ganhou!!!".format(player))
                        return
                    
                    for line in X:
                        if 0 not in line:
                            print("Empate!")
                            return
                    else:
                        continue

            except:
                raise InvalidInput

main()